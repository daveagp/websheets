<?php

if (!array_key_exists('stdin', $_REQUEST)
    || !array_key_exists('args', $_REQUEST))
  {
    echo "Internal error, malformed request to Websheet.php";
    die;
  }
$stdin = $_REQUEST["stdin"];
$args = $_REQUEST["args"];

// only accept characters that cannot cause problems
if (!preg_match("@^[0-9a-zA-Z_. ]*$@", $args)) {
  echo "Internal error, malformed arguments \"$args\"";
  die;
 }

$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

$process = proc_open("./submit.py " . $args, $descriptorspec, $pipes);
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