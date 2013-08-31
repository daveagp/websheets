<html>
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
   <script type="text/javascript">
   $(function() { 
       resetup( <?php echo passthru("./Websheet.py get_html_template MaxThree"); ?> ); 
     });
   </script>

</head>
<body>
   Select a problem: <select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val());">
   <option value="MaxThree">MaxThree</option>
   <option value="FourSwap">FourSwap</option>
   <option value="NextYear">NextYear</option>
   </select>
   <h3>Exercise Description</h3>
   <div id="description"></div>
   <p><i>Enter code in the yellow areas. F8: submit code. Tab/Shift-Tab: next/prev blank.</i></p>
   <textarea id="code" name="code"></textarea>
   <button id="submitButton" onClick="checkSolution()">Submit code</button>
   <p>Results will appear below.</p>
   <div id="results"></div>
</body>
</html>