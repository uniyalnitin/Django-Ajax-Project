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
		url : SUBMIT_URL,
		data:{
			'color_search_text': searchText,
		},
		dataType: 'html',
		success: processServerResponse
	};
	$.ajax(config)
};	