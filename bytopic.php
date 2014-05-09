<html>
<head>
<title>Websheets examples</title>
</head>
<body>
Here is a list of example exercises for the <a href="index.php">Websheets</a>
programming practice tool, grouped by topic.
   
<p>References to chapters within exercises mean the book <a href="http://introcs.cs.princeton.edu/java/home/">Introduction to Programming in Java: An Interdisciplinary Approach</a> by Sedgewick and Wayne. 

<p>
<?php

$categories = <<<EOT
[
 ["Intro and Cmd Line Args", 
  ["HelloWorld", "NameAge", "NextYear", "SquareOf", "SquareSwap"]],
 ["Data Types",
  ["Eggsactly", "PercentScore", "PizzaCalculator", "WindChill", "Distance", "ThreeSort"]],
 ["Loops and Conditionals",
  ["Flag", "AgeChecker", "SquareCensus", "Quadratic", "ModularSqrt"]],
 ["Arrays",
  ["Distinct", "Reverse", "NOrdered", "NSwap", "Commonest", "Students"]],
 ["StdIn",
  ["MaxMin", "Powers", "Squish", "Means"]],
 ["Static Methods",
  ["Positive", "Find", "Boxed", "Summer", "Yarra"]],
 ["Practice Midterm Exams",
  ["HatsPart1", "HatsPart2", "FoodPart1", "FoodPart2", 
   "SnowStats", "SnowMelt"]],
 ["Recursion",
  ["Kettles", "Factorial", "TextFractal", "BinarySum", "Evaluate", "ZeroSum"]],
 ["Dynamic Programming",
  ["Catalan", "PartitionCount", "Mario", "Knapsack", "KnapsackBacktrack"]],
 ["Binary Search",
  ["Lambert"]],
 ["Using Objects",
  ["FourChargeClient", "IsPalindrome", "ComplementaryDNA", 
   "CircularShift", "GeneFind"]],
 ["Creating Objects",
  ["Recorder", "Clicker", "CountingSort", "CombinationLock", "Monomial",
   "Name", "Interval", "Vector"]],
 ["Stacks, Queues, and Symbol Tables",
  ["QMerge", "LineEdit", "FrequencyTable", "ReverseLookup", "CME"]],
 ["Linked Lists",
  ["MonkeyTraverse", "MonkeyAddStart", "MonkeyAddEnd", "LinkIt",
   "Quote", "CircularQuote"]],
 ["Regular Expressions",
  ["RegularExercise"]],
 ["Practice Final Exams",
  ["BinaryInteger", "Person", "TigerBook", "MiniPro", "MiniPro2"]],
 ["Threads",
  ["SumParallel", "FTPLimiter", "FJSort"]]
]
EOT;

$categories = json_decode($categories, true);

$categorized_exercises = array();

echo "<table>";
foreach ($categories as $category) {
  $topic = $category[0];
  echo "<tr><th>$topic</th><td> ";
  $group = implode($category[1], '+');
  foreach ($category[1] as $slug) {
    echo "<a href='index.php?group=$group#$slug'>$slug</a> ";
    $categorized_exercises[$slug] = true;
  }
  echo "</td></tr>";
}
echo "</table>";

// do some sanity checking to make sure topics list matches known exercises

$filesystem_exercises = array();
foreach (scandir("./exercises") as $filename) {
  $bits = explode('.', $filename);
  if (count($bits)==2 && $bits[1]=='py')
    $filesystem_exercises[$bits[0]] = true;
}

foreach ($filesystem_exercises as $f_ex => $whatevs)
  if (!array_key_exists($f_ex, $categorized_exercises))
    echo "<br>Warning: $f_ex in filesystem with no category";
foreach ($categorized_exercises as $c_ex => $whatevs)
  if (!array_key_exists($c_ex, $filesystem_exercises))
    echo "<br>Warning: $c_ex in categories with no file";

?>

<p>
You can also view the <a href="https://github.com/daveagp/websheets">Websheets source code</a>.
</body>


