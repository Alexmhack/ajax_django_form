(function() {
	console.log("Script is running");

	viewPage = $("h1").html();

	$.ajax({
		url: "/send-view-visit/",
		dataType: 'json',
		data: {
			'viewPage': viewPage
		},
		success: function(data) {
			console.log("Successfully send view visit...");
			console.log("Views for " + viewPage + ": " + data.total);
		},
		error: function(e, jqXHR, status) {
			console.log(e);
		}
	})
})()