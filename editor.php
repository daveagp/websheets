<?php require_once('auth.php'); ?>
<html>
<head>
<script type="text/x-mathjax-config"> 
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]} });
</script>
<script type="text/javascript" 
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type='text/javascript' src='jquery.min.js'></script>
<script type='text/javascript' src='editor.js'></script>
<script type='text/javascript' src='websheets.js'></script>
<script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
<script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
<script type="text/javascript" src="CodeMirror/mode/javascript/javascript.js"></script>
<script type="text/javascript" src="CodeMirror/mode/xml/xml.js"></script>
<script type="text/javascript" src="CodeMirror/mode/css/css.js"></script>
<script type="text/javascript" src="CodeMirror/mode/htmlmixed/htmlmixed.js"></script>
<script type="text/javascript"
   src="CodeMirror/addon/selection/mark-selection.js"></script>
<script type="text/javascript"
   src="CodeMirror/addon/edit/matchbrackets.js"></script>
<link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
<link rel="stylesheet" href="CodeMirror/theme/neat.css">
<link rel="stylesheet" href="websheets.css">
<style>
   .howto {font-size: 75%;}
   .CodeMirror {height: auto; border:1px solid black;}
   .cm-container {max-height: 50vh; overflow:auto;}
   .rowlabel {text-align:right;}
   .widget {text-align:left;}
   table#editor .CodeMirror {font-size: 80%;}
   .unsaved-changes {font-style: italic; font-weight: bold; color: red; display: none;}
   table#editor tr td:first-child {width: 250px;}
   .readonly .hide-readonly {display: none;}
</style>
<script type='text/javascript'> 

  websheets.urlbase = '.';          // where do load.php, submit.php etc live?
  websheets.header_toggling = false; // start closed and open/close by a click?
  websheets.require_login = true;   // refuse to work with non-logged in users?
  // next line is how load requests know who is logged in (or not)
  websheets.authinfo = <?php echo json_encode($GLOBALS['WS_AUTHINFO']); ?>;

<?php 
if (!$GLOBALS['WS_AUTHINFO']['logged_in'])
  echo "websheets.initialize_error = 'You must log in to use the editor.';";
 else if (!array_key_exists('edit', $_REQUEST))
  echo "websheets.initialize_error = 'Please use one of the buttons above to start editing.';";
 else {
  require_once('edit.php');
  $_REQUEST['action'] = 'load';
  $_REQUEST['problem'] = $_REQUEST['edit'];
  $result = json_decode(run_edit_py(), true);
  $author = '';
  $readonly = false;
  if (is_string($result))
    echo "websheets.initialize_error = " . json_encode($result).";";
  else {
    if ($result['success']) {
      echo "websheets.initialize_editor = " . json_encode($result) . ";";
      $author = $result['author'];
      if ($author != $GLOBALS['WS_AUTHINFO']['username'])
        echo "websheets.editor_readonly = true;";
    }
    else
      echo "websheets.initialize_error = " . json_encode($result['message']).";";
  }
}
?>

</script>
</head>
<body>
<div id='info'><?php echo $GLOBALS['WS_AUTHINFO']['info_span']; ?></div>
<p><button id='reload' class='pure'>Create blank Websheet or open existing Websheet</button> <a href='./list.php'>List of all my Websheets</a>
<div id='error' style='display:none'>
</div>
<div class='editor'>
<hr>
<p><span id='doing'>Editing</span> <a href='./?start=<?php echo $_REQUEST['edit']; ?>'><tt><?php echo $_REQUEST['edit'];?></tt></a> by <tt><?php echo $author;?></tt>. <span class='unsaved-changes'>You have unsaved changes.</span> <button id='preview'>Preview</button> <button id='save'>Save</button> <button id='rename'>Rename</button> <button id='copy' class='pure'>Copy</button> <button id='export' class='pure'>Export</button> <button id='import'>Import</button> <button id='delete'>Delete</button> 
<table id='editor' style='width:100%'>
   <tr><th>Property</th><th style='text-align:left'>Value</th></tr>
</table>
<hr style='width:50%'>
<p class='hide-readonly'>Optional properties:<span id='optionals'></span>
<p>
Note: problems are open-source by default (see 'Public permissions'). 
License will be assumed to be <a href='https://creativecommons.org/licenses/by-sa/4.0/'>Creative Commons 4.0 Attribution-ShareAlike</a> unless otherwise specified in 'Remarks'.
<hr>
<div class='preview'></div>
</div> <!-- editor -->
</body>
</html>