window.websheets = {}; // namespace

websheets.all = [];

websheets.GET = {};
if (window.location.search) {
   var parts = window.location.search.substr(1).split("&");
   for (var i = 0; i < parts.length; i++) {
      var temp = parts[i].split("=");
//      console.log(temp, decodeURIComponent(temp[1]));
      websheets.GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
   }
}

websheets.url = function(tail) {
  var result = websheets.urlbase;
  if (result.slice(-1)!='/') result += '/';
  return result + tail;
}

websheets.load = function(slug) {
  var p = slug.lastIndexOf('/');
  if (p < 0)
    window.location.href = websheets.url('?start='+slug);
  window.location.href = websheets.url('?folder='+slug.substr(0, p)+'&start='+slug.substr(p+1));
}

websheets.refresh_page = function(query) {
   var url = '';
   for (var key in query) if (query.hasOwnProperty(key)) {
      var comp = query[key];
     comp=encodeURIComponent(comp).replace(/%2F/g, '/');
      url += "&" + key + "=" + comp;
   }
   window.location.href = '?' + url.substring(1); // remove leading '&'
}

// refresh the page, loading this new provider
websheets.auth_reload = function(provider) {
   // for websheets/index.php
   if ($('#selectSheet').length > 0)
      websheets.GET['start'] = $('#selectSheet').val();
   websheets.GET['auth'] = provider;
   websheets.refresh_page(websheets.GET);
}

// open a new window and reload the current provider
// e.g., for when your login token has expired
// this is a static function.
websheets.popup_reauth = function(domain) {
  if (typeof domain === 'undefined') {
    domain = websheets.authinfo.domain;
    if (!websheets.authinfo.logged_in) domain = 'logout';
  }
  var newWindow = window.open(websheets.url('loginout.php?auth=' + domain));
  // hide the message and close the window once done.
  var intervalID = setInterval(function(){
    try {
      if (newWindow.loginout_loaded) {
        if (websheets.auth_by_embed) {
          websheets.set_authinfo(newWindow.authinfo);
        }
        newWindow.close();
        $(".ws_error_span").remove();
        clearInterval(intervalID);
      }
    }
    catch (err) {} // will get security errors until finished if cross-site login window
  }, 100);
};

websheets.set_authinfo = function(info) {
  // reload when username changes
  var reload_sheets =  websheets.authinfo &&
    websheets.authinfo.username != info.username;
  websheets.authinfo = info;
  if (info.error_span)
    $(".embed-authinfo").html(info.error_span);
  else {
    if (info.logged_in)
      $(".embed-authinfo").html("Logged in as " + info.username + ". <a href='javascript:websheets.popup_reauth(\"logout\")'>Log out</a>");
    else {
      var msg = "Not logged in, your work will not be saved. Log in with ";
      for (var i=0; i<info.providers.length; i++) {
        if (i != 0) msg += ' or ';
        msg += "<a href='javascript:websheets.popup_reauth(\""+info.providers[i]+"\")'>"+info.providers[i]+"</a>";
      }
      $(".embed-authinfo").html(msg +".");
    }
  }
  if (reload_sheets)
    for (var i=0; i<websheets.all.length; i++)
      websheets.all[i].load();
}

websheets.skipauthwarn = false;
// make a warning. then return true if user cannot edit.
websheets.authwarn = function() {
  console.log('authwarn');
  if (websheets.authinfo.logged_in)
    return false;
  if (websheets.require_login) {
    alert("Note: you are not logged in. Since your work would not be saved, you cannot edit code. Please login using the link at the top right.");
    return true;
  }
  else {
    if (!websheets.skipauthwarn) {
      alert("Not logged in. WARNING: your work will not be saved.");
      websheets.skipauthwarn = true;
    }
    return false;
  }
}

// if data is null, fetch it asynchronously
// otherwise, it should be the json output of a 'load'
websheets.createHere = function(slug, data) {
   var arrScripts = document.getElementsByTagName('script');
   var currScript = arrScripts[arrScripts.length - 1];
   var containerdiv = $(currScript).closest('div');
  return websheets.createAt(slug, data, containerdiv);
}

