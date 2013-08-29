<?php

if (!array_key_exists('user_state', $_REQUEST)
    || !array_key_exists('module', $_REQUEST))
  {
    echo "Internal error, malformed request to check.php";
    die;
  }
$user_state = $_REQUEST['user_state'];
$module = $_REQUEST['module'];

if (!preg_match("@^[a-zA-Z_]+$@", $module)) {
  echo "Internal error, malformed module name \"$module\"";
  die;
 }

$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

$process = proc_open("./Websheet.py poschunks $module", $descriptorspec, $pipes);
if (!is_resource($process)) {
  echo "Internal error, could not run Websheet program";
  die;
 }

fwrite($pipes[0], $user_state);
fclose($pipes[0]);
$stdout = stream_get_contents($pipes[1]);
fclose($pipes[1]);
$stderr = stream_get_contents($pipes[2]);
fclose($pipes[2]);
$return_value = proc_close($process);

if ($stderr != "" || $return_value != 0) {
  echo "Internal error: ";
  echo $stdout . $stderr . "\nReturned $return_value";
  die;
 }

echo $stdout;