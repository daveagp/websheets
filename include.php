<?php
define ('WS_PRINCETON', substr($_SERVER['SERVER_NAME'], -13)=='princeton.edu');

//** needs some work to sanitize secrets and deal with base_url **//
 
$config = array( 
                "base_url" => "http://cscircles.cemc.uwaterloo.ca/dev/websheets/hybridauth/hybridauth/index.php",  
                "providers" => 
                array("Facebook" => 
                      array("enabled" => true,
                            "keys"    => 
                            array("id" => file_get_contents("keys/facebook-id"),
                                  "secret" => file_get_contents("keys/facebook-secret"),
                                  ),
                            "scope"   => "email",
                            ),    

                      "Google" => 
                      array("enabled" => true,
                            "keys"    => 
                            array("id" => file_get_contents("keys/google-id"),
                                  "secret" => file_get_contents("keys/google-secret"),
                                  ),
                            "scope"           => "https://www.googleapis.com/auth/userinfo.email",
                            "access_type"     => "online",
                            "approval_prompt" => "force",
                            )));

if (WS_PRINCETON) {
  $config['base_url'] = "http://www.cs.princeton.edu/~cos126/websheets/hybridauth/hybridauth/index.php";
}

   require_once( "hybridauth/hybridauth/Hybrid/Auth.php" );
   
   $hybridauth = new Hybrid_Auth( $config );

   if ($_REQUEST['auth']=='logout') {
     $hybridauth->logoutAllProviders();
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
     phpCAS::setDebug();
     phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
     phpCAS::setNoCasServerValidation();

     if ($_REQUEST['auth']=='Princeton') {
       phpCAS::forceAuthentication();
     }

     if (phpCAS::isAuthenticated() &&  !defined('WS_LOGGED_IN')) {
       if ($_REQUEST['auth']=='logout') {
         phpCAS::logout();
       }

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

