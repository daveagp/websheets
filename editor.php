<html>
<head>
<style>
.howto {font-size: 75%;}
</style>
</head>
<body>
<table>
<tr><th>Property</th><th>Value</th></tr>
<tr data-key='description' data-type='codemirror' data-mode='html' data-label='Description'>
  <td><div class='howto'>html markup<br>shown to student</div></td></tr>
<tr data-key='epilogue' data-type='codemirror' data-mode='html' data-optional data-label='Epilogue'>
  <td><div class='howto'>html markup<br>shown when solved</div></td></tr>
<tr data-key='lang' data-type='choice' data-label='Engine'><td></td>
   <td><select><option value='' selected>Select one...<option value='Java'>Java<option value='C++'>C++ (main, argv, stdin) 
   <option value='C++func'>C++ (call functions)<option value='multichoice'>Multiple true/false
   <option value='shortanswer'>Short answer</select></td></tr>
<tr data-key='choices' data-lang='multichoice' data-type='codemirror' data-mode='json' data-label='Choices'><td>
   <div class='howto'>json list of string, bool pairs<br>e.g. <tt>[["good", True],<br>["bad", False]]</div></td></tr>
<tr data-key='answer' data-lang='shortanswer' data-type='string' data-label='Correct Answer'><td></td></tr>
<tr data-key='source_code' data-lang='iscode' data-type='codemirror' data-mode='java' data-label='Template / Reference Solution'><td></td></tr>
<tr data-key='tests' data-lang='Java' data-type='codemirror' data-mode='java' data-label='Java test suite'><td></td></tr>
<tr data-key='tests' data-lang='C++ C++func' data-type='codemirror' data-mode='json' data-label='C++ test suite'></td></tr>
<tr data-key='verboten' data-optional data-lang='iscode' data-type='codemirror' data-mode='json' data-label='Forbidden Substrings'>
   <td><div class='howto'>json list of strings<br>e.g. <tt>["for","while"]</tt></td></tr>
<tr data-key='attempts_until_ref' data-type='choice' data-label='Allow Viewing Solution'></td>
   <td><select><option value='infinity' selected>When problem is completed<option value='0'>Always
   <option value='1'>After 1 incorrect attempt<option value='2'>After 2 incorrect attempts
   <option value='3'>After 3 incorrect attempts<option value='4'>After 4 incorrect attempts
   <option value='5'>After 5 incorrect attempts<option value='-1'>Never</select></td>

<tr data-key='imports' data-optional data-lang='Java' data-type='codemirror' data-mode='json' data-label='Java imports'>
   <td><div class='howto'>json list of importables
   <br>e.g. <tt>["java.util.*"]</tt></td></tr>
<tr data-key='classname' data-optional data-lang='Java' data-type='string' data-label='Override Java classname'><td>
   <div class='howto'>else defaults to<br>websheet name</td></tr>
<tr data-key='hide_class_decl' data-optional data-lang='Java' data-type='boolean' data-label='Hide <tt>class ClassName {</tt>'><td>
   <div class='howto'>default is False</td></tr>
<tr data-key='dependencies' data-optional data-lang='Java' data-type='codemirror' data-mode='json' data-label='Dependent on other websheets?'><tr><div class='howto'>json list of websheet names in this folder
   <br>e.g. <tt>["DataStructure"]</tt></td></tr>

<tr data-key='example' data-optional data-lang='C++ C++func' data-type='boolean' data-label='Just an example?'><td><div class='howto'>(e.g., demo, not exercise)</td></tr>
<tr data-key='cppflags_add' data-optional data-lang='C++ C++func' data-type='codemirror' data-mode='json' data-label='Compiler flags to add?'><td><div class='howto'>json list of flags
   <br>e.g. <tt>["-Wno-unused-variable"]</tt></div></td></tr>
<tr data-key='cppflags_remove' data-optional data-lang='C++ C++func' data-type='codemirror' data-mode='json' data-label='Compiler flags to remove?'><td><div class='howto'>json list of flags
   <br>DEFAULT LIST IS HERE
   <br>e.g. <tt>["-Wno-write-strings"]</tt></div></td></tr>
<tr data-key='cppflags_replace' data-optional data-lang='C++ C++func' data-type='codemirror' data-mode='json' data-label='Use custom list of compiler flags?'><td><div class='howto'>json list of flags
   <br>overrides all other compiler option settings
   <br>e.g. <tt>["-Wpedantic"]</tt></div></td></tr>
</table>
Add these optional properties?
</body>
</html>