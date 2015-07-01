<?php
include_once('auth.php');
global $WS_AUTHINFO;
?><html>
<head>
   <title>Websheets</title>
   <link rel="icon" type="image/png" href="favicon.png">
    <script type='text/javascript'>
    window.authinfo = <?php echo json_encode($WS_AUTHINFO).';' ?>;
    window.loginout_loaded = true;
</script>
</head>

<body>
<?php 
if ($WS_AUTHINFO['logged_in'])
   echo "You are now logged in as <tt>".$WS_AUTHINFO['username']."</tt>.";
  else
    echo "You are now logged out.";

echo "<br>You can now close this tab/window.";
?>
</body>
