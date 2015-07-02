var editor_schema = 
  [{key: 'description', type:'codemirror', mode:'html', label:'Description', howto: 'html markup<br>shown to student'},
   {key: 'epilogue', type: 'codemirror', mode:'html', optional: true, label: 'Epilogue', howto: 'html markup<br>shown when solved'},
   {key: 'sharing', type: 'choice', default: 'open-nosol', optional: true, label: 'Public permissions',
    choices: [["open", "open: anyone can solve, see in listings, see source"],
              ["open-nosol", "open: open, but when viewing source, redact solution"],
              ["visible", "closed-source, but list publicly and anyone can attempt it"],
              ["hidden", "closed-source, and hide from listings (need direct URL to attempt)"],
              ["draft", "draft: don't let anyone other than me see this at all"]]},
   {key: 'remarks', type: 'codemirror', optional: true, label: 'Remarks', mode:'html', 
    howto: 'Comments, history, license, etc.'},

   {key: 'lang', type: 'choice', label: 'Engine', default: '', 
    choices: [["", "Select one..."], ["Java", "Java"], ["C++", "C++ (call main with stdin and args)"],
              ["C++func", "C++ (call functions directly)"], ['multichoice', "Multiple true/false"],
              ["shortanswer", "Short answer"]]},
   {key: 'choices', lang: 'multichoice', type: 'codemirror', mode:'json', label: 'Choices',
    howto: 'json list of string, bool pairs<br>e.g. <tt>[["good", True],<br>["bad", False]]'},
   {key: 'answer', lang: 'shortanswer', type: 'string', label: 'Correct answer'},
   {key: 'source_code', lang: 'Java', type: 'codemirror', mode:'java', label: 'Template / Reference solution'},
   {key: 'source_code', langs: ['C++', 'C++func'], type: 'codemirror', mode:'c++', label: 'Template / Reference solution'},
   {key: 'tests', lang: 'Java', type: 'codemirror', mode:'java', label: 'Java test suite'},
   {key: 'tests', lang: 'C++', type: 'codemirror', mode:'json', label: 'C++ test suite',
    howto: 'json list of stdin/args tests<br>e.g. <tt>[{"stdin":"hi", "args":["4", "5"]},<br>{"stdin":"noargs"}]</tt><br>to just run once with no input use <tt>[{}]</tt>'},
   {key: 'tests', lang: 'C++func', type: 'codemirror', mode:'json', label: 'C++ test suite', howto:'TODO'},
   {key: 'verboten', optional: true, langs: ['Java', 'C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Forbidden substrings',
    howto:'json list of strings<br>e.g. <tt>["for","while"]</tt>'},
   {key: 'attempts_until_ref', langs: ['Java', 'C++', 'C++func'], default: 'infinity', optional: true, type: 'choice', label: 'Solution visibility', 
    choices: [["0", "Always"],
              ["1", "After 1 attempt"], ["2", "After solving or 2 attempts"],
              ["3", "After solving or 3 attempts"], ["4", "After solving or 4 attempts"],
              ["5", "After solving or 5 attempts"], 
              ["infinity", "After solving"], 
              ["never", "Never"]]},

   {key: 'imports', optional: true, lang: 'Java', type: 'codemirror', mode:'json', label: 'Java imports',
    howto: 'json list of importables<br>e.g. <tt>["java.util.*"]</tt>'},
   {key: 'classname', optional: true, lang: 'Java', type: 'string', label: 'Override Java classname',
    howto: 'else defaults to<br>websheet name'},
   {key: 'dependencies', optional: true, lang: 'Java', type: 'codemirror', mode:'json', label: 'Dependent on other websheets?',
    howto: 'json list of websheet names in this folder<br>e.g. <tt>["DataStructure"]</tt>'},

   {key: 'example', optional: true, langs: ['C++', 'C++func'], type: 'choice', label: 'Is example?',
    choices: [['False', 'False'], ['True', 'True']], default: 'False',
    howto: 'i.e., just a demo<br><a href="javascript:explain_example()">can still be <tt>\\[editable]\\</tt></a>'},
   {key: 'cppflags_add', optional: true, langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Add compiler flag(s)',
    howto: 'json list of flags<br>e.g. <tt>["-Wno-unused-variable"]</tt>'},
   {key: 'cppflags_remove', optional: true, langs: ['C++', 'C++func'], type: 'codemirror', mode:'json', label: 'Remove default compiler flag(s)', howto: 'json list of flags<br>see <a href="https://github.com/daveagp/websheets/blob/master/grade_cpp.py">default_cppflags</a><br>e.g. <tt>["-Wno-write-strings"]</tt>'}
  ];
var explain_example = function() {
  alert("This could be a sandbox or something to kick off discussion. In the cpp folder, see scratch, arrays/arraybad, var-expr/optest for instance. This also is appropriate if it simply can't be autograded due to randomness or timeouts, see random/randdigits and streams/buffer.");
}

var codemirrors = {};

$(function() {
  if (websheets.editor_readonly) {
    $('body').addClass('readonly');
    $('#doing').html('Viewing');
  }

  var widget = function(item) {
    if (item.type == 'choice') {
      var result = '<select>';
      for (var i=0; i<item.choices.length; i++)
        result += '<option value="' + item.choices[i][0] + '" '
        +(item.choices[i][0]==item.default?'selected':'')
        +'>' + item.choices[i][1] 
        +(item.choices[i][0]==item.default?' (default)':'')
        +'</option>';
      result += '</select>';
      return result;
    }
    if (item.type == 'string') {
      return '<input type="text"></input>';
    }
    if (item.type == 'codemirror') {
      return '<div class="cm-maker"></div>';
    }
  }

  for (var i=0; i<editor_schema.length; i++) {
    var item = editor_schema[i];
    var row = '<tr id="row-'+i+'" class="rowlabel row-'+item.key+'"><td>'+item.label;
    if (item.howto) row += '<div class="howto">'+item.howto+'</div>';
    row += '</td><td class="widget">';
    row += widget(item);
    if (item.optional) row += ' <a href="#" class="optout hide-readonly" data-row="'+i+'">remove</a>';
    row += '</td></tr>';
    
    // force rendering as DOM element so codemirror can access it immediately
    row = $.parseHTML(row)[0];
    $('table#editor').append(row); 

    if (item.type == 'codemirror') {
      var modemap = {'html':'text/html','json':'application/json','c++':'text/x-c++src','java':'text/x-java'};
      var modetag = item.mode;
      if (!modemap[modetag])
        alert("Don't know mode " + modetag);
      codemirrors[i] = CodeMirror(row.children[1].firstChild, {
        mode: modemap[modetag],
        theme: "neat", tabSize: 3, indentUnit: 3,
        //         lineNumbers: true,
        styleSelectedText: true,
        viewportMargin: Infinity,
        matchBrackets: true,
        readOnly: websheets.editor_readonly === true
      });
    }
  }

  var update_rows = function() {
    var lang = $('.row-lang select').val();
    $('#optionals').html('');
    for (var i=0; i<editor_schema.length; i++) {
      var item = editor_schema[i];
      if (item.lang && lang != item.lang 
          || item.langs && item.langs.indexOf(lang) == -1)
        $('#row-'+i).hide();
      else {
        $('#row-'+i).show();
        if (item.optional) {
          $('#row-'+i).hide();
          $('#optionals').append(' <button data-row="'+i+'" class="optin">'+item.label+'</button>');
        }
        else
          if (codemirrors[""+i]) codemirrors[""+i].refresh();
      }
    };
  };

  window.optin = function(index, time) {
    if (time === undefined) time = 400;
    $('#row-'+index).show(time);
    if (codemirrors[""+index]) codemirrors[""+index].refresh();
    $('.optin[data-row="'+index+'"]').hide(time);
    if (codemirrors[""+i]) codemirrors[""+i].refresh();
  };

  $('body').on('click', '.optin', function(event) {    
    var index = $(event.target).attr('data-row');
    optin(index);
    return false;
  });

  $('body').on('click', '.optout', function(event) {
    var index = $(event.target).attr('data-row');
    $('#row-'+index).hide(400);
    $('.optin[data-row="'+index+'"]').show(400);
    return false;
  });

  $('.row-lang select').on('change', update_rows);
  update_rows();

  window.encode = function() {
    result = {};
    for (var i=0; i<editor_schema.length; i++) if ($('#row-'+i).is(":visible")) {
      var item = editor_schema[i];
      var value;
      if (item.type == 'choice')
        value = $('#row-'+i+' select').val();
      else if (item.type == 'string')
        value = $('#row-'+i+' input').val();
      else 
        value = codemirrors[""+i].getValue();
      result[item.key] = value;
    }
    return JSON.stringify(result);
  };

  window.decode = function(jsoned_websheet) {
    var obj = JSON.parse(jsoned_websheet || '{}' );
    var lang = obj.lang || '';
    $('#optionals').html('');
    for (var i=0; i<editor_schema.length; i++) {
      var item = editor_schema[i];
      if (item.lang && lang != item.lang 
          || item.langs && item.langs.indexOf(lang) == -1) {
        $('#row-'+i).hide();
      }
      else {
        if (item.optional) {
          $('#optionals').append(' <button data-row="'+i+'" class="optin">'+item.label+'</button>');
          $('#row-'+i).hide();
        }
        if (obj.hasOwnProperty(item.key)) {
          $('#row-'+i).show();
          optin(i, 0); // no animation delay
          var value = obj[item.key];
          if (item.type == 'choice')
            $('#row-'+i+' select').val(value);
          else if (item.type == 'string')
            $('#row-'+i+' input').val(value);
          else {
            codemirrors[""+i].setValue(value);            
          }          
        }
      }
    };
  };

  window.display_error = function(html) {
    $('div#error').html('<hr>'+html);
    $('div#error').show();
  }
  
  window.remove_error = function() {
    $('div#error').hide();
  }

  if (websheets.initialize_error) {
    display_error(websheets.initialize_error);
    $(".editor").hide();
  }

  if (websheets.initialize_editor !== undefined) {
    if (websheets.initialize_editor['new']) {
      //alert('You are creating a new websheet named '+websheets.GET['edit']);
    }
    else { 
      window.decode(websheets.initialize_editor['definition']);
      window.editstate = 'saved';
    }
  }

  var enable_buttons = function()  {
    if (websheets.editor_readonly)
      $('button.pure').prop("disabled",false);
    else {
      $('button, input, select').prop('disabled',false);
    for (var i=0; i<editor_schema.length; i++)
      if (codemirrors[""+i]) codemirrors[""+i].options.readOnly = false;
    }
  }

  var disable_buttons = function() {
    $('button, input, select').prop('disabled', true);
    for (var i=0; i<editor_schema.length; i++)
      if (codemirrors[""+i]) codemirrors[""+i].options.readOnly = true;
  }

  disable_buttons();
  enable_buttons();

  var change_callback = function() {
    $('span.unsaved-changes').show(400);
    $('div.preview').hide(200);
    remove_error();
  }

  $('body').on('change', 'select', change_callback);
  $('body').on('keypress', 'input', change_callback);
  for (var i=0; i<editor_schema.length; i++)
    if (codemirrors[i])
      codemirrors[i].on("change", change_callback);

  $('button#reload').on('click', function() {
    var msg = "";
    if ($('.unsaved-changes').is(':visible')) 
      msg = 'NOTE: you have unsaved changes!.\n';
    var slug = window.prompt(msg + "Enter the full path of the websheet to create or edit. E.g., cpp/arrays/echo");
    if (slug != null) {
      nowarn = true;
      window.location.href='?edit='+encodeURIComponent(slug); 
    }
    
  });

  $('button#export').on('click', function() {
    prompt("Copy this JSON of the currently defined websheet:", window.encode());
  });

  $('button#import').on('click', function() {
    var p = prompt("Paste your JSON websheet definition:")
    if (p != null)
      window.decode(p);
  });

  $('button#rename, button#copy, button#save, button#preview, button#delete').on('click', function() {
    var action = $(this).attr('id');
    if (action == 'delete' || action == 'rename') {
      if (!confirm("Do you really want to "+action+" " + websheets.GET['edit'] + "?"))
        return;
    }
    var request = {action: action, problem: websheets.GET['edit'], definition: window.encode(),
                   ajax_uid_intended: websheets.authinfo.username};
    if (action == 'rename' || action == 'copy') {
      var newname = prompt(action+ " to what new name? (Include the full path, e.g. cpp/cs201/halting)");
      if (newname == null) return;
      request.newname = newname;
    }    

    disable_buttons();
    $('#error').hide();
    $.ajax(websheets.urlbase + '/edit.php',
           {
             data: request,
             dataType: "json",
             
             success: function(data) {
               enable_buttons();
               if (typeof data == "string") alert(data);
               else {
                 if (data.success) 
                   display_error(data.message);
                 else {
                   remove_error();
                   alert('Failed: ' + data.message);
                 }
                 if (data.success && (action=='delete' || action=='rename' || action=='copy')) {
                   alert(action + ' successful.');
                   nowarn = true;
                   window.location.href='./editor.php' + (action!='delete'?'?edit='+newname:'');
                 }
                 if (data.success && action=='save') {
                   $('.unsaved-changes').hide(400);
                 }
                 if (data.success && action=='preview') {
                   $("div.preview").show();
                   if (websheets.previewer)
                     websheets.previewer.load(websheets.GET['edit']);
                   else
                     websheets.createAt(websheets.GET['edit'], null, $('div.preview'), true);
                     $('html, body').animate({
                       scrollTop: $("div.preview").offset().top
                     }, 2000);
                 }
               }
             },
             
             error: function(jqXHR, textStatus, errorThrown) {
               enable_buttons();
               if (textStatus == "parsererror") {
                 var info = jqXHR.responseText;
                 alert('Error: '+info);
               }}
           })
    
  });

  var nowarn = false;
  $(window).on('beforeunload', function(){
    if (!nowarn && $('.unsaved-changes').is(':visible')) {
      return 'You have unsaved changes.';
    }
  });
  
});

