<?php

  /*

requires: ws-config.json

authenticates user. processes $_REQUEST variables:
- auth: optional. "logout" to log out or "Google", "Facebook" to log in
- ajax_uid_intended: optional. signals this is an ajax request. if auth'ed
  user not equal to this, signal an error (if no other errors)

output: defines 2 global associative arrays.

WS_AUTHINFO contains info that can be made PUBLIC to the user and which can be converted to JSON:

["logged_in"] : boolean
["username"] : email address, or "anonymous"
["domain"] : currently logged-in domain: Facebook/Google/Princeton/etc or "n/a"
["providers"] : list of known providers
["error_span"] : html-formatted error message (bad server config, auth expiry) or empty string if none.
["info_span"] : very simple user-showable summary of authentication status, for convenience
["required_username_suffix"] : blank if n/a, or required login domain, used for error message UI
["is_super"] : is this a super user?
 (e.g., cant load config file, user has wrong domain, ajax user expired etc)

WS_CONFIG is the contents of ws-config.json and MUST BE KEPT PRIVATE since it will have things like database credentials

   */

global $WS_AUTHINFO, $WS_CONFIG;
$WS_AUTHINFO = array("logged_in"=>false); // by default

  // try to load the ws-config.json file and see if it includes required fields
$error = ''; // no news is good news
$data = file_get_contents(dirname(__FILE__)."/ws-config.json");
if ($data == FALSE) {
  $error = "Couldn't find ws-config.json";
  $error .= "<br><b>You cannot submit any code.</b>";
}
else {
  $WS_CONFIG = json_decode($data, TRUE); // associative array
  if ($WS_CONFIG == NULL) {
    $error = "ws-config.json is not JSON formatted";
  }
  else foreach (array("safeexec-executable-abspath", "java_jail-abspath", 
                      "baseurl", 
                      "db-password", "db-database", "db-user", "db-host") 
                as $required) {
      if (!array_key_exists($required, $WS_CONFIG)) {
        $error = "ws-config.json does not define $required";
        if ($required=="safeexec-executable-abspath" 
            || $required=="java_jail-abspath")
          $error .= "<br><b>You cannot submit any code.</b>";
        break;
      }
    }      
}

// someone who is logged in, should not be required to log in for this long
// main reason is to avoid hitting rate limit on authentication server
$cookie_renew_seconds = 60*90; // 90 minutes, length of a class

// server-side cookie management
ini_set('session.gc_maxlifetime', $cookie_renew_seconds); // expires after 90 unused minutes
session_start();
$now = time();
if (isset($_SESSION['discard_after']) && $now > $_SESSION['discard_after']){
   // this session has worn out its welcome; 
   // kill it and start a brand new one
   session_unset();
   session_destroy();
   session_start();
}
$_SESSION['discard_after'] = $now + $cookie_renew_seconds;

// client-side cookie management
// just in case their clock is screwed up, let them keep it forever so server can reject them 
$params = session_get_cookie_params();
setcookie(session_name(), session_id(), 0, $params['path'], 
        $params['domain'], $params['secure'], isset($params['httponly']));
// old approach: ini_set('session.cookie_lifetime', 0);

