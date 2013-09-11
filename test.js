
   resetup = function(data) {
     if (typeof window.testWS != 'undefined')
       window.testWS.cm.toTextArea();
     window.testWS = websheet("code", data.code );
     $("#description").html(data.description);
     testWS.cm.addKeyMap({F8: checkSolution});
   }

loadProblem = function(slug) {
  window.location.hash = slug;
  $("#page").removeClass("passed");
  $("#results").html("");
  $('#container').hide();
  $('#selectSheet')[0].disabled = true;
  $.ajax("Websheet.php",
         {data: {args: "get_html_template "+$("#selectSheet").val(), 
                 stdin: ""},
          success: function(data) {
            if (data.substring(0, 1) != '{') // not json array -- so an error
              alert(data);
            else {
	      $.ajax("load.php",
		     {data: {problem: $("#selectSheet").val()},
			     success: function(user_data) {
			     $('#container').show();
			     $('#selectSheet')[0].disabled = false;
			     resetup(JSON.parse(data));
			     if (user_data != false)
				 testWS.setUserAreas(JSON.parse(user_data));
			 }
		     });
            }
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