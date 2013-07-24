var java_keywords = {
    abstract:0, continue:0, for:0, new:0, switch:0,assert:0, default:0, 
    goto:0, package:0, synchronized:0, boolean:0, do:0, if:0, private:0, 
    this:0, break:0, double:0, implements:0, protected:0, throw:0, 
    byte:0, else:0, import:0, public:0, throws:0, case:0, enum:0, 
    instanceof:0, return:0, transient:0,catch:0, extends:0, int:0, 
    short:0, try:0, char:0, final:0, interface:0, static:0, void:0,class:0, 
    finally:0, long:0, strictfp:0, volatile:0, const:0, float:0, native:0, 
    super:0, while:0};

function load(textarea, fragments) {
  var leftmargin = $(this).offset().left 
    - $(this).parent().offset().left 
    - $(this).parent().css("padding-left").replace("px", "")
    - 7; //e.g. .CodeMirror pre gives an extra 4px
  var width = $(this).width();
  var height = $(this).height();    
  var cm = CodeMirror.
    fromTextArea(this, 
		 {mode: {name: "clike", keywords: java_keywords},
		  theme: "neat", tabSize: 3, indentUnit: 3}); 
  $(cm.getScrollerElement()).css("min-height", height);
  $(cm.getWrapperElement()).css("margin-left", leftmargin+"px");
};

$(function() {

  var fragments = [['text', 'hello'], 
                   ['user-inline', 'jello'],
                   ['text', 'fellow'],
                   ['user-inline', 'foo'],
                   ['text', 'some lines \n of text'],
                   ['user', 'a user \nfield']];

  var spans = array();

  var text = '';
  var row = 0;
  var col = 0; // position of the next character to appear

  for (var f=0; f<fragments.length; f++) {
    var type = fragments[f][0];
    if (type == 'text') {
      
    }
    else if (type == 'text') {
    }
    else if (type == 'user') {
    }
    else
  }
  
  var cm = CodeMirror(document.body,
                      {mode: {name: "clike", keywords: java_keywords},
                       theme: "neat", tabSize: 3, indentUnit: 3});

  for (var f=0; f<fragments.length; f++) {
    
  }
});