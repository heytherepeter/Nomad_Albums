$(document).ready(function(){
	$('#get_photos').click(function(e){
		e.preventDefault();
		console.log('prevented action');
		var req = $.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=25984466.fa53796.0028e4fd1be04930855b67ddf089d2f3');
		console.log('Got data', req)
		req.done(function(res){
			$('#photos_field').html(res);
			console.log('Changing div to', res);
		})
	})
})
