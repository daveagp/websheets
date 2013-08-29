
function websheet(textarea_id, fragments) {
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

  // tab jumps you to the start of the next input field
  function do_tab() {
    var pos = cm.getCursor();
    var first = null;
    for (var i=0; i<editable.length; i++) {
      var ustart = editable[i].find().from;
      if (cm.getLine(ustart.line).length == ustart.ch) 
        ustart = {line: ustart.line+1, ch: 0};
      else
        ustart.ch++;
      if (compare(ustart, pos) == 1) {
        cm.setCursor(ustart);
        return;
      }
      if (first == null) first = ustart;
    }
    cm.setCursor(first);
  }

  var cm = CodeMirror.fromTextArea(document.getElementById(textarea_id), {
    mode: "text/x-java",
    theme: "neat", tabSize: 3, indentUnit: 3,
    lineNumbers: true,
    styleSelectedText: true,
    viewportMargin: Infinity,
    extraKeys: { Tab: do_tab }
  });

  cm.setValue(fragments.join(""));

  var inline = new Array();
  var block = new Array();
  var editable = new Array();

  var line = 0;
  var ch = 0;
  for (var i=0; i<fragments.length; i++) {
    var oldline = line;
    var oldch = ch;
    var lastNL = fragments[i].lastIndexOf("\n");

    if (lastNL == -1) {
      ch += fragments[i].length;
    }
    else {
      for (var j=0; j<fragments[i].length; j++)
        if (fragments[i].charAt(j)=='\n') line++;
      ch = fragments[i].length - lastNL - 1;
    }

    if (i%2 == 1) { // alternate chunks are for user input
      if (fragments[i].length < 2) {
        cm.toTextArea();
        var errmsg = "Error: fragment " + i + " is too short";
        console.log(errmsg, fragments);
        return;
      }
      
      // check for errors
      if (lastNL != -1) {
        if (fragments[i].charAt(0)!='\n'
            || fragments[i].charAt(fragments[i].length-1)!='\n') {
          cm.toTextArea();
          var errmsg = "Error: fragment " + i + " contains a newline, must start and end with a newline";
          console.log(errmsg, fragments);
          return;
        }
      }
      else {
        if (fragments[i].charAt(0)!=' '
            || fragments[i].charAt(fragments[i].length-1)!=' ') {
          cm.toTextArea();
          var errmsg = "Error: fragment " + i + " contains no newline, must start and end with a space";
          console.log(errmsg, fragments);
          return;
        }
      }
      
      var marker = cm.markText(
        {line: oldline, ch: oldch},
        {line: line, ch: ch},
        {className: lastNL==-1?"inline":"block"});
      editable.push(marker);
      if (lastNL==-1) { // inline
        inline.push(marker);
        // mark half-char widths
        cm.markText({line: oldline, ch: oldch},
                    {line: oldline, ch: oldch+1},
                    {className: "inlineL"});
        cm.markText({line: line, ch: ch-1},
                    {line: line, ch: ch},
                    {className: "inlineR"});
      }
      else { // block
        block.push(marker);
        for (var ell=oldline+1; ell<line; ell++)
          cm.indentLine(ell, "smart");
      }
    }
  }
  
  // this is better than readOnly since it works when you surround read-only text
  // and try to change the whole selection
  cm.on("beforeChange", function(cm, change) {

    // cancel newlines in inline regions
    if (change.text.length > 1) // array of lines; is there a newline?
      for (var i=0; i<inline.length; i++) {
        var inlinerange = inline[i].find();
        if (contains_strictly(inlinerange, change)) {
          change.cancel();
          return;
        }
      }

    // only allow changes within editable regions
    for (var i=0; i<editable.length; i++) {
      var fixedrange = editable[i].find();
      if (contains_strictly(fixedrange, change)) return;
    }
    change.cancel();
  });
  
  cm.on("renderLine", function(cm, line, elt) {
    var ln = cm.getLineNumber(line);
    for (var i=0; i<block.length; i++) {
      var mrange = block[i].find();
      if (mrange && mrange.from.line < ln && mrange.to.line > ln) $(elt).addClass("block");
    }
  });
  
  cm.refresh();

  return {
    getUserCode: function() {
      var result = new Array();
      for (var i=0; i<editable.length; i++) {
        var range = editable[i].find();
        result.push(cm.getRange(range.from, range.to));
      }
      return result;
    }};
  
}
