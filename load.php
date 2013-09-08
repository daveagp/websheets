<?php
include_once('include.php');
if (!PRINCETON) {
  echo "false";
  die;
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
if (!preg_match("@^[0-9a-zA-Z]+$@", $problem)) {
  echo "Internal error, malformed problem \"$problem\"";
  die;
 }

$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

$process = proc_open("./load.py " . $problem . " " . WS_USERNAME, $descriptorspec, $pipes);
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