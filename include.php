<?php
define ('WS_PRINCETON', substr($_SERVER['SERVER_NAME'], -13)=='princeton.edu');
if (WS_PRINCETON) {

  include_once('../CAS-1.3.2/CAS.php');
  phpCAS::setDebug();
  phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
  phpCAS::setNoCasServerValidation();
  if (isset($_REQUEST['login'])) {
    phpCAS::forceAuthentication();
  }
  define ('WS_USERNAME', phpCAS::getUser());
  define ('WS_LOGGED_IN', true);
}
else {
   $config = array( 
        "base_url" => "http://cscircles.cemc.uwaterloo.ca/dev/websheets/hybridauth/hybridauth/index.php",  
        "providers" => array (
            "Facebook" => array ( 
               "enabled" => true,
               "keys"    => array ( "id" => "493038877467966", 
                                    "secret" => "b1eaebe81d4be9cc3010c8f6e6e0f65d" ), 
               "scope"   => "email", // optional
               //"display" => "popup" // optional
               ),                                    
            "Google" => array ( 
              "enabled" => true,
              "keys"    => array ( "id" => "179206563569-936o4fmit27ua72ldeqvfmsbeu46uull.apps.googleusercontent.com", 
                                   "secret" => "wVKNo_KuR6gFJMxmbtjhtd9P" ), 
              "scope"           => //"https://www.googleapis.com/auth/userinfo.profile ". // optional
              "https://www.googleapis.com/auth/userinfo.email"   , // optional
              "access_type"     => "online",   // optional
              "approval_prompt" => "force",     // optional
              //                    "hd"              => "domain.com" // optional
              )));
   
   require_once( "hybridauth/hybridauth/Hybrid/Auth.php" );
   
   $hybridauth = new Hybrid_Auth( $config );

   if ($_REQUEST['auth']=='logout') {
     $hybridauth->logoutAllProviders();
     if (WS_PRINCETON) {
       phpCAS::logout();
     }
   }

   $providers = "";

   foreach ($config["providers"] as $authdomain => $domaininfo) {
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

   // special providers
   if (WS_PRINCETON) {
     $providers = " Princeton" . $providers;

     include_once('../CAS-1.3.2/CAS.php');
     if ($_REQUEST['auth']=='Princeton') {
       phpCAS::setDebug();
       phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
       phpCAS::setNoCasServerValidation();
       phpCAS::forceAuthentication();
     }

     if (phpCAS::isAuthenticated() &&  !defined('WS_LOGGED_IN')) {
       define ('WS_USERNAME', phpCAS::getUser() . '@princeton.edu');
       define ('WS_AUTHDOMAIN', 'Princeton'); 
       define ('WS_LOGGED_IN', true);
     }     
   }

   // e.g. "Facebook Google"
   define("WS_PROVIDERS", substr($providers, 1));

   if (!defined('WS_LOGGED_IN')) {
     define('WS_LOGGED_IN', false);
     define('WS_USERNAME', "anonymous");
     define('WS_AUTHDOMAIN', "n/a"); 
   }
}
