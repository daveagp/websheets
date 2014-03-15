<?php
include_once('include.php');
?><html>
<head>
   <title>Websheets</title>
   <link rel="icon" 
      type="image/png" 
      href="favicon.png">
   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
   <script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
   <script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
   <script type="text/javascript" src="CodeMirror/addon/selection/mark-selection.js"></script>
   <script type="text/javascript" src="CodeMirror/addon/edit/matchbrackets.js"></script>
   <script type="text/javascript" src="websheet.js?1"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
      });
</script>
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

   <link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
   <link rel="stylesheet" href="CodeMirror/theme/neat.css">
   <link rel="stylesheet" href="websheet.css?1">
  
   <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700' rel='stylesheet' type='text/css'>

   <script type="text/javascript" src="test.js?2"></script>

</head>
<body>
<div id="page">
  <div class="menu-bar noprint">
<?php if (WS_LOGGED_IN) {
   echo "<p>Logged in as <b>" . WS_USERNAME . "</b>. " .
   "Click to <a href='" . WS_LOGOUT_LINK . "'>log out</a>.</p>";
} ?>
   <p>This is an experimental system. <a href="mailto:dp6@cs.princeton.edu">Contact us</a>
    if you find bugs, typos, user interface issues, inaccurate grading or anything else.</p>
   Select a problem: <select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val())">
   </select>
   <script type='text/javascript'>
   var sheets = 
  <?php
       if (array_key_exists("group", $_REQUEST))
	 echo json_encode(explode(" ", $_REQUEST["group"]));
       else
	 echo passthru("./Websheet.py list") 
	   ?> 
    populateSheets(sheets);
   </script>
   <button id='resetButton'>Start over</button>
   <button id='answerButton'>View reference solution</button>
   </div> <!-- menu-bar -->
   <div id="container" style="display:none">
   <div class='exercise-header'>Exercise Description</div>
   <div id="description"></div>
   <p class="noprint"><i>Enter code in the yellow areas. F2: submit code. PgDn/PgUp: next/prev blank. Tab: reindent.</i></p>
   <textarea id="code" name="code"></textarea>
   <script type='text/javascript'>
    if (window.location.hash) {
      var ex = window.location.hash.substring(1);
    }
    else {
      var ex = sheets[0];
    }
    $('#selectSheet').val(ex);
    loadProblem(ex);
   </script>
   <button class="noprint" id="submitButton" onClick="checkSolution()">Submit code</button>
   <p class="noprint">Results will appear below.</p>
   <div class="noprint" id="results"></div>
   </div>
</div>
</body>
</html>