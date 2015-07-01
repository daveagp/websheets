<?php
include_once('auth.php');

global $WS_AUTHINFO;
if ($WS_AUTHINFO["error_span"] != "") {
   echo json_encode($WS_AUTHINFO);
   die();
}

if (!array_key_exists('stdin', $_REQUEST)
    || !array_key_exists('problem', $_REQUEST))
  {
    echo "Internal error, malformed request to submit.php";
    die;
  }

$client_request = json_decode($_REQUEST["stdin"], true);
if ($client_request == FALSE) {
  echo "Internal error, request did not receive a json on stdin";
  die;
 }

$problem = $_REQUEST["problem"];

// only accept characters that cannot cause problems
if (!preg_match("@^[0-9a-zA-Z_/-]+$@", $problem)) {
  echo "Internal error, malformed problem \"$problem\"";
  die;
 }

$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

$stdin = json_encode(array("client_request" => $client_request,
                           "authinfo" => $WS_AUTHINFO,
                           "php_data" => array("user"=>$WS_AUTHINFO['username'],
                                               "problem"=>$problem,
                                               "meta"=>array("authdomain"=>$WS_AUTHINFO['domain'],
                                                             "preview"=>$client_request['preview'],
                                                             "ip"=>$_SERVER['REMOTE_ADDR']))));

$process = proc_open("./submit.py", $descriptorspec, $pipes);

if (!is_resource($process)) {
  echo "Internal error, could not run Websheet program";
  die;
 }

fwrite($pipes[0], $stdin);
fclose($pipes[0]);
$stdout = stream_get_contents($pipes[1]);
fclose($pipes[1]);
$stderr = stream_get_contents($pipes[2]);
fclose($pipes[2]);
$return_value = proc_close($process);

if ($stderr != "" || $return_value != 0) {
  echo "Internal error: <pre>";
  echo $stdout . $stderr . "\nReturned $return_value</pre>";
  die;
 }

echo $stdout;