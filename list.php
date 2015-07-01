<?php require_once('auth.php'); ?>
<html>
<head>
<script type='text/javascript' src='jquery.min.js'></script>
<style>
table#list tr td:first-child {text-align:right;}
</style>
</head>
<body>
<div id='info'><?php echo $GLOBALS['WS_AUTHINFO']['info_span']; ?></div>
<table id='list'>
<?php 
if ($GLOBALS['WS_AUTHINFO']['logged_in']) {
  require_once('edit.php');
  $_REQUEST['action'] = 'listmine';
  $editout = run_edit_py();
  //  echo $editout;
  $result = json_decode($editout, true);
  $author = '';
  $readonly = false;
  if (is_string($result))
    echo $result;
  else {
    foreach ($result['problems'] as $probleminfo) {
      $name = $probleminfo[1];
      $i = strrpos($name, '/');
      if ($i == -1) $folder = ""; else $folder = substr($name, 0, $i);
      $slug = substr($name, $i+1);
      $sharing = $probleminfo[2];
      $action = $probleminfo[0]?'View':'Edit';
      echo "<tr><td>$name</td><td><a href='editor.php?edit=$name'>$action</a></td>";
      if ($sharing != 'draft') echo "<td><a href='./?folder=$folder&start=$slug'>Solve</a></td>";
      echo '</tr>';
    }
  }
}
?>
</table>
</body>
</html>