websheets.createAt = function(slug, data, containerdiv, preview) {
   $(containerdiv).addClass("wscontainer");
   $(containerdiv).addClass("show-body");
     var template = ' \
<div class="embed-authinfo"></div> \
<div class="exercise-header"><span class="title"></span><a class="sharing"><img src="'+websheets.url('images/cc.png')+'"></a></div> \
 <div class="exercise-body"> \
   <div class="description"></div> \
   <textarea class="code" name="code" ></textarea> \
   <table class="buttonTable"><tbody><tr> \
    <td style="width:33%"> \
    <button class="noprint submitButton"> \
     Submit \
    </button> \
   </td> \
   <td style="width:33%"> \
    <button class="noprint resetButton"> \
     Start over \
    </button> \
   </td> \
    <td style="width:33%"> \
    <button class="noprint showrefButton"> \
     View reference solution \
    </button> \
    <button style="display:none" class="noprint hiderefButton"> \
     Go back to my solution \
    </button> \
   </td> \
   </tbody></table> \
   <div class="noprint results"></div> \
   <div class="noprint after-results" style="display:none"></div> \
  </div> <!-- exercise-body --> \
  </div> <!-- container -->';

$(containerdiv).html(template); // too slow?
//$(containerdiv).append($.parseHTML(template)[0]); // force adding to DOM?

   if (websheets.header_toggling)
      $(containerdiv).find('.exercise-header').addClass('toggleable');
  var ws = new websheets.Websheet(slug, data, containerdiv, preview);
   websheets.all.push(ws);
   return ws;
};

// embedding tool
(function() {
   // don't pollute things with new variables
   // the callback
   var process = function (parent, child) {
      if (child.nodeName=="DIV" && child.classList.contains("websheet-stub"))
         websheets.createAt(child.innerHTML, null, child);
   };

   // construct observer _before_ anything is rendered
   var mo = new MutationObserver(
      // constructor argument: callback on MutationRecord[]
      function (events) {
         // for each record,
         for (var i=0; i<events.length; i++)
            // MutationRecord has Node "target" and Node[] "addedNodes"
            for (var j=0; j<events[i].addedNodes.length; j++)
               // we'll define "process(parent, child)" below
               process(events[i].target, events[i].addedNodes[j]);
      }
   );

   // what should we observe, and with what options?
   mo.observe(document, {childList: true, subtree: true});
})();

websheets.Websheet = function(slug, data, div, preview) {
   var this_ws = this; // to access in callbacks
   
   this.slug = slug;
   this.div = div; // .wscontainer
  
   if (typeof preview == "undefined" || preview == false)
     preview = "False";
   else
     preview = "True";
   this.preview = preview;
 
   this.num_submissions = 0;
   this.viewing_ref = false;
   this.changing_viewing_ref = false;
   this.saved_chunks = undefined; // remember user code when viewing ref
   this.load_data = undefined;
   this.wse = undefined; // websheetEditor object
   this.reference_sol = undefined;
   
   $(this.div).find(".results").html("");
   $(this.div).find(".after-results").hide();
   $(this.div).find('.container').hide();
   $(this.div).find('.errcontainer').hide();
   
   $(this.div).find('.resetButton').click( function(eventObject) {
      this_ws.reset();
   });
   
   $(this.div).find('.submitButton').click( function(eventObject) {
      this_ws.submit();
   });
   
   $(this.div).find('.hiderefButton').click( function(eventObject) {
      this_ws.hideRef();
   });

   if (websheets.header_toggling) {
      $(this.div).find('.exercise-header').click( function(eventObject) {
        // dont expand when clicking on (cc) link
        if (eventObject.target.tagName != 'IMG')
          this_ws.toggle();
      });
   }
   
   $(this.div).find('.showrefButton').click( function(eventObject) {
      this_ws.showRef();
   });
   
   if (data) 
      this.load_success(data); // avoid extra ajax
   else {
      this.load(); // load data wasn't passed, ajax it
   }
}

websheets.Websheet.prototype.reset = function() {
   var body = $(this.div).find('.exercise-body')
   var show = body.is(":visible"); 
   body.show();

   // setuserareas only works on visible things
   $(this.div).find('.results').empty();
   if (this.viewing_ref)
      this.hideRef();
   this.wse.setUserAreas(this.load_data.initial_snippets);
   this.wse.indentAllLines();

   if (!show) body.hide();
}

websheets.Websheet.prototype.toggle = function() {
   var body = $(this.div).find('.exercise-body');
   var this_ws = this;
   if ($(this_ws.div).hasClass('show-body')) {
      body.slideToggle(400, function() {
         $(this_ws.div).toggleClass('show-body');
      });
   }
   else { 
      $(this_ws.div).toggleClass('show-body');
      body.slideToggle();
   }
}

