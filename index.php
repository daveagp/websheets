<?php
include_once('auth.php');
?><html>
<head>
   <title>Websheets</title>
   <link rel="icon" type="image/png" href="favicon.png">
   <script type="text/javascript" src="jquery.min.js"></script>
   <script type="text/javascript" src="CodeMirror/lib/codemirror.js"></script>
   <script type="text/javascript" src="CodeMirror/mode/clike/clike.js"></script>
   <script type="text/javascript"
    src="CodeMirror/addon/selection/mark-selection.js"></script>
   <script type="text/javascript" 
    src="CodeMirror/addon/edit/matchbrackets.js"></script>
   <script type="text/javascript">
   "use strict";
   </script>
   <script type="text/javascript" src="websheets.js"></script>
   <script type="text/javascript" src="index.js"></script>
   <script type="text/x-mathjax-config"> 
      MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]} });
   </script>
   <script type="text/javascript" 
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
   </script>

   <link rel="stylesheet" href="CodeMirror/lib/codemirror.css">
   <link rel="stylesheet" href="CodeMirror/theme/neat.css">
   <link rel="stylesheet" href="websheets.css">
   <link rel="stylesheet" href="index.css">
  
   <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700'
    rel='stylesheet' type='text/css'>
<script type='text/javascript'> 
   websheets.authinfo = <?php echo json_encode($GLOBALS['WS_AUTHINFO']); ?>;
   websheets.urlbase = "./";
   websheets.require_login = true;
   websheets.sheets = 
      <?php
      if (!array_key_exists('group', $_GET)) 
         echo passthru("./Websheet.py list") . ";\n";
      else {
         $g = $_GET['group'];
         if (1 != preg_match('~^([\w-]+(/| ))*[\w-]+$~', $g))
            echo "['hello']; alert('Bad group');";
         else echo passthru("./Websheet.py list $g") . ";";
      }
   echo " websheets.subfolders = ";
      $g = "";
      if (array_key_exists('group', $_GET)) $g = $_GET['group']; 
      echo passthru("./Websheet.py list-folders $g") . ";\n";
?>
   </script>
</head>
<body>
 <div id="page">
  <div class="menu-bar noprint">

<!--    <p>
    This is an experimental system. 
    <a href="mailto:daveagp@gmail.com">Contact us</a> 
    if you find bugs or have feedback.     
    <a href="bytopic.php">See all problems by topic.</a>
    Visit the <a href="https://github.com/daveagp/websheets">source code</a> 
    on GitHub. -->
    
    <p>
    <span>
    Select an exercise:
    <select name="selectSheet" id="selectSheet">
    </select>
    </span>
    <span id="subfoldering" style='margin-left:30px; display: none;'>
    Change group?
    <select name="selectSubfolder" id="selectSubfolder">
    </select>
    <button name="enterSubfolder" id="enterSubfolder">
    Change
    </button>
    </span>
    
  </div> <!-- menu-bar -->

  <div id="container">
  </div>

 </div> <!-- page -->
</body>
</html>
