(function() {
	var uNameJSON = "http://localhost:3000/userName";
	var itemsJSON = "http://localhost:3000/usersItems";
	
	$.getJSON( uNameJSON, {
		format: "json"
	})
		.done(function( data ) {
			$.each( data, function(key, userName) {
				$('#userName').text(userName);
			});
		});
	
	$.getJSON( itemsJSON, {
		format: "json"
	})
        .done(function( data ) {
            var items = [];
            $.each( data, function(key, item) {
                items.push('<a href="#">' +
                    '<div class="col-md-4 nopadding">' +
                    '<div id="card0" class="thumbnail">' +
                    '<div class="card-head style-primary">' +
                    '<header>' + item.itemName + '</header>' +
                    '</div>' +
                    '<div class="nopadding divimg">' +
                    '<img src="assets/img/' + item.imgSrc[0] + '" alt="assets/img/' + item.imgSrc[0] + '" class="bordered imgimg">' +
                    '</div>' +
                    '<div class="text-right">' + item.itemOwner + '</div>' +
                    '<div class="card-body">' + item.itemDesc + '</div>' +
                    '</div>' +
                    '</div>' +
                    '</a>');
            });
            $('#cards').append( items.join('') );
		});
})();