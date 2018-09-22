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
