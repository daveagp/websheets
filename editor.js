var editor_schema = 
  [{key: 'description', type:'codemirror', mode:'html', label:'Description', howto: 'html markup<br>shown to student'},
   {key: 'epilogue', type: 'codemirror', mode:'html', optional: true, label: 'Epilogue', howto: 'html markup<br>shown when solved'},
   {key: 'lang', type: 'choice', label: 'Engine', 
    choices: [["", "Select one..."], ["Java", "Java"], ["C++", "C++ (call main with stdin and args)"],
              ["C++func", "C++ (call functions directly)"], ['multichoice', "Multiple true/false"],
              ["shortanswer", "Short answer"]]},
   {key: 'choices', lang: 'multichoice', type: 'codemirror', mode:'json', label: 'Choices',
    howto: 'json list of string, bool pairs<br>e.g. <tt>[["good", True],<br>["bad", False]]'},
   {key: 'answer', lang: 'shortanswer', type: 'string', label: 'Correct Answer'},
   {key: 'source_code', lang: 'Java', type: 'codemirror', mode:'java', label: 'Template / Reference Solution'},
   {key: 'source_code', langs: ['C++', 'C++func'], type: 'codemirror', mode:'c++', label: 'Template / Reference Solution'},
   {key: 'tests', lang: 'Java', type: 'codemirror', mode:'java', label: 'Java test suite'},
   {key: 'tests', langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'C++ test suite'},
   {key: 'verboten', optional: true, langs: ['Java', 'C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Forbidden Substrings',
    howto:'json list of strings<br>e.g. <tt>["for","while"]</tt>'},
   {key: 'attempts_until_ref', optional: true, type: 'choice', label: 'Solution Visibility', howto:'default: when problem is completed',
    choices: [["infinity", "When problem is completed"], ["0", "Always"],
              ["1", "After 1 incorrect attempt"], ["2", "After 2 incorrect attempts"],
              ["3", "After 3 incorrect attempts"], ["4", "After 4 incorrect attempts"],
              ["5", "After 5 incorrect attempts"], ["never", "Never"]]},

   {key: 'imports', optional: true, lang: 'Java', type: 'codemirror', mode:'json', label: 'Java imports',
    howto: 'json list of importables<br>e.g. <tt>["java.util.*"]</tt>'},
   {key: 'classname', optional: true, lang: 'Java', type: 'string', label: 'Override Java classname',
    howto: 'else defaults to<br>websheet name'},
   {key: 'hide_class_decl', optional: true, lang: 'Java', type: 'boolean', label: 'Hide <tt>class ClassName {</tt>',
    howto: 'default is False'},
   {key: 'dependencies', optional: true, lang: 'Java', type: 'codemirror', mode:'json', label: 'Dependent on other websheets?',
    howto: 'json list of websheet names in this folder<br>e.g. <tt>["DataStructure"]</tt>'},

   {key: 'example', optional: true, langs: ['C++', 'C++func'], type: 'boolean', label: 'Is Example?',
    howto: '(i.e., demo, not exercise)'},
   {key: 'cppflags_add', optional: true, langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Compiler flags to add?',
    howto: 'json list of flags<br>e.g. <tt>["-Wno-unused-variable"]</tt>'},
   {key: 'cppflags_remove', optional: true, langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Compiler flags to remove?', howto: 'json list of flags<br>see <a href="https://github.com/daveagp/websheets/blob/master/grade_cpp.py">default_cppflags</a><br>e.g. <tt>["-Wno-write-strings"]</tt>'},
   {key: 'cppflags_replace', optional: true, langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Use custom list of compiler flags?', howto:'json list of flags<br>overrides all other compiler option settings<br>e.g. <tt>["-Wpedantic"]</tt>'}
  ];

var codemirrors = {};

// inelegant since jquery's .append doesn't pass items to MutationObserver one by one
   var process = function (parent, child) {
     $(child).find('div.cm-maker').each(function() {
       if (!$(this).hasClass('cm-maker')) return;
       $(this).removeClass('cm-maker');
       var modemap = {'html':'text/html','json':'application/json','c++':'text/x-c++src','java':'text/x-java'};
       var modetag = $(this).attr('data-mode');
       var row = $(this).closest('tr').attr('id').substring(4); // row-
       if (!modemap[modetag])
         alert("Don't know mode " + modetag);
       codemirrors[row] = CodeMirror(this, {
         mode: modemap[modetag],
         theme: "neat", tabSize: 3, indentUnit: 3,
         lineNumbers: true,
         styleSelectedText: true,
         viewportMargin: Infinity,
         matchBrackets: true
       });
     })};

   // construct observer _before_ anything is rendered
   new MutationObserver(
      // constructor argument: callback on MutationRecord[]
      function (events) {
         // for each record,
         for (var i=0; i<events.length; i++)
            // MutationRecord has Node "target" and Node[] "addedNodes"
            for (var j=0; j<events[i].addedNodes.length; j++)
               // we'll define "process(parent, child)" below
               process(events[i].target, events[i].addedNodes[j]);
      }
   ).observe(document, {childList: true, subtree: true});


$(function() {
  var widget = function(item) {
    if (item.type == 'choice') {
      var result = '<select>';
      for (var i=0; i<item.choices.length; i++)
        result += '<option value="' + item.choices[i][0] + '">' + item.choices[i][1] + '</option>';
      result += '</select>';
      return result;
    }
    if (item.type == 'boolean') {
      return widget({type:'choice', choices:[['false','false'],['true','true']]});
    }
    if (item.type == 'string') {
      return '<input type="text"></input>';
    }
    if (item.type == 'codemirror') {
      return '<div class="cm-maker" data-mode="'+item.mode+'"></div>';
    }
  }

  for (var i=0; i<editor_schema.length; i++) {
    var item = editor_schema[i];
    var row = '<tr id="row-'+i+'" class="row-'+item.key+'"><td>'+item.label;
    if (item.howto) row += '<div class="howto">'+item.howto+'</div>';
    row += '</td><td>';
    row += widget(item);
    if (item.optional) row += ' <a href="#" class="optout" data-row="'+i+'">remove</a>';
    row += '</td></tr>';
    $('table#editor').append(row);
  }

  var update_rows = function() {
    var lang = $('.row-lang select').val();
    $('#optionals').html('');
    for (var i=0; i<editor_schema.length; i++) {
      var item = editor_schema[i];
      if (item.lang && lang != item.lang 
          || item.langs && item.langs.indexOf(lang) == -1)
        $('#row-'+i).addClass('wronglang');
      else {
        $('#row-'+i).removeClass('wronglang');
        if (item.optional) {
          $('#row-'+i).addClass('optedout');
          $('#optionals').append(' <button data-row="'+i+'" class="optin">'+item.label+'</button>');
        }
        else
          if (codemirrors[""+i]) codemirrors[""+i].refresh();
      }
    };
  };

  $('body').on('click', '.optin', function(event) {
    var index = $(event.target).attr('data-row');
    $('#row-'+index).show(400);
    if (codemirrors[""+index]) codemirrors[""+index].refresh();
    $('#row-'+index).removeClass('optedout');
    $(event.target).hide(400);
    return false;
  });

  $('body').on('click', '.optout', function(event) {
    var index = $(event.target).attr('data-row');
    $('#row-'+index).hide(400);
    $('#row-'+index).addClass('optedout');
    $('.optin[data-row="'+index+'"]').show(400);
    return false;
  });

  $('.row-lang select').on('change', update_rows);
  update_rows();

});

