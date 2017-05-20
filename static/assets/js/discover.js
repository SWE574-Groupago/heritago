(function() {
	var itemsJSON = "http://localhost:8000/api/v1/heritages";
	$.getJSON( itemsJSON, {
		format: "json"
	})
	.done(function( data ) {
        var items = [];
        var cnt = 0;
            $.each(data, function (key, item) {


                    if (item.multimedia.length > 0 )
                        var preview = item.multimedia[0].url;
                    else
                        var preview = "placeholder.png";

                    items.push('<div class="col-md-4 nopadding">' +
                        '<a href="heritage.html?id='+item.id+'">' +
                        '<div id="card0" class="thumbnail">' +
                        '<div class="card-head style-primary">' +
                        '<header>' + item.title + '</header>' +
                        '</div>' +
                        '<div class="nopadding">' +
                        '<img src="/api/v1' + preview + '" alt="preview" class="bordered imgimg center-block">' +
                        '</div>' +
                        '<div class="text-right">Not Implemented</div>' +
                        '<div class="card-body scrollDesc">' + item.description + '</div>' +
                        '</div>' +
                        '</a>' +
                        '</div>');
                    cnt++;

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