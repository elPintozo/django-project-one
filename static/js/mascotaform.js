$(document).ready(function() {
    $('select').material_select();
    //Corrigue error de bug de Materialize con los check
	$.each($(':checkbox'), function(k, v) {
	    var label = $(this).closest('label');
	    $(this).insertBefore(label);
	});
});