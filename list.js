$(function() {
  $("#searchField").on("input", function(){
    var search_terms = window.searchField.value.toLowerCase()
      .trim().split(" ");
    $("tr.problem").each(function(index, element) {
      var row = $(element);
      var name = row.find("td.name").html().toLowerCase();
      var author = row.find("td.author").html().toLowerCase();
      var data = name + " " + author;

      var matches = true;
      for (var $i=0; $i < search_terms.length; $i++)
        matches &= data.includes(search_terms[$i]);
      
      if (matches) row.removeClass('filteredout');
      else row.addClass('filteredout');
    });
  });
});
