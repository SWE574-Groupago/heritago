(function() {
	var itemsJSON = "http://localhost:3000/searchItems";
	$.getJSON( itemsJSON, {
		format: "json"
	})
		.done(function( data ) {
            var items = [];
            var cnt = 0;
                $.each(data, function (key, item) {
                    if( cnt < 6 ) {
                        items.push('<div class="col-md-4 nopadding">' +
                            '<a href="#">' +
                            '<div id="card0" class="thumbnail">' +
                            '<div class="card-head style-primary">' +
                            '<header>' + item.itemName + '</header>' +
                            '</div>' +
                            '<div class="nopadding divimg">' +
                            '<img src="assets/img/' + item.imgSrc[0] + '" alt="assets/img/' + item.imgSrc[0] + '" class="bordered imgimg center-block">' +
                            '</div>' +
                            '<div class="text-right">' + item.itemOwner + '</div>' +
                            '<div class="card-body scrollDesc">' + item.itemDesc + '</div>' +
                            '</div>' +
                            '</a>' +
                            '</div>');
                        cnt++;
                    }
                });
            $('#cards').append(items.join(''));
		});
})();

AnyTime.picker( "startDate",
    {
        format: "%e %b %Y %E",
        formatUtcOffset: "%: (%@)",
        placement: "popup",
        latest: new Date()
    }
);

AnyTime.picker( "endDate",
    {
        format: "%e %b %Y %E",
        formatUtcOffset: "%: (%@)",
        placement: "popup",
        latest: new Date()
    }
);

function showAdv() {
    $('#advSearch').removeClass('hidden');
    $('#butAdvSearchHidden').removeClass('hidden');
    $('#butAdvSearchShow').addClass('hidden');
    $('#enterSearch').addClass('hidden');
    $('#enterSearchButton').addClass('hidden');
}

function hideAdv() {
    $('#advSearch').addClass('hidden');
    $('#butAdvSearchHidden').addClass('hidden');
    $('#butAdvSearchShow').removeClass('hidden');
    $('#enterSearch').removeClass('hidden');
    $('#enterSearchButton').removeClass('hidden');
}

$('#ulOriginCountries0 li').on("click", function() {
    $('#butOriginCountries0').text($(this).text());
});

$('#ulOriginCities0 li').on("click", function() {
    $('#butOriginCities0').text($(this).text());
    alert($(this).text());
});

$('#ulOriginCountries1 li').on("click", function() {
    $('#butOriginCountries1').text($(this).text());
});

$('#ulOriginCities1 li').on("click", function() {
    $('#butOriginCities1').text($(this).text());
    alert($(this).text());
});