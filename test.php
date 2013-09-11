<?php
include_once('include.php');
?><html>
<head>
   <title>Websheets</title>
   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
   <script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
   <script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
   <script type="text/javascript" src="CodeMirror/addon/selection/mark-selection.js"></script>
   <script type="text/javascript" src="CodeMirror/addon/edit/matchbrackets.js"></script>
   <script type="text/javascript" src="websheet.js"></script>

   <link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
   <link rel="stylesheet" href="CodeMirror/theme/neat.css">
   <link rel="stylesheet" href="websheet.css">
  
   <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700' rel='stylesheet' type='text/css'>

   <script type="text/javascript" src="test.js"></script>

</head>
<body>
<div id="page">
<?php if (WS_LOGGED_IN) {
   echo "<p>Logged in as <b>" . WS_USERNAME . "</b>. " .
   "Click to <a href='" . WS_LOGOUT_LINK . "'>log out</a>.</p>";
} ?>
   <p>This is an experimental system. <a href="mailto:dp6@cs.princeton.edu">Contact us</a>
    if you find bugs, typos, user interface issues, inaccurate grading or anything else.</p>
   Select a problem: <select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val())">
   </select>
   <script type='text/javascript'>
   populateSheets(<?php
       if (array_key_exists("group", $_REQUEST))
	 echo json_encode(explode(" ", $_REQUEST["group"]));
       else
	 echo passthru("./Websheet.py list") 
	   ?> );
   </script>
   <div id="container" style="display:none">
   <h3>Exercise Description</h3>
   <div id="description"></div>
   <p><i>Enter code in the yellow areas. F2: submit code. PgDn/PgUp: next/prev blank. Tab: reindent.</i></p>
   <textarea id="code" name="code"></textarea>
   <script type='text/javascript'>
    if (window.location.hash) {
      var ex = window.location.hash.substring(1);
    }
    else {
      var ex = "SquareOf";
    }
    $('#selectSheet').val(ex);
    loadProblem(ex);
   </script>
   <button id="submitButton" onClick="checkSolution()">Submit code</button>
   <p>Results will appear below.</p>
   <div id="results"></div>
   </div>
</div>
</body>
</html>