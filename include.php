<?php

  /*

requires: config.json

authenticates user and defines several constants:

WS_LOGGED_IN : boolean
WS_USERNAME : email address, or "anonymous"
WS_AUTHDOMAIN : Facebook, Google, Princeton, etc or "n/a"
WS_PROVIDERS : space-separated list of known providers
WS_CONFIG_ERROR : string (error message, or empty string if config ok)

   */

  /*
    internal details:
?auth=logout will log out
?auth=XXX will try to log in with authentication domain XXX
  */

  // try to load the config.json file and see if it includes required fields
$config_error = ''; // no news is good news
$data = file_get_contents("config.json");
if ($data == FALSE) {
  $config_error = "Couldn't find config.json";
}
else {
  $config_jo = json_decode($data, TRUE); // associative array
  if ($config_jo == NULL) {
    $config_error = "config.json is not JSON formatted";
  }
  else foreach (array("hybridauth-base_url", "db-password", "db-database", "db-user", "db-host") as $required) {
      if (!array_key_exists($required, $config_jo)) {
        $config_error = "config.json does not define $required";
        break;
      }
    }      
}

if ($config_error != "") {
  define("WS_PROVIDERS", "");  
}
else {
  $ha_config = array();
  $ha_config["base_url"] = $config_jo["hybridauth-base_url"];
  $ha_config["providers"] = array();

  // configure Facebook if details exist in config.json
  if (array_key_exists("facebook-id", $config_jo) 
      && array_key_exists("facebook-secret", $config_jo)) {
    $ha_config["providers"]["Facebook"] = 
      array("enabled" => true,
            "keys"    => 
            array("id" => $config_jo["facebook-id"],
                  "secret" => $config_jo["facebook-secret"]
                  ),
            "scope"   => "email",
            );
  }    

  // configure Google if details exist in config.json
  if (array_key_exists("google-id", $config_jo) 
      && array_key_exists("google-secret", $config_jo)) {
    $ha_config["providers"]["Google"] = 
      array("enabled" => true,
            "keys"    => 
            array("id" => $config_jo["google-id"],
                  "secret" => $config_jo["google-secret"]
                  ),
            "scope"           => "https://www.googleapis.com/auth/userinfo.email",
            "access_type"     => "online",
            "approval_prompt" => "auto",
            );
  }

  //echo json_encode($ha_config);
  
  // now call the hybridauth library
  require_once( "hybridauth/hybridauth/Hybrid/Auth.php" ); 
  $hybridauth = new Hybrid_Auth( $ha_config );

  if ($_REQUEST['auth']=='logout') {
    $hybridauth->logoutAllProviders();
  }

  // try logging in, also build a list of providers
  $providers = "";
  foreach ($ha_config["providers"] as $authdomain => $domaininfo) {
    $providers .= " " . $authdomain;
    
    if ($_REQUEST['auth']==$authdomain)
      $hybridauth->authenticate( $authdomain );  
    
    if ($hybridauth->isConnectedWith($authdomain) && !defined('WS_LOGGED_IN')) {
      $adapter = $hybridauth->authenticate( $authdomain );  
      $user_profile = $adapter->getUserProfile(); 
      define ('WS_USERNAME', $user_profile->emailVerified); 
      define ('WS_AUTHDOMAIN', $authdomain); 
      define ('WS_LOGGED_IN', true);
    }     
  }
  
  // some schools will want to use their own authentication
  if (substr($_SERVER['SERVER_NAME'], -13)=='princeton.edu') {
    $providers = " Princeton" . $providers;
    
    include_once('../CAS-1.3.2/CAS.php');
    phpCAS::setDebug();
    phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
    phpCAS::setNoCasServerValidation();
    
    if ($_REQUEST['auth']=='Princeton') {
      phpCAS::forceAuthentication();
    }
    
    if (phpCAS::isAuthenticated() && !defined('WS_LOGGED_IN')) {
      if ($_REQUEST['auth']=='logout') {
        phpCAS::logout();
      }
      
      define('WS_USERNAME', phpCAS::getUser() . '@princeton.edu');
      define('WS_AUTHDOMAIN', 'Princeton'); 
      define('WS_LOGGED_IN', true);
    }     
  }

// pass the list of authentication services to the next php file
  if (strlen($providers) > 0) {
    // e.g. "Facebook Google"
    define("WS_PROVIDERS", substr($providers, 1));
  }
  else {
    define("WS_PROVIDERS", "");
    $config_error = "No authentication providers are configured.";
  }
}

// define all remaining constants
if (!defined('WS_LOGGED_IN')) {
  define('WS_LOGGED_IN', false);
  define('WS_USERNAME', "anonymous");
  define('WS_AUTHDOMAIN', "n/a"); 
}

if (strlen($config_error) > 0)
  $config_error = "<div><i>$config_error<br>You will not be able to log in, load, or save.</i></div>";
define('WS_CONFIG_ERROR', $config_error);