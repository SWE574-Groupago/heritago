(function() {
	var uNameJSON = "http://localhost:3000/userName";
	var itemsJSON = "http://localhost:3000/usersItems";
	
	$.getJSON( uNameJSON, {
		format: "json"
	})
		.done(function( data ) {
			var count = 0;
			var cnt = 0;
			$.each( data, function(key, userName) {
				$('#userName').text(userName);
			});
		});
	
	$.getJSON( itemsJSON, {
		format: "json"
	})
		.done(function( data ) {
			var count = 0;
			var cnt = 0;
			$.each( data, function(key, item) {
				$('#itemName' + count).text(item.itemName);
				$('#itemOwner' + count).text(item.itemOwner);

				for(cnt = 0; cnt <= 2; cnt++) {
					$('#img' + count + cnt).attr("src", "assets/img/" + item.imgSrc[cnt]);
					$('#img' + count + cnt).attr("alt", "assets/img/" + item.imgSrc[cnt]);
				}
				count++;
			});
		});
})();