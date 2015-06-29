<?php require_once('auth.php'); ?>
<html>
<head>
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
<style>
   .howto {font-size: 75%;}
   .CodeMirror {height: auto; border:1px solid black;}
   .cm-container {max-height: 50vh; overflow:auto;}
   .rowlabel {text-align:right;}
   .widget {text-align:left;}
</style>
<script type='text/javascript'> 
  $(function(){$('#info').prepend(websheets.authinfo.info_span)});

  websheets.urlbase = '.';          // where do load.php, submit.php etc live?
  websheets.header_toggling = false; // start closed and open/close by a click?
  websheets.require_login = true;   // refuse to work with non-logged in users?
  // next line is how load requests know who is logged in (or not)
  websheets.authinfo = <?php echo json_encode($GLOBALS['WS_AUTHINFO']); ?>;
</script>
</head>
<body>
<div id='info'></div>
<p><button>New Websheet</button> <button>List all Websheets I've authored</button>
<hr>
<div class='editor'>
<p>Currently editing <tt>blah/blah</tt>. <button>Preview</button> <button>Save</button> <button>Rename</button> <button>Copy</button> <button>Export</button> <button>Import</button> <button>Delete</button> 
<table id='editor' style='width:100%'>
   <tr><th style='width:250px'>Property</th><th style='text-align:left'>Value</th></tr>
</table>
<hr style='width:50%'>
<p>Optional properties:<span id='optionals'></span>
<p>
Note: problems are open-source by default (see 'Public permissions'). 
License is <a href='https://creativecommons.org/licenses/by/4.0/'>Creative Commons 4.0 Attribution</a> unless you specify in 'Remarks'.
<hr>
<p>(Preview will disappear if any settings are changed.)
<p>Preview here.
</div>
</body>
</html>