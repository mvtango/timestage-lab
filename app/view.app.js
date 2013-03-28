jQuery(function($) {
 
$('#viewTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
});

var parameter=recline.View.parseQueryString(decodeURIComponent(window.location.search));
var filename="data/json/"+parameter.id+".json";
$.getJSON(filename, function(d) { 
//	$("#json-source").val(JSON.stringify(d).replace("<","&lt;"));
	$("#json-source").html(JSON.stringify(d).replace(/&/g,"&amp;").replace(/</g,"&lt;"));
    // prettyPrint();
	window.data=d;
} );

var timeline_config = {
     width: "100%",
     height: "100%",
     source: filename
    }
	


 
 
});
