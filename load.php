<?php
include_once('auth.php');

global $WS_AUTHINFO;
if ($WS_AUTHINFO["error_div"] != "") {
   echo json_encode($WS_AUTHINFO);
   die();
}

if (//!array_key_exists('stdin', $_REQUEST) ||
     !array_key_exists('problem', $_REQUEST))
  {
    echo "Internal error, malformed request to load.php";
    die;
  }
//$stdin = $_REQUEST["stdin"];
$problem = $_REQUEST["problem"];

// only accept characters that cannot cause problems
$regex = "[_0-9a-zA-Z/-]+";
if (!preg_match("@^$regex\$@", $problem)) {
  echo "Internal error, problem name \"$problem\" doesn't match $regex";
  die;
 }

$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

$process = proc_open("./load.py " . $problem . " " . $WS_AUTHINFO['username'], $descriptorspec, $pipes);

if (!is_resource($process)) {
  echo "Internal error, could not run Websheet program";
  die;
 }

fwrite($pipes[0], "");//$stdin);
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