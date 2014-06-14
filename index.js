var num_submissions;
var lastload;
var viewing_ref = false;
var saved_chunks; // when viewing reference, remember what used to be there

resetup = function(data) {
    if (typeof window.testWS != 'undefined')
	window.testWS.cm.toTextArea();
  window.testWS = websheet("code", data.template_code, lastload.initial_snippets);
    $("#description").html(data.description);
    MathJax.Hub.Typeset();
    testWS.cm.addKeyMap({F2: checkSolution, F5: function() {return false;}});
}

loadProblem = function(slug) {
  set_viewing_ref(false);
  window.location.hash = slug;
  $("#page").removeClass("passed");
  $("#page").removeClass("ever-passed");
  $("#results").html("");
  $("#after-results").hide();
  $('#container').hide();
  $('#errcontainer').hide();
  $('#selectSheet')[0].disabled = true;
  $('#selectSheet').val(slug);
  $.ajax("load.php",
         {data: {problem: slug},
	  dataType: "json",
	  success: function(data) 
          {
            lastload = data;
	    $('.exercise-header').html("Exercise Description: <code>" + slug + "</code>");
	    $('#container').show();
	    $('#selectSheet')[0].disabled = false;
	    resetup(data);
	    if (data.user_code != false)
	      testWS.setUserAreas(data.user_code);
            else {
              testWS.setUserAreas(data.initial_snippets);
	      var lc = testWS.cm.lineCount();
	      for (var i=0; i<lc; i++)
		testWS.cm.indentLine(i);
            }
	    if (data.ever_passed != false)
	      $('#page').addClass("ever-passed");
	    num_submissions = data.num_submissions;
	  },
          error: function(jqXHR, textStatus, errorThrown) {
            if (textStatus == "parsererror") {
              var info = jqXHR.responseText;
              $("#errcontainer").html("Error..."+info);
              $("#errcontainer").show();
	      $('#selectSheet')[0].disabled = false;
            }
          }
         });
};

checkSolution = function() {
  $("#results").html("Waiting for a reply...");
  $("#page").removeClass("passed");
  $("#submitButton").attr("disabled", "disabled");
  var user_state = JSON.stringify({viewing_ref:viewing_ref,
				   snippets:testWS.getUserCodeAndLocations()});
  $.ajax("submit.php",
         {
           data: {stdin: user_state, problem: $('#selectSheet').val()},
           dataType: "json",
           error: function(jqXHR, textStatus, errorThrown) {
	     $("#submitButton").removeAttr("disabled");
             $("#results").html("Internal Ajax Error!!! Please contact course staff. <br>" + 
                                "status: " + textStatus + "<br>" + 
                                (textStatus == "parsererror" ? "" : 
                                 ("error thrown: " + errorThrown + "<br>")) + 
                                "response text:<br><pre>" 
                                + jqXHR.responseText + "</pre>");  
             },
           success: function(data) {
	     //console.log(data);
	     num_submissions++;
	     $("#submitButton").removeAttr("disabled");
	     if (data.category == 'Passed' && !viewing_ref) {
		 $("#page").addClass("passed");
		 $('#page').addClass("ever-passed");
	     }
	     var results = data.results;
             if (data.epilogue) {
               $("#after-results").html("<div id='epilogue'>Epilogue</div>" + data.epilogue);
               $("#after-results").show();
             }
             $("#results").html(results);
             var line = results.match(/[Ll]ine (\d)+(?!\d)/);
             if (line != null && line.length > 0) {
               var lineno = parseInt(line[0].substr(5));
               testWS.tempAlert(lineno);
             }
             $("html, body").animate({ scrollTop: $(document).height() }, "slow");
           }
         });
};

var populateSheets = function(sheets) {
  for (var i=0; i<sheets.length; i++) {
    $('#selectSheet').append('<option value="' + sheets[i]+'">'
                             +sheets[i]
                             +"</option>");
  }
}

var auth = function(provider) {
  // go to ?group=prob1+prob2&start=prob2&auth=provider
  var url = '?auth='+provider;
  if (window.hasGroup)
    url += '&group=' + sheets.join('+');    
  url += '&start=' + $('#selectSheet').val();
  window.location.href = url;
}

    function set_viewing_ref(show_ref) {
	if (viewing_ref == show_ref)
	    return;
	// already looking at reference solution
	if (viewing_ref) {
	    testWS.readOnly = false;
	    testWS.setUserAreas(saved_chunks);
	    $("#page").removeClass("viewing-ref");
	    $("#resetButton").removeAttr("disabled");
	}
	// put in the reference solution
	else {
	    saved_chunks = testWS.getUserCode();
	    testWS.setUserAreas(lastload.reference_sol);
	    $("#results").html("");
	    $("#page").addClass("viewing-ref");
	    var lc = testWS.cm.lineCount();
	    for (var i=0; i<lc; i++)
		testWS.cm.indentLine(i);
	    testWS.readOnly = true;
	    $("#resetButton").attr("disabled", "disabled");
	}
	viewing_ref = !viewing_ref;
	$("#answerButton").html(viewing_ref ? "Go back to my solution" : "View reference solution");
    }

// stuff to do after page is loaded
$(function() {
  $("#resetButton").click( function(eventObject) {
    set_viewing_ref(false);
    testWS.setUserAreas(lastload.initial_snippets);
    var lc = testWS.cm.lineCount();
    for (var i=0; i<lc; i++)
      testWS.cm.indentLine(i);
  });
  
  $("#answerButton").click( function(eventObject) {
    if (num_submissions < 4 && !$("#page").hasClass("ever-passed")) {
      alert("You have to make 4 attempts or complete the problem before you can view the reference solution. " +
	    "You have made " + num_submissions + " attempts so far.");
    }
    else {
      set_viewing_ref(!viewing_ref);
    }
  });
       
  // use variables "sheets" and "GET" defined by the php script 
  // that included this js to initialize the list of sheets
  // and the first exercise to show

  populateSheets(sheets);
  
  var ex = "";
  
  // note! return from facebook auth changes hash
  if (window.location.hash 
      && sheets.indexOf(window.location.hash.substring(1)) >= 0)
    ex = window.location.hash.substring(1);
  else if ("start" in GET && sheets.indexOf(GET["start"]) >= 0)
    ex = GET["start"];
  else if ("group" in GET)
    ex = sheets[0];
  else
    ex = "Distance"; // a nice sample exercise
  
  loadProblem(ex);
  
});
