var MILLS_TOIGNORE_LIKES = 500;

var processLike = function(){
	var $button_just_clicked_on = $(this);

	var color_id = $button_just_clicked_on.data('color_id');

 	var processServerResponse = function(serverResponse_data, textStatus_ignored,jqXHR_ignored)  {
 		$('#toggle_color_like_cell' + color_id).html(serverResponse_data);
 	}

 	var config = {
	 	url :
 	 	LIKE_URL_PRE_ID +color_id+ '/',
 		dataType : 'html',
 		success: processServerResponse
	};
	$.ajax(config);
};

$(document).ready(function(){
	$('.td__toggle_color_like_button').click(_debounce(processLike,MILLS_TOIGNORE_LIKES,true));

});