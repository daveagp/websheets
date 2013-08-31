
   resetup = function(data) {
     if (typeof window.testWS != 'undefined')
       window.testWS.cm.toTextArea();
     window.testWS = websheet("code", data.code );
     $("#description").html(data.description);
     testWS.cm.addKeyMap({F8: checkSolution});
   }

loadProblem = function(slug) {
  window.location.hash = slug;
  $.ajax("Websheet.php",
         {data: {args: "get_html_template "+$("#selectSheet").val(), 
                 stdin: ""},
          success: function(data) {
            if (data.substring(0, 1) != '{') // not json array -- so an error
              alert(data);
            else {
              resetup(JSON.parse(data));
              $("#results").html("");
            }
          }});
};

checkSolution = function() {
  $("#results").html("Waiting for a reply...");
  $("#submitButton").attr("disabled", "disabled");
  var user_state = JSON.stringify(testWS.getUserCodeAndLocations());
  $.ajax("submit.php",
         {
           data: {stdin: user_state, args: $('#selectSheet').val() + " joestu"},
           dataType: "text",
           success: function(data) {
             $("#submitButton").removeAttr("disabled");
             $("#results").html(data);
             var line = data.match(/[Ll]ine (\d)+(?!\d)/);
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