$( function() {

var cm = CodeMirror.fromTextArea(document.getElementById("code"),
  {
  mode: "text/x-java",
  theme: "neat", tabSize: 3, indentUnit: 3,
  lineNumbers: true,
  styleSelectedText: true,
  viewportMargin: Infinity});

cm.setValue("public static  max3(  ) {\n\n}");

function compare(pos1, pos2) {
 // 1: pos1 later; -1: pos1 earlier; 0: identical
  if (pos1.line < pos2.line) return -1;
  if (pos1.line > pos2.line) return 1;
  if (pos1.ch < pos2.ch) return -1;
  if (pos1.ch > pos2.ch) return 1;
  return 0;
}

function contains_strictly(int1, int2) {
  return (compare(int1.from, int2.from) < 0)
      && (compare(int2.to, int1.to) < 0);
}

var inline = [
     cm.markText({line: 0, ch: 13}, {line: 0, ch: 15},
            {className: "inline",
                       inclusiveLeft: true, inclusiveRight: true}),
     cm.markText({line: 0, ch: 20}, {line: 0, ch: 22},
            {           className: "inline",
                       inclusiveLeft: true, inclusiveRight: true})
                       ];

cm.markText({line:0,ch:13},{line:0,ch:14},{className: "inlineL"});
cm.markText({line:0,ch:14},{line:0,ch:15},{className: "inlineR"});

var block = [
     cm.markText({line: 0, ch: 25}, {line: 2, ch: 0},
            {readOnly: false, 
            className: "block",
                       inclusiveLeft: true, inclusiveRight: true})
                       ];

var user = [inline[0], inline[1], block[0]];

// this is better than readOnly since it works when you surround read-only text
// and try to change the whole selection
cm.on("beforeChange", function(cm, change) {
   for (var i=0; i<user.length; i++) {
      var mrange = user[i].find();
      if (contains_strictly(mrange, change)) return;
   }
   change.cancel();
});

cm.on("renderLine", function(cm, line, elt) {
     var ln = cm.getLineNumber(line);
     for (var i=0; i<block.length; i++) {
      var mrange = block[i].find();
                                  // <= looked too goofy
      if (mrange && mrange.from.line < ln && mrange.to.line > ln)
      {       //console.log(elt);// cm.addLineClass(line, "background", "green");
      $(elt).addClass("block");}
    }
});

cm.refresh();

});
