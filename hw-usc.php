<?php
if (!array_key_exists('course', $_GET)) {
   echo "No course selected.";
   die();
}

require_once("auth.php");

$course = $_GET["course"];

if (!preg_match("@^[0-9a-zA-Z_-]+$@", $course)) {
   echo "Error, malformed course";
   die();
}

$path = "/home/parallel05/courseware/courses/$course/info.json";

$courseinfo = json_decode(file_get_contents($path), true);

if (!in_array($WS_AUTHINFO["username"], $courseinfo["staff"])) {
   echo "Please <a href='?course=$course&auth=Google'>log in</a> as course staff.";
   die();
}

passthru("./hw-usc.py $course");
