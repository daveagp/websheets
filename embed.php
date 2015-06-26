<?php 
// in principle you could maybe authenticate asynchronously and defer all 
// websheet loads until that is finished. this version authenticates synchronously.
require_once('auth.php');
?>
<html>
<head>

<!-- all of the requirements for an embedded websheet: -->
<script type='text/javascript' src='jquery.min.js'></script>
<script type='text/javascript' src='CodeMirror/lib/codemirror.js'></script>
<script type='text/javascript' src='CodeMirror/mode/clike/clike.js'></script>
<script type='text/javascript' src='CodeMirror/addon/selection/mark-selection.js'></script>
<script type='text/javascript' src='CodeMirror/addon/edit/matchbrackets.js'></script>
<link rel='stylesheet' type='text/css' href='CodeMirror/lib/codemirror.css'/>
<link rel='stylesheet' type='text/css' href='CodeMirror/theme/neat.css'/>
<link rel='stylesheet' type='text/css' href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700'/>
<script type='text/javascript' src='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
<link rel='stylesheet' type='text/css' href='websheets.css'/>
<script type='text/javascript' src='websheets.js'></script>
<script type='text/x-mathjax-config'> 
MathJax.Hub.Config({tex2jax: {displayMath: [ ['$$','$$'] ], inlineMath: [['$','$'] ]} });
</script>

<!-- configuration options: -->
<script type='text/javascript'> 
  websheets.urlbase = '.';          // where do load.php, submit.php etc live?
  websheets.header_toggling = true; // websheets start closed and open/close by a click
  websheets.require_login = true;   // refuse to work with non-logged in users?
  // next line is how load requests know who is logged in (or not)
  websheets.authinfo = <?php global $WS_AUTHINFO; echo json_encode($WS_AUTHINFO); ?>;
</script>
</head>

<body>

<!-- the user should have some way to log in or out: -->
<div style='text-align:center'><?php echo $WS_AUTHINFO['info_span']; ?></div>

<!-- the websheets! -->
Here is a Hello, World exercise in Java:
<div class='websheet-stub'>pointers/swap</div>
Here is a C++ scratchpad:
<div class='websheet-stub'>scratch</div>

</body>
