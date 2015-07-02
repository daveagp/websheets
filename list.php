<?php require_once('auth.php'); ?>
<html>
<head>
<style>
table#list tr td:first-child {text-align:right;}
.hidemine .mine {display:none;}
.hidenotmine .notmine {display:none;}
</style>
</head>
<body>
<div id='info'><?php echo $GLOBALS['WS_AUTHINFO']['info_span']; ?> </div>
<div>
<a href='#' onclick='window.list.className="hidenotmine"'>Show only my websheets</a>
<a href='#' onclick='window.list.className="hidemine"'>Show only other authors' websheets</a>
<a href='#' onclick='window.list.className=""'>Show all websheets</a>
</div>
<table id='list'>
<?php 
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
      $name = $probleminfo[0];
      $i = strrpos($name, '/');
      if ($i == -1) $folder = ""; else $folder = substr($name, 0, $i);
      $slug = substr($name, $i+1);
      $sharing = $probleminfo[2];
      $action = $probleminfo[1]?'View Source':'Edit';
      $class = $probleminfo[1]?'notmine':'mine';
      echo "<tr class='$class'><td>$name</td><td><a href='editor.php?edit=$name'>$action</a></td>";
      if ($sharing != 'draft') echo "<td><a href='./?folder=$folder&start=$slug'>Solve</a></td>";
      echo '</tr>';
    }
  }
?>
</table>
</body>
</html>