websheets.Websheet.prototype.updateTriesButton = function() {
  if (this.reference_sol) {
    $(this.div).find(".showrefButton").removeAttr("disabled");          
    $(this.div).find(".showrefButton").html("View reference solution");              
  }
  var triesleft = this.load_data.attempts_until_ref - this.num_submissions;
  // for anonymous users UI decides threshold
  if (triesleft <= 0) {
    if (this.anon_reference_sol) {
      this.reference_sol = this.anon_reference_sol;
      $(this.div).find(".showrefButton").removeAttr("disabled");          
      $(this.div).find(".showrefButton").html("View reference solution");              
    }
    return;
  }
  var msg = "View solution after "+triesleft+' more tr' + (triesleft > 1 ? 'ies':'y');
  $(this.div).find('.showrefButton').html(msg);  
}

websheets.Websheet.prototype.load_success = function(data) {
   var this_ws = this; // to access in callbacks
   this_ws.load_data = data;
   $(this_ws.div).find('.exercise-body').show();   
  $(this_ws.div).find('.showrefButton').show();
   
   var arrtmp = this_ws.slug.split("/");
   $(this_ws.div).find('.exercise-header .title')
      .html("<code>" + arrtmp[arrtmp.length-1] + "</code>");

  if (data.sharing.substring(0, 4)=='open') {
    $(this_ws.div).find('.exercise-header a.sharing img').show();
    $(this_ws.div).find('.exercise-header a.sharing').attr('href', websheets.url("editor.php?edit="+this_ws.slug));
  } 

   // for reloads
   $(this_ws.div).find(".CodeMirror").remove();
   $(this_ws.div).find(".results").html("");
   $(this_ws.div).find(".nocode-ui").remove();

   $(this_ws.div).find(".description").html(data.description);
   MathJax.Hub.Typeset();

   if (data.ever_passed != false)
      $(this_ws.div).addClass("ever-passed");
   else
      $(this_ws.div).removeClass("ever-passed");
   $(this_ws.div).removeClass("passed");

  // update solution revel button
   this_ws.num_submissions = data.num_submissions;   
  if (data.reference_sol) {
    // nothing to do
  }
  else if (data.attempts_until_ref == 'never') {
    $(this_ws.div).find('.showrefButton').hide();
  }
  else if (data.attempts_until_ref == 'infinity') {
    $(this_ws.div).find('.showrefButton').attr("disabled", "disabled");
    $(this_ws.div).find('.showrefButton').html('Solve to see reference solution');  
  }
  else {
    $(this_ws.div).find('.showrefButton').attr("disabled", "disabled");
    this.updateTriesButton();
  }

   if (data.nocode) {
      var markup = "";
      if (data.nocode.type=="multichoice") {
         for (var i=0; i<data.nocode.choices.length; i++)
            markup += "<div class='nocode-option'><input type='checkbox'/><label>"
            +data.nocode.choices[i]+"</label></div>";
      }
      else if (data.nocode.type=="shortanswer") {
         markup = "<input type='text' class='nocode-textinput'/>";
      }
      $(this_ws.div).find(".code").after("<div class='nocode-ui'>"+markup+"</div>");
      $(this_ws.div).addClass('nocode');
   }
   else {
      $(this_ws.div).removeClass('nocode');
      this_ws.wse = websheets.WebsheetEditor( // no new, pseudoclass
         $(this_ws.div).find(".code")[0], 
         data.template_code, 
         data.initial_snippets);

      
   
//   $(function() {$(this_ws.div).find('.exercise-body').hide();});
      this_ws.wse.cm.addKeyMap({F2: function(){this_ws.submit();}});
   
      if (data.user_code != false)
         this_ws.wse.setUserAreas(data.user_code);
      else {
         this_ws.wse.setUserAreas(data.initial_snippets);
         this_ws.wse.indentAllLines();
      }
   
   this_ws.wse.cm.on("beforeChange", function(cm, change) {
     if (!this_ws.setting_viewing_ref && websheets.authwarn())
       change.cancel();
   });   
   
      this_ws.reference_sol = data.reference_sol;

   }
   // if header_toggling is enabled, start as hidden
   if (websheets.header_toggling) {
      $(this_ws.div).find('.exercise-body').hide();
      $(this_ws.div).removeClass('show-body');
   }
}

