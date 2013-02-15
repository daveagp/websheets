var java_keywords = {
    abstract:0, continue:0, for:0, new:0, switch:0,assert:0, default:0, 
    goto:0, package:0, synchronized:0, boolean:0, do:0, if:0, private:0, 
    this:0, break:0, double:0, implements:0, protected:0, throw:0, 
    byte:0, else:0, import:0, public:0, throws:0, case:0, enum:0, 
    instanceof:0, return:0, transient:0,catch:0, extends:0, int:0, 
    short:0, try:0, char:0, final:0, interface:0, static:0, void:0,class:0, 
    finally:0, long:0, strictfp:0, volatile:0, const:0, float:0, native:0, 
    super:0, while:0};


//main
$(function() {
	$('body').
	    on('click', 
	       '.exercise-submit', 
	       function() {
		   var ex = $(this).parents("div.exercise");
		   var results = ex.find(".results");
		   results.html("Submtting your code...");
		   window.setTimeout(function() {results.html("This is only a UI demo. But it would check syntax, compile, grade, etc. on a server and give all of the responses in this area. The color could change when correct."); ex.css("background", "rgb(144, 255, 129)");}, 1000);
	       });
	
	$("input.oneliner").each(function() {
		$(this).autoGrowInput({
			comfortZone: 20, 
			    minWidth: $(this).attr('width')});
	    });
	
	$('textarea').each(function() {
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
	    });
    });