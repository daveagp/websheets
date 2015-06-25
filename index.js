// stuff to do after page is loaded
$(function() {
   
   var snippet = "";
   if (websheets.authinfo.error_div != "") 
      snippet = websheets.authinfo.error_div;
   else if (websheets.authinfo.logged_in) 
      snippet = 
      "<p>Logged in as <b>"+websheets.authinfo.username+"</b>"+
      " (logged in through "+websheets.authinfo.domain+")."+
      " Click to <a href='javascript:websheets.auth_reload(\"logout\")'>"+
      " log out</a>.";
   else {
      snippet = '<p><b style="color:red">Not logged in, your work will '+
         'not be saved.</b> ';
      pretext = 'Login '; 
      if (websheets.authinfo.required_username_suffix)
         pretext += 'to your ' + websheets.authinfo.required_username_suffix + ' account ';
      pretext += 'via ';
      if (websheets.authinfo.providers.length==1) {
         snippet += '<a href="javascript:websheets.auth_reload(\'' +
            websheets.authinfo.providers[0] + '\')">' +
            pretext + websheets.authinfo.providers[0] + '</a>';
      }
      else {
         snippet += pretext;
         for (var i=0; i<websheets.authinfo.providers.length; i++)
            snippet += '<a href="javascript:websheets.auth_reload(\''
            + websheets.authinfo.providers[i] + '\')">' +
            websheets.authinfo.providers[i] + '</a>';
         }
   }
   $(".menu-bar").prepend(snippet);
   
   // use variables "sheets" and "GET" defined by the php script 
   // that included this js to initialize the list of sheets
   // and the first exercise to show
      
   // populator select input
   for (var i=0; i<websheets.sheets.length; i++) {
      $('#selectSheet').append('<option value="' + websheets.sheets[i]+'">'
                               +websheets.sheets[i]
                               +"</option>");
   }

   if (websheets.subfolders.length > 0) {
      $('#subfoldering').show();
      for (var i=0; i<websheets.subfolders.length; i++) {
         var val = websheets.subfolders[i];
         $('#selectSubfolder').append('<option value="' + val+'">'
                                      +(val==""?"/":val)
                                      +"</option>");
      }
   }
   
   // note! return from facebook auth changes hash
   var ex;
   if (window.location.hash 
       && websheets.sheets.indexOf(window.location.hash.substring(1)) >= 0)
      ex = window.location.hash.substring(1);
   else if ("start" in websheets.GET && 
            websheets.sheets.indexOf(websheets.GET["start"]) >= 0)
      ex = websheets.GET["start"];
   else if ("group" in websheets.GET)
      ex = websheets.sheets[0];
   else
      ex = "hello"; // a nice sample exercise
   
   $('#selectSheet').val(ex)
   var index_ws = websheets.createAt(ex, null, window.container);
   
   $("#selectSheet").on("change", function() {
      index_ws.load($('#selectSheet').val());
   });
   
   $("#enterSubfolder").on("click", function() {
      var query = {};
      if ($('#selectSubfolder').val() != "")
         query['group'] = $('#selectSubfolder').val();
      websheets.refresh_page(query);
   });
   
});
