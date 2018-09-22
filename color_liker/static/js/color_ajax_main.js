var MILLS_TOIGNORE_LIKES = 500;

var processLike = function(){
	var $button_just_clicked_on = $(this);

	var color_id = $button_just_clicked_on.data('color_id');
	
 	var processServerResponse = function(serverResponse_data, textStatus_ignored,jqXHR_ignored)  {

 		$('#toggle__color_like_cell_' + color_id).html(serverResponse_data);
 	}

 	var config = {
	 	url :'/color_liker/like_color_/'+color_id,
 		dataType : 'html',
 		success: processServerResponse
	};
	$.ajax(config);
};




var processSearch = function(){
	var MIN_SEARCH_CHARS = 2
	var SUBMIT_URL = $('#color_search_text').SUBMIT_URL
	var searchText = $('#color_search_text').val().trim().toLowerCase();

	if(searchText.length < MIN_SEARCH_CHARS){
		$('#color_search_text').html("");
	} else {
		var processServerResponse = function(serverResponse_data, textStaus_ignore, jqXHR_ignored){
			$('#color_search_results').html(serverResponse_data);
		}
	}

	var config={
		type:"GET",
		url : '/color_liker/search_colors',
		data:{
			'color_search_text': searchText,
		},
		dataType: 'html',
		success: processServerResponse
	};
	$.ajax(config)
};	


$(document).ready(function(){
	$('.td__toggle_color_like_button').click(processLike);

	$('#color_search_text').keyup( function() {
  		$("#color_search_text").autocomplete({
    		source: '/color_liker/get_color_ajax',
    		minLength: 2,
  });
});


});