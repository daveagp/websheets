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

   <script type="text/javascript" src="test.js"></script>
<script type="text/javascript">
   $(function() { resetup( <?php echo passthru("./Websheet.py get_html_template ws_MaxThree"); ?> ); });
</script>

</head>
<body>
   <select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val());">
   <option value="ws_MaxThree">MaxThree</option>
   <option value="ws_FourSwap">FourSwap</option>
   <option value="ws_NextYear">NextYear</option>
   </select>
   <h3>Problem statement</h3>
   <div id="description"></div>
   <p><i>User interface hint:</i> use the Tab key as a shortcut to jump from one blank to the next.</p>
   <textarea id="code" name="code"></textarea>
   <button id="submitButton" onClick="checkSolution()">Submit code</button>
   <p>Results will appear below.</p>
   <div id="results"></div>
</body>
</html>