var num_submissions;
var lastload;
var viewing_ref = false;
var saved_chunks; // when viewing reference, remember what used to be there

   resetup = function(data) {
     if (typeof window.testWS != 'undefined')
       window.testWS.cm.toTextArea();
     window.testWS = websheet("code", data.template_code );
     $("#description").html(data.description);
     testWS.cm.addKeyMap({F2: checkSolution});
   }

loadProblem = function(slug) {
  set_viewing_ref(false);
  window.location.hash = slug;
  $("#page").removeClass("passed");
  $("#page").removeClass("ever-passed");
  $("#results").html("");
  $('#container').hide();
  $('#selectSheet')[0].disabled = true;
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
	       if (data.ever_passed != false)
		   $('#page').addClass("ever-passed");
	       num_submissions = data.num_submissions;
	   }});
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
           success: function(data) {
	     //console.log(data);
	     num_submissions++;
	     $("#submitButton").removeAttr("disabled");
	     if (data.category == 'Passed' && !viewing_ref) {
		 $("#page").addClass("passed");
		 $('#page').addClass("ever-passed");
	     }
	     var results = data.results;
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

    $(function() {
	    $("#resetButton").click( function(eventObject) {
			set_viewing_ref(false);
			testWS.setUserAreas(lastload.initial_snippets);
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
	});