function getQueryVariable(variable) // https://css-tricks.com/snippets/javascript/get-url-variables/
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return("");
}

websheets.Websheet.prototype.load = function(newslug) {
   var this_ws = this; // to access in callbacks

   $(this_ws.div).find(".exercise-body").hide();
   $(this_ws.div).find(".exercise-header .title").html('loading&hellip;');
  $(this_ws.div).find('.exercise-header a.sharing img').hide();
   
   if (newslug)
      this_ws.slug = newslug;

  var doauth = websheets.auth_by_embed && !websheets.authinfo;
  
  var request = {problem: this_ws.slug,
                 preview: this_ws.preview,
                 student: getQueryVariable("student")};

  if (!doauth) request['ajax_uid_intended'] = websheets.authinfo.username;

  $.ajax(websheets.url("load.php"), {
    data: request,
    dataType: "json",
      
      success: function(data) {
        if (doauth) {
          websheets.set_authinfo(data . authinfo);
        }
         $(this_ws.div).find(".load-error").remove();
         if (data.error_span) {
            $(this_ws.div).prepend('<span class="load-error">'+data.error_span+'</span>');            
         }
         else {
            this_ws.load_success(data);
         }
      },      
      error: function(jqXHR, textStatus, errorThrown) {
         $(this_ws.div).find(".load-error").remove();
         if (textStatus == "parsererror") {
            var info = jqXHR.responseText;
            $(this_ws.div).find(".exercise-body").hide();
            $(this_ws.div).find(".exercise-header .title").html('Error');
            $(this_ws.div).find(".exercise-header").after("<div class='load-error'>Error: "+info+"</div>");
         }
      }
   });
} // end of load method

websheets.Websheet.prototype.submit = function() {
   var this_ws = this; // to access in callbacks
   
   $(this.div).find(".results").html("Waiting for a reply...");
   $(this.div).removeClass("passed");
   $(this.div).find(".submitButton").attr("disabled", "disabled");
   
   var user_state = {
      viewing_ref: this.viewing_ref,
      frontend_user: websheets.authinfo.username
   };

   if (this.load_data.nocode) {
      if (this.load_data.nocode.type=="multichoice") {
         user_state['nocode_state'] = [];
         var boxes = $(this.div).find(".nocode-option input");
         for (var i=0; i<boxes.length; i++) {
            user_state['nocode_state'][i] = boxes[i].checked;
         }
      }
      else if (this.load_data.nocode.type=="shortanswer") {
         user_state['nocode_state'] = $(this.div).find("input")[0].value;
      }
   }
   else {
      user_state['snippets'] = this.wse.getUserCodeAndLocations();
   }
  user_state['preview'] = this_ws.preview;
  $.ajax(websheets.url("submit.php"), {
      data: {stdin: JSON.stringify(user_state), problem: this_ws.slug,
             ajax_uid_intended: websheets.authinfo.username},
      dataType: "json",
      error: function(jqXHR, textStatus, errorThrown) {
	 $(this_ws.div).find(".submitButton").removeAttr("disabled");
         $(this_ws.div).find(".results").html(
            "Internal Ajax Error!!! Please contact course staff. <br>" + 
               "status: " + textStatus + "<br>" + 
               (textStatus == "parsererror" ? "" : 
                ("error thrown: " + errorThrown + "<br>")) + 
               "response text:<br><pre>" 
               + jqXHR.responseText + "</pre>");  
      },
      success: function(data) {
        if ('error_span' in data && data['error_span'] != '') {
	  $(this_ws.div).find(".submitButton").removeAttr("disabled");
          $(this_ws.div).find(".results").html(data['error_span']);
          return;
        }

        if (!this_ws.reference_sol && data.reference_sol) {
          this_ws.reference_sol = data.reference_sol;
	  $(this_ws.div).find(".showrefButton").removeAttr("disabled");          
	  $(this_ws.div).find(".showrefButton").html("View reference solution");          
        }

	 //console.log(data);
	 this_ws.num_submissions++;
        if (data.anon_reference_sol)
          this_ws.anon_reference_sol = data.anon_reference_sol;
        if (!this_ws.reference_sol && ["never", "infinity"].indexOf(this_ws.load_data.attempts_until_ref)==-1) 
            this_ws.updateTriesButton(); 
	 $(this_ws.div).find(".submitButton").removeAttr("disabled");
	 if (data.category == 'Passed' && !this_ws.viewing_ref) {
	    $(this_ws.div).addClass("passed");
	    $(this_ws.div).addClass("ever-passed");
	 }
	 var results = data.results;
         if (data.epilogue) {
            $(this_ws.div).find(".after-results")
               .html("<div class='epilogue'><div class='header'>Epilogue</div>" 
                     + data.epilogue + '</div>');
            $(this_ws.div).find(".after-results").show();
         }
         $(this_ws.div).find(".results").html(results);
        console.log(results)
        var re = /([Ll]ine |\.cpp:)([0-9]+)/; // greedy :)
        var line = re.exec(results);
         if (line != null && line.length > 0) {
            var lineno = parseInt(line[2]); // group 2 holds the [0-9]+
            this_ws.wse.tempAlert(lineno);
         }
         //$("html, body").animate({ 
         //    scrollTop: $(document).height() 
         //}, "slow");
      }
   });
};