if ($error != "") {
  $WS_AUTHINFO["providers"] = array();  
}
else {
   if (array_key_exists("required_username_suffix", $WS_CONFIG)) {
      $WS_AUTHINFO["required_username_suffix"] = 
         $WS_CONFIG["required_username_suffix"];
   }   

  $ha_config = array();
  $ha_config["base_url"] = $WS_CONFIG["baseurl"] . "/hybridauth/hybridauth/index.php";
  $ha_config["providers"] = array();

  // configure Facebook if details exist in ws-config.json
  if (array_key_exists("facebook-id", $WS_CONFIG) 
      && array_key_exists("facebook-secret", $WS_CONFIG)) {
    $ha_config["providers"]["Facebook"] = 
      array("enabled" => true,
            "keys"    => 
            array("id" => $WS_CONFIG["facebook-id"],
                  "secret" => $WS_CONFIG["facebook-secret"]
                  ),
            "scope"   => "email",
            );
  }    

  // configure Google if details exist in ws-config.json
  if (array_key_exists("google-id", $WS_CONFIG) 
      && array_key_exists("google-secret", $WS_CONFIG)) {
    $ha_config["providers"]["Google"] = 
      array("enabled" => true,
            "keys"    => 
            array("id" => $WS_CONFIG["google-id"],
                  "secret" => $WS_CONFIG["google-secret"]
                  ),
            "scope"           => "https://www.googleapis.com/auth/userinfo.email",
            "access_type"     => "online",
            "approval_prompt" => "auto",
	    "name" => "Google",
      );
    if (array_key_exists("google-apps-domain", $WS_CONFIG)) {
       $ha_config["providers"]["Google"]["hd"] = 
          $WS_CONFIG["google-apps-domain"];
    }
  }

  //echo json_encode($ha_config);
  
  // now call the hybridauth library
  require_once( dirname(__FILE__)
                ."/hybridauth/hybridauth/Hybrid/Auth.php" ); 
  $hybridauth = new Hybrid_Auth( $ha_config );

  if (!array_key_exists('auth', $_REQUEST))
     $_REQUEST['auth'] = '';

  if ($_REQUEST['auth']=='logout') {
    $hybridauth->logoutAllProviders();
  }

  $cookied = false;

  // see if the cookie has saved a previous login
  if (array_key_exists('WS_AUTHINFO', $_SESSION)) {
     $cookiedomain = $_SESSION['WS_AUTHINFO']['domain'];
     $requestdomain = '';
     if (array_key_exists('auth', $_REQUEST))
        $requestdomain = $_REQUEST['auth'];
     if ($requestdomain == '' || $requestdomain == $cookiedomain) {
        $cookied = true;
        $WS_AUTHINFO = $_SESSION['WS_AUTHINFO'];
     }
  }

  // else try logging in, also build a list of providers
  if (!$cookied) 
  foreach ($ha_config["providers"] as $authdomain => $domaininfo) {
    $WS_AUTHINFO['providers'][] = $authdomain;

    // tries to log in twice. the reason is that an exception can be thrown
    // on the first attempt. if two exceptions, just log out.
    // however, it actually reloads the page on the second time,
    // so a persistent hybridauth bug could cause an infinite redirect loop.
    for ($i=0; $i<2; $i++) {
       // hybridauth doesn't let you authenticate through ajax. so ajax
       // (which won't use 'auth') will only reuse existing connection
       if ($_REQUEST['auth']==$authdomain || 
           $_REQUEST['auth']=='' 
           && $hybridauth->isConnectedWith($authdomain)) {
          $adapter = $hybridauth->authenticate( $authdomain );  
          try {
             $user_profile = $adapter->getUserProfile(); 
             $un = $user_profile->emailVerified;

             if (array_key_exists("required_username_suffix", $WS_CONFIG)) {
               $rus = $WS_CONFIG["required_username_suffix"];
               
               // logged in with invalid account.
               // this usually can't happen if you use Google's "hd" option
               if (!(substr($un, -strlen($rus)) === $rus))  {
                 $error = "You need to log in with your an email address ending
 in $rus. You logged in as $un instead. Please 
<a href='javascript:websheets.auth_reload(\"logout\")'>log out</a>. 
In case of problems you may need to visit $authdomain in a new tab/window 
and sign out."; 
                 $hybridauth->logoutAllProviders();
                 break;
               }
             }

             //if (rand(0, 10)<8) throw new Exception(); //for testing
             $WS_AUTHINFO['username'] = $un; 
             $WS_AUTHINFO['domain'] = $authdomain; 
             $WS_AUTHINFO['logged_in'] = true;
             break;
          }
          catch (Exception $e) {
             $hybridauth->logoutAllProviders();
          }
       }
    }
  }     
  
  // some schools will want to use their own authentication. example:
  if (substr($_SERVER['SERVER_NAME'], -13)=='princeton.edu') {
    $WS_AUTHINFO['providers'][] = "Princeton";
    
    include_once('../CAS-1.3.2/CAS.php');
    phpCAS::setDebug();
    phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
    phpCAS::setNoCasServerValidation();
    
    if ($_REQUEST['auth']=='Princeton') {
      phpCAS::forceAuthentication();
    }
    
    if (phpCAS::isAuthenticated() && !$WS_AUTHINFO['logged_in']) {
      if ($_REQUEST['auth']=='logout') {
        phpCAS::logout();
      }
      
      $WS_AUTHINFO['username'] = phpCAS::getUser() . '@princeton.edu';
      $WS_AUTHINFO['domain'] = 'Princeton'; 
      $WS_AUTHINFO['logged_in'] = true;
    }     
  }

// pass the list of authentication services to the next php file
  if ($WS_AUTHINFO["providers"] == array()) {
     $error = "No authentication providers are configured.";
  }
}

