<?php
$descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin
                        1 => array("pipe", "w"),  // stdout
                        2 => array("pipe", "w"),  // stderr
                        );

#$process = proc_open("./submit.py bugfix_2013_11_01", $descriptorspec, $pipes);

if (!is_resource($process)) {
  echo "Internal error, could not run Websheet program";
  die;
 }

fwrite($pipes[0], "");
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