<?php
include_once('../CAS-1.3.2/CAS.php');
phpCAS::setDebug();
phpCAS::client(CAS_VERSION_2_0,'fed.princeton.edu',443,'cas');
phpCAS::setNoCasServerValidation();
phpCAS::forceAuthentication();
if (isset($_REQUEST['logout'])) {
  phpCAS::logout();
}
?><html>
<head>
   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
   <script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
   <script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
   <script type="text/javascript" src="CodeMirror/addon/selection/mark-selection.js"></script>
   <script type="text/javascript" src="websheet.js"></script>

   <link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
   <link rel="stylesheet" href="CodeMirror/theme/neat.css">
   <link rel="stylesheet" href="websheet.css">
  
   <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700' rel='stylesheet' type='text/css'>

   <script type="text/javascript" src="test.js"></script>

</head>
<body>
   <p>Logged in as <b><?php echo phpCAS::getUser(); ?></b>.
   Click to <a href="?logout=">log out</a>.</p>
   Select a problem: <select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val())">
   </select>
   <script type='text/javascript'>
   populateSheets(<?php echo passthru("./Websheet.py list") ?> );
   </script>
   <div id="container" style="display:none">
   <h3>Exercise Description</h3>
   <div id="description"></div>
   <p><i>Enter code in the yellow areas. F8: submit code. Tab/Shift-Tab: next/prev blank.</i></p>
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
</body>
</html>