// define all remaining constants
if (!$WS_AUTHINFO["logged_in"]) {
   $WS_AUTHINFO["username"] = "anonymous";
   $WS_AUTHINFO["domain"] = "n/a";
   // nuke the php session
   session_unset();
   session_destroy();
   $params = session_get_cookie_params();
   setcookie(session_name(), '', 0, $params['path'], $params['domain'], $params['secure'], isset($params['httponly']));
}

$WS_AUTHINFO['is_super'] = array_key_exists("super_users", $WS_CONFIG) && 
  in_array($WS_AUTHINFO["username"], $WS_CONFIG["super_users"]);

// check if an ajax request was not authenticatable by the expected user
if ($error == "" && array_key_exists("ajax_uid_intended", $_REQUEST)) {
   $aui = $_REQUEST["ajax_uid_intended"];
   if (!$WS_AUTHINFO["logged_in"] && $aui != "anonymous") {
      $error = "This page was loaded as <tt>$aui</tt> but your login token
has expired. <a href='javascript:websheets.popup_reauth()'>
Please click here to fix it (pops up a new link)</a> then try again. 
Sorry for the inconvenience.";
   }
   else if ($aui == "anonymous" && $WS_AUTHINFO["logged_in"]) {
      $error = "This page was loaded anonymously, but you have logged in
on another window as <tt>".$WS_AUTHINFO["username"]."</tt>. Please
click the login link on this page if you want your work saved under your account.
Copy your work to a text editor if you want to avoid losing it.
";
   }
   else if ($aui != "anonymous" && $aui != $WS_AUTHINFO["username"]) {
      $error = "This page was loaded as <tt>$aui</tt>, but you have logged in
on another window as <tt>".$WS_AUTHINFO["username"]."</tt>.";
   }
}

$WS_AUTHINFO["error_span"] = "";

if (strlen($error) != 0) {
   $WS_AUTHINFO["error_span"] = "<span class='ws_error_span'><i>$error</i>
   <script type='text/javascript'>
   $(function(){alert('Error! Please see status message.');});</script></span>";
}

$gets = '?';
foreach ($_GET as $key=>$val)
  $gets .= urlencode($key) .'='. urlencode($val) . '&';


if (strlen($error) != 0)
   $WS_AUTHINFO["info_span"] = "<span class='ws_info_span'><i>$error</i>
   <script type='text/javascript'>
   $(function(){alert('Error! Please see status message.');});</script></span>";
else if ($WS_AUTHINFO['logged_in'])
   $WS_AUTHINFO["info_span"] = "<span class='ws_info_span'>Logged in as " . $WS_AUTHINFO["username"] 
      . " via " . $WS_AUTHINFO["domain"] 
      . ". <a href='$gets"."auth=logout'>Log out.</a></span>";
else {
   $msg = "<span class='ws_info_span'>Not logged in. Log in with";
   foreach ($WS_AUTHINFO["providers"] as $i => $p)
     $msg .= ($i==0?"":" or")." <a href='$gets"."auth=$p'>$p</a>";
   $WS_AUTHINFO["info_span"] = $msg . '.</span>';
}

