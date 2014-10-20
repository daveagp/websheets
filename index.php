<?php
include_once('include.php');
?><html>
<head>
   <title>Websheets</title>
   <link rel="icon" type="image/png" href="favicon.png">
   <script type="text/javascript" 
    src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
   <script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
   <script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
   <script type="text/javascript"
    src="CodeMirror/addon/selection/mark-selection.js"></script>
   <script type="text/javascript" 
    src="CodeMirror/addon/edit/matchbrackets.js"></script>
   <script type="text/javascript" src="websheet.js?4"></script>
   <script type="text/x-mathjax-config"> 
      MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]} });
   </script>
   <script type="text/javascript" 
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
   </script>

   <link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
   <link rel="stylesheet" href="CodeMirror/theme/neat.css">
   <link rel="stylesheet" href="websheet.css?8">
  
   <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700'
    rel='stylesheet' type='text/css'>

   <script type="text/javascript" src="index.js?7"></script>

<!-- start of php interactions -->
   <script type='text/javascript'>
     <?php if (!WS_LOGGED_IN) { ?>
           $(function(){window.setTimeout(function(){
 alert('None of your work will be saved until you log in (see links at top).');
           }, 1000 ); });
     <?php }; ?>

     // pass variables to be used by index.js
     var GET = <?php echo json_encode($_GET); ?>;
     var sheets = 
  <?php
       if (array_key_exists("group", $_GET))
         echo "GET['group'].split(' ')";
       else
	 echo passthru("./Websheet.py list");
   ?>;
   </script>
</head>
<body>
 <div id="page">
  <div class="menu-bar noprint">
    <?php 
if (WS_CONFIG_ERROR_DIV) {
  echo WS_CONFIG_ERROR_DIV;
}
if (WS_LOGGED_IN) { ?>
  <p>Logged in as <b><?php echo WS_USERNAME;?></b> 
    (logged in through <?php echo WS_AUTHDOMAIN;?>)
   Click to <a href="javascript:auth('logout')">log out</a>.
<?php 
} else { 
?>
 <p><b style="color:red">Not logged in, your work will not be saved.</b>
    Log in with:
 <?php foreach (explode(" ", WS_PROVIDERS) as $authprovider) 
    echo <<<EOT
     <a href="javascript:auth('$authprovider')">$authprovider</a> 
EOT;
 } // else
?>
<!-- end of php interactions -->

    <p>
    This is an experimental system. 
    <a href="mailto:daveagp@gmail.com">Contact us</a> 
    if you find bugs or have feedback.     
    <a href="bytopic.php">See all problems by topic.</a>
    Visit the <a href="https://github.com/daveagp/websheets">source code</a> 
    on GitHub.
    
    <p>
    Select a problem: 
    <select name="selectSheet" id="selectSheet" 
       onChange="loadProblem($('#selectSheet').val())">
    </select>
    <button id='resetButton'>Start over</button>
    <button id='answerButton'>View reference solution</button>
    
  </div> <!-- menu-bar -->

  <div id="container" style="display:none">
   <div class='exercise-header'>Exercise Description</div>
   <div id="description"></div>
   <p class="noprint">
     <i>Enter code in the yellow areas. F2: submit code. 
     PgDn/PgUp: next/prev blank. Tab: reindent.</i>
   </p>
   <textarea id="code" name="code"></textarea>
   <button class="noprint" id="submitButton" onClick="checkSolution()">
     Submit code
   </button>
   <p class="noprint">Results will appear below.</p>
   <div class="noprint" id="results"></div>
   <div class="noprint" id="after-results" style="display:none"></div>
  </div> <!-- container -->
  <div id="errcontainer" style="display:none">
  </div>
 </div> <!-- page -->
</body>
</html>
