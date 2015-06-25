// stuff to do after page is loaded
$(function() {

  if (websheets.current_folder=='') {
    $('#currfolder').html('<i>none</i>');
  }
  else {
    $('#currfolder').html('<tt>'+websheets.current_folder+'</tt>');
  }   

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
            websheets.authinfo.providers[i] + '</a> ';
         }
   }
   $(".menu-bar").prepend(snippet);
   
   // use variables "sheets" and "GET" defined by the php script 
   // that included this js to initialize the list of sheets
   // and the first exercise to show

  if (websheets.sheets[0] == "FOLDER_IS_EMPTY") {
    $('.exercise-header').hide();
    $('.selectspan').hide();
    $('.selectdiv').prepend('<p>This folder has no exercises. Please change to another folder.').show();
  }
  else {
   // populator select input
   for (var i=0; i<websheets.sheets.length; i++) {
      $('#selectSheet').append('<option value="' + websheets.sheets[i]+'">'
                               +websheets.sheets[i]
                               +"</option>");
   }
  }

   if (websheets.subfolders.length > 0) {
      $('#subfoldering').show();
      for (var i=0; i<websheets.subfolders.length; i++) {
         var val = websheets.subfolders[i];
         $('#selectSubfolder').append('<option value="' + val+'">'
                                      +val+(websheets.current_folder != '' && i==0?' (parent)':'')
                                      +"</option>");
      }
   }
   
   // note! return from facebook auth changes hash
   var ex;
   if ("start" in websheets.GET && 
            websheets.sheets.indexOf(websheets.GET["start"]) >= 0)
      ex = websheets.GET["start"];
   else 
      ex = websheets.sheets[0];

  var qualify = function(slug) {
    var qualified_slug = websheets.current_folder;
    if (qualified_slug != '') qualified_slug += '/';
    qualified_slug += slug;
    return qualified_slug;
  }

  // load something
  if (websheets.sheets[0] != "FOLDER_IS_EMPTY") {
    $('#selectSheet').val(ex);
    var index_ws = websheets.createAt(qualify(ex), null, window.container);
  }

   $("#selectSheet").on("change", function() {
     index_ws.load(qualify($('#selectSheet').val()));
   });  
   
   $("#enterSubfolder").on("click", function() {
      var query = {};
      if ($('#selectSubfolder').val() != "")
         query['folder'] = $('#selectSubfolder').val();
      websheets.refresh_page(query);
   });
   
});
