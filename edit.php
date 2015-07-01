<?php
$edit_is_main = (count(get_included_files()) == 1);

require_once('auth.php');

# for internal errors, it will print a json-encoded string
# otherwise (including some errors), it will print a json-encoded object

function run_edit_py() {

  global $WS_AUTHINFO;
  if ($WS_AUTHINFO["error_span"] != "") 
    return json_encode($WS_AUTHINFO);
  
  $_REQUEST['authinfo'] = $WS_AUTHINFO;
  
  $package = json_encode($_REQUEST);
  
  $descriptorspec = array(
                          0 => array("pipe", "r"),  // stdin
                          1 => array("pipe", "w"),  // stdout
                          2 => array("pipe", "w"),  // stderr
                          );
  
  $process = proc_open("./edit.py", $descriptorspec, $pipes);
  
  if (!is_resource($process))
    return json_encode("Internal error, could not run Websheet program");
  
  fwrite($pipes[0], $package);
  fclose($pipes[0]);
  $stdout = stream_get_contents($pipes[1]);
  fclose($pipes[1]);
  $stderr = stream_get_contents($pipes[2]);
  fclose($pipes[2]);
  $return_value = proc_close($process);
  
  if ($stderr != "" || $return_value != 0)
    return json_encode("Internal error: <pre>$stdout$stderr\nReturned $return_value</pre>");
  
  return $stdout;
}

if ($edit_is_main) {
  echo run_edit_py();
}