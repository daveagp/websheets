<?php
include_once('auth.php');

global $WS_AUTHINFO;
if ($WS_AUTHINFO["error_span"] != "") {
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
$preview = $_REQUEST["preview"]=='True' ? 'True' : 'False';

$student = $WS_AUTHINFO['username']; 
// for code review by instructor
if (array_key_exists('student', $_REQUEST) && $_REQUEST["student"]!="undefined"){
    $student = $_REQUEST["student"];
}

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

$process = proc_open("python3 ./load.py " . $problem . " " . $student . " " . $preview, $descriptorspec, $pipes);

if (!is_resource($process)) {
  echo "Internal error, could not run Websheet program";
  die;
 }

fwrite($pipes[0], json_encode($WS_AUTHINFO));
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
