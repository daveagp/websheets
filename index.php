<?php

echo "foo";
echo `./parse.py`;
passthru('./parse.py');
popen('./parse.py', 'r');
echo exec("./parse.py");
echo "bar";
pcntl_exec("./parse.py");
echo "baz";

?>