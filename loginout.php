<?php
include_once('auth.php');
?><html>
<head>
   <title>Websheets</title>
   <link rel="icon" type="image/png" href="favicon.png">
</head>

<body>
<?php 
global $WS_AUTHINFO;
if ($WS_AUTHINFO['logged_in'])
   echo "You are now logged in as <tt>".$WS_AUTHINFO['username']."</tt>.";
  else
    echo "You are now logged out.";

echo "<br>You can now close this tab/window.";
?>
</body>
