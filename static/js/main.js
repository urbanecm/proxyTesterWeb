testProxy = function () {

	var ip = $('#ip').val();
	var port = $('#port').val();

	if (ip != '')
	{
		$.get("https://tools.wmflabs.org/proxies/checkProxy?ip=" + ip + "&port=" + port, function ( respound ) {
			$( "<h1>" + respound + "</h1>" ).appendTo( "#returnVal" );
			//alert(respound);
		});
	}

};

$( document ).ready(function () {

	$('#testProxy').click(function () {
		testProxy();
		console.log('testing proxy');
	});

});