websheets.Websheet.prototype.hideRef = function() {
   this.setting_viewing_ref = true;
   this.wse.readOnly = false;
   this.wse.setUserAreas(this.saved_chunks);
   $(this.div).removeClass("viewing-ref");
   $(this.div).find(".hiderefButton").hide();
   $(this.div).find(".showrefButton").show();
   $(this.div).find(".results").html("");
   this.wse.indentAllLines();
   this.viewing_ref = false;
   this.setting_viewing_ref = false;
}

websheets.Websheet.prototype.set_viewing_ref = function(ref) {
   if (this.viewing_ref != ref) {
      if (ref) this.hideRef();
      else this.showRef();
   }
}

websheets.Websheet.prototype.showRef = function() {
   this.setting_viewing_ref = true;
   $(this.div).addClass("viewing-ref");
   $(this.div).find(".hiderefButton").show();
   $(this.div).find(".showrefButton").hide();
   this.saved_chunks = this.wse.getUserCode();
   this.wse.setUserAreas(this.reference_sol);
   $(this.div).find(".results").html("");
   this.wse.indentAllLines();
   this.viewing_ref = true;
   this.wse.readOnly = true;
   this.setting_viewing_ref = false;
}


// WebsheetEditor pseudo-class is just for the CodeMirror interactions,
// not for the surrounding UI
websheets.WebsheetEditor = function(textarea_element, fragments, initial_snippets) {
   
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
   
   function goto(range, inline) {
      if (!inline)
         // put at end of first line in this multi-line region
         return {line: range.from.line+1,
                 ch: cm.getLine(range.from.line+1).length};
      
      var pos = range.to.ch-1;
      // put at end of region, but before any trailing spaces
      while (pos > range.from.ch+1 && cm.getLine(range.to.line).charAt(pos-1)==' ')
         pos--;
      
      return {line: range.from.line, ch: pos};
   }
   
   // tab jumps you to the start of the next input field
   function next_blank(reverse) {
      if (typeof reverse === 'undefined') reverse = false;
      var pos = cm.getCursor();
      var first = null;
      var tgt = null;
      for (var i=(reverse ? editable.length-1 : 0); i>=0 && i<editable.length; i += (reverse ? -1 : 1)) {
         var ustart = goto(editable[i].find(), editable_info[i].type=="inline");
         if (compare(ustart, pos) == (reverse ? -1 : 1)) {
            cm.setCursor(ustart);
            return;
         }
      }
      var x = reverse ? editable.length-1 : 0;
      cm.setCursor(goto(editable[x].find(), editable_info[x].type=="inline"));
   }
   
   var keyMap = {PageDown: function() {next_blank(false); return true;},
                 PageUp: function() {next_blank(true); return true;},
                 Tab: function() {
                    var lo = cm.getCursor("start").line;
                    var hi = cm.getCursor("end").line;
                    for (var i = lo; i <= hi; i++)
                       cm.indentLine(i, "smart");
                    cm.setCursor(cm.getCursor("end"));
                 }
                };
   
   var cm = CodeMirror.fromTextArea(textarea_element, {
      mode: "text/x-c++src",
      theme: "neat", tabSize: 3, indentUnit: 3,
      lineNumbers: true,
      styleSelectedText: true,
      viewportMargin: Infinity,
      extraKeys: keyMap,
      matchBrackets: true
   });
   
  var firsteditable = 1;
  if (fragments[0] == "" && fragments[1].charAt(0) == "\n") {
    fragments[1] = fragments[1].substring(1);
  }
//  console.log(fragments);
   cm.setValue(fragments.join(""));
   
   var inline = new Array();
   var block = new Array();
   var editable = new Array();
   var editable_info = new Array();
   var inline_width = new Array();
   var block_height = new Array();
   
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
      
      if (i%2 == firsteditable) { // alternate chunks are for user input
         if (fragments[i].length < 1) {
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

        var incleft = (oldline == 0 && oldch == 0);
         var marker = cm.markText(
            {line: oldline, ch: oldch},
            {line: line, ch: ch},
           {className: lastNL==-1?"inline":"block", inclusiveLeft:incleft});
//        console.log({line: oldline, ch: oldch},
  //                  {line: line, ch: ch},
    //                {className: lastNL==-1?"inline":"block"});
         editable.push(marker);
         editable_info.push(lastNL==-1?{"type":"inline", "index":inline.length}
                            :{"type":"block", "index":block.length});
         if (lastNL==-1) { // inline
            inline.push(marker);
            inline_width.push(initial_snippets[(i-1)/2].length);
            
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
            block_height.push(initial_snippets[(i-1)/2].length);
            for (var ell=oldline+1; ell<line; ell++)
               cm.indentLine(ell, "smart");
         }
      }
   }
   
   var retval;
   
   var override = false;
   
   var latest_change = -1; //{"type": "block" or "inline"; "index": integer; "delta": integer}
   // delta is # added lines for block, # added chars for inline
   
   // this is better than readOnly since it works when you surround read-only text
   // and try to change the whole selection
   cm.on("beforeChange", function(cm, change) {
      if (override) return;
      if (retval.readOnly) {change.cancel(); return;}
      
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
        if (fixedrange.from.ch == 0 && fixedrange.from.line == 0)
          fixedrange.from.line = -1;
         latest_change = i; // for removing excess trailing space
         
         if (editable_info[i].type == "inline" && change.to.ch == fixedrange.to.ch-1)
            latest_change = -1; // don't apply in this case
         
         if (editable_info[i].type == "block" && change.to.line == fixedrange.to.line-1)
            latest_change = -1; // don't apply in this case
         
         // allow changes within an editable region
         if (contains_strictly(fixedrange, change)) {
            //console.log(change.to, fixedrange.to);
            return;
         }
         
         // the editor often replaces '\n...' by '\n...', allow it
         if (compare(fixedrange.from, change.from)==0
             && compare(fixedrange.to, change.to)<0
             && cm.getLine(fixedrange.from.line).charAt(fixedrange.from.ch)=='\n'
             && change.test.length > 1 && change[0] == '') // first char is '\n' 
         {
            //console.log(change.to, fixedrange.to);
            return;
         }
      }
      latest_change = -1; // nothing to fix up
      change.cancel();
   });
   
   // prevent trailing space bloating
   cm.on("change", function(cm, change) {
      if (latest_change == -1) return;
      var change_info = editable_info[latest_change];
      var region = editable[latest_change].find();
      if (change_info.type == "inline") {
         var addedChars = change.text[0].length-change.removed[0].length;
         var excessChars = Math.max(0, region.to.ch - region.from.ch - inline_width[change_info.index]);
         var maxCharsToRemove = Math.max(0, Math.min(addedChars, excessChars));
         if (maxCharsToRemove > 0) {
            var charsToRemove = 0;
            var curr = cm.getRange(
               {"line":region.to.line, "ch":region.to.ch-1-maxCharsToRemove},
               {"line":region.to.line, "ch":region.to.ch-1});
            for (var i=maxCharsToRemove-1; i>=0; i--) {
               if (curr.charAt(i)!=" ") break;
               charsToRemove++;
            }
            if (charsToRemove > 0)
               cm.replaceRange("",
                               {"line":region.to.line, "ch":region.to.ch-1-charsToRemove},
                               {"line":region.to.line, "ch":region.to.ch-1});
         }
      }
      else {
         var addedLines = change.text.length-change.removed.length;
         var excessLines = Math.max(0, region.to.line - region.from.line - block_height[change_info.index]);
         var maxLinesToRemove = Math.max(0, Math.min(addedLines, excessLines));
         if (maxLinesToRemove > 0) {
            var linesToRemove = 0;
            var curr = cm.getRange(
               {"ch":0, "line":region.to.line-1-maxLinesToRemove},
               {"ch":0, "line":region.to.line-1}).split("\n"); // there's a trailing empty at the end, not a big deal
            for (var i=maxLinesToRemove-1; i>=0; i--) {
               if (!curr[i].match(/^\s*$/)) break;
               linesToRemove++;
            }
            //console.log(maxLinesToRemove, curr, linesToRemove);
            if (linesToRemove > 0)
               cm.replaceRange("",
                               {"ch":0, "line":region.to.line-1-linesToRemove},
                               {"ch":0, "line":region.to.line-1});
         }
      }
      latest_change = -1; // don't correct it twice
   });
   
   // auto-indent when typing 1st char of line
   cm.on("change", function(instance, changeObj) {
      if (cm.getDoc().getSelection().length == 0) {
         var lo = cm.getCursor("start").line;
         if (cm.getLine(lo).trim().length == 1) {
            cm.indentLine(lo, "smart");
         }
      }
   }
        );
   
   cm.on("renderLine", function(cm, line, elt) {
      var ln = cm.getLineNumber(line);
      for (var i=0; i<block.length; i++) {
         var mrange = block[i].find();
         if (mrange && mrange.from.line < ln && mrange.to.line > ln
            || mrange.from.ch == 0 && mrange.from.line == 0 && ln == 0) $(elt).addClass("block");
      }
   });
   
   var hhandle = null;
   cm.on("change", function() {
      if (hhandle != null) cm.removeLineClass(hhandle, "wrapper", "tempAlert");
      hhandle = null;
   });
   
   cm.refresh();
   
   var setUserAreas = function(data) {
      for (var i=0; i<data.length; i++) {
	 var f = editable[i].find().from;
	 var t = editable[i].find().to;
//         console.log(f, t);
	 if (data[i].indexOf("\n") != -1) {
	   f = f.line+f.ch==0 ? f : {line: f.line+1, ch: 0};
	    t = {line: t.line-1, ch: cm.getLine(t.line-1).length};
	 }
	 else {
	    f = {line: f.line, ch: f.ch+1};
	    t = {line: t.line, ch: t.ch-1};
	 }
	 cm.replaceRange(data[i].substring(1, data[i].length-1), f, t);
      }
   }
   
   retval = {
      getUserCode: function() {
         var result = new Array();
         for (var i=0; i<editable.length; i++) {
            var range = editable[i].find();
            result.push(cm.getRange(range.from, range.to));
         }
         return result;
      },
      getUserCodeAndLocations: function() {
         var result = new Array();
         for (var i=0; i<editable.length; i++) {
            var range = editable[i].find();
            result.push({
               code: cm.getRange(range.from, range.to),
               // add one since what the gutter displays is one more than the line index
               from: {line: range.from.line+1, ch: range.from.ch},
               to: {line: range.to.line+1, ch: range.to.ch}
            });
         }
         return result;      
      },
      indentAllLines: function() {
         var lc = cm.lineCount();
         for (var i=0; i<lc; i++)
            cm.indentLine(i);
      },
      tempAlert: function(line) {
        console.log("templaert", line);
         // subtract one since what the gutter displays is one less than the line index
         if (hhandle != null) cm.removeLineClass(hhandle, "wrapper", "tempAlert");
         hhandle = cm.addLineClass(line-1, "wrapper", "tempAlert");
      },
      readOnly: false,
      cm: cm,
      setUserAreas: setUserAreas
   };
   return retval;  
}

$(function() {
  if (websheets.auth_by_embed)
    $('body').addClass('show-embed-authinfo');


   $("body").on("click", ".nocode-option", function(event) {
      var cb = $(event.target).closest('.nocode-option').find('input')[0];
     if (websheets.authwarn()) {
       cb.checked = false;
       return false;
     }

     if (cb != event.target)
       cb.checked = !cb.checked;
   });
   $("body").on("input", ".nocode-textinput", function(event) {
     if (websheets.authwarn()) {
       event.target.value = "";
       return false;
     }
   });
});

function delete_metacomments(){
    var code = $('textarea#smart-paste').val();    
    // replace (delete) metacomments:     /**:    and       :**/    
    code = code.replace( /\/\*\*\:/g, '');
    code = code.replace( /\:\*\*\//g, '');
    codemirrors["source_code"].setValue(code);
}
