<?php require_once('auth.php'); ?>
<html>
<head>
<title>Websheets Grades</title>
</head>
<body>
<div id='info'><?php echo $GLOBALS['WS_AUTHINFO']['info_span']; ?> </div>
<?php
global $WS_AUTHINFO;
if (!$WS_AUTHINFO['logged_in']) {
  echo "You have to log in to see your students' grades.";
 }
 else {
  require_once('edit.php');
  $_REQUEST['action'] = 'showgrades';
  $editout = run_edit_py();
  //  echo $editout;
  $result = json_decode($editout, true);
  if (is_string($result))
    echo $result;
  else if (count($result['grades']) == 0)
    echo "You have no students.";
  else {
    $count = 0;
    echo "<pre>{";
    foreach ($result['grades'] as $student => $info) {
      if ($count > 0) echo ",\n"; else echo "\n";
      $count++;
      echo json_encode($student) . ": {";
      $count2 = 0;
      foreach ($info as $problem => $results) {
        if ($count2 > 0) echo ",\n"; else echo "\n";
        $count2++;
        echo "    ".json_encode($problem).": ".json_encode($results);
      }
      echo "\n  }";
    }
    echo "\n}";
  }
 }
 ?>
</body>
</html>
