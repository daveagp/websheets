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

   <script type="text/javascript">
   resetup = function(data) {
       hhandle = null;
       window.testWS.cm.toTextArea();
       window.testWS = websheet("code", data );
       window.testWS.cm.on("change", function() {
                             if (hhandle != null) testWS.cm.removeLineClass(hhandle, "wrapper", "red");
                             hhandle = null;
                           });
   }

   $(function() {
       window.testWS = websheet("code", <?php echo passthru("./Websheet.py get_json_template ws_MaxThree"); ?> );
       window.testWS.cm.on("change", function() {
                             if (hhandle != null) testWS.cm.removeLineClass(hhandle, "wrapper", "red");
                             hhandle = null;
                           });
     });

       loadProblem = function(slug) {
         $.ajax("Websheet.php",
                {data: {args: "get_json_template "+$("#selectSheet").val(), 
                    stdin: ""},
                success: function(data) {
                  if (data.substring(0, 1) != '[') // not json array -- so an error
                    alert(data);
                  else {
                    resetup(JSON.parse(data));
                  }
                  }});
       };
                

var hhandle = null;

   checkSolution = function() {
     var user_state = JSON.stringify(testWS.getUserCodeAndLocations());
     $.ajax("check.php",
            {
            data: {user_state: user_state, module: $('#selectSheet').val()},
                dataType: "text",
                success: function(data) {
                if (data.substring(0, 1) != '[') // not json array -- so an error
                  $("#results").html(data);
                else {
                  var result = JSON.parse(data);
                  if (result[0]) {
                    $("#results").html("Passes basic grammar tests and produces:\n" + result[1]);
                  }
                  else {
                    $("#results").html(result[1]);
                    var line = result[1];
                    line = line.substr(result[1].indexOf("line ")+5);
                    var x = 0;
                    while (line.charAt(x) >= '0' && line.charAt(x) <= '9') x++;
                    var line = parseInt(line.substr(0, x))-1;
                    hhandle = testWS.cm.addLineClass(line, "wrapper", "red");
                  }
                }
                  }
            });
   };
   </script>
</head>
<body>
<select name="selectSheet" id="selectSheet" onChange="loadProblem($('#selectSheet').val());">
<option value="ws_MaxThree">MaxThree</option>
<option value="ws_FourSwap">FourSwap</option>
<option value="ws_NextYear">NextYear</option>
</select>
<p>Use the Tab key as a shortcut to jump from one blank to the next.</p>
<textarea id="code" name="code"></textarea>
<button onClick="checkSolution()">Submit code</button>
<p>Results of the basic syntax check will appear below.</p>
<pre id="results"></pre>
</body>
</html>