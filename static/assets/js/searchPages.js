(function() {
	var itemsJSON = "http://localhost:3000/searchItems";
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

$('#ulEndDate li').on("click", function(){
    $('#butEndDate').text($(this).text());
});

$('#ulStartDate li').on("click", function() {
    $('#butStartDate').text($(this).text());
});

$('#ulOrigin li').on("click", function() {
    $('#butOrigin').text($(this).text());
});