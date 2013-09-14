
   resetup = function(data) {
     if (typeof window.testWS != 'undefined')
       window.testWS.cm.toTextArea();
     window.testWS = websheet("code", data.template_code );
     $("#description").html(data.description);
     testWS.cm.addKeyMap({F2: checkSolution});
   }

loadProblem = function(slug) {
  window.location.hash = slug;
  $("#page").removeClass("passed");
  $("#results").html("");
  $('#container').hide();
  $('#selectSheet')[0].disabled = true;
  $.ajax("load.php",
   {data: {problem: slug},
	   dataType: "json",
	   success: function(data) 
	   {
	       $('.exercise-header').html("Exercise Description: <code>" + slug + "</code>");
	       $('#container').show();
	       $('#selectSheet')[0].disabled = false;
	       resetup(data);
	       if (data.user_code != false)
		   testWS.setUserAreas(data.user_code);
	   }});
};

checkSolution = function() {
  $("#results").html("Waiting for a reply...");
  $("#page").removeClass("passed");
  $("#submitButton").attr("disabled", "disabled");
  var user_state = JSON.stringify(testWS.getUserCodeAndLocations());
  $.ajax("submit.php",
         {
           data: {stdin: user_state, problem: $('#selectSheet').val()},
           dataType: "json",
           success: function(data) {
	     //console.log(data);
	     $("#submitButton").removeAttr("disabled");
	     if (data.category == 'Passed') $("#page").addClass("passed");
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