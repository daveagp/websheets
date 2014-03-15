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
  if (phpCAS::isAuthenticated()) {
    if (isset($_REQUEST['logout'])) {
      phpCAS::logout();
    }
    define ('WS_USERNAME', phpCAS::getUser());
    define ('WS_LOGGED_IN', true);
    define ('WS_LOGOUT_LINK', "?logout=");
  }
  else {    
    phpCAS::forceAuthentication();
    define ('WS_USERNAME', "fakestudentthatcannotbelogged"); // not terribly secure
    define ('WS_LOGGED_IN', false);
    define ('WS_LOGIN_LINK', "?login=");
  }
}
else { // not at princeton
    define ('WS_USERNAME', "fakestudentthatcannotbelogged"); // not terribly secure
    define ('WS_LOGGED_IN', false);
}