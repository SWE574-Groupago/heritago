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
                            '<div id="card0" class="thumbnail">' +
                            '<div class="card-head style-primary">' +
                            '<header>' + item.itemName + '</header>' +
                            '</div>' +
                            '<div class="nopadding divimg">' +
                            '<a href="#">' +
                            '<img src="assets/img/' + item.imgSrc[0] + '" alt="assets/img/' + item.imgSrc[0] + '" class="bordered imgimg">' +
                            '</a>' +
                            '</div>' +
                            '<div class="text-right">' + item.itemOwner + '</div>' +
                            '<div class="card-body">' + item.itemDesc + '</div>' +
                            '</div></div>');
                        cnt++;
                    }
                });
            $('#cards').append(items.join(''));
		});
})();
var cntAddCountry = 2;
function addCountry(){
    var items = [];
    var cntId = cntAddCountry+1;
        items.push('<div class="col-md-1 noBreak">' +
            '<h3 class="noBreak">' + cntAddCountry + '</h3>' +
            '</div>' +
            '<div class="btn-group col-md-5 noBreak">' +
            '<input id="autocomplete' + cntId + '" type="text" class="autocomplete form-control" data-source="http://localhost:3000/Countries" placeholder="Countries">' +
            '</div>');
    $('#countries').append(items.join(''));
    cntAddCountry++;

    var countries = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 15,
        prefetch: {
            // url points to a json file that contains an array of country names
            url: $("#autocomplete" + cntId).data('source')
            // the json file contains an array of strings, but the Bloodhound
            // suggestion engine expects JavaScript objects so this converts all of
            // those strings
        }
    });

    countries.initialize();
    $("#autocomplete" + cntId).typeahead(null, {
        name: 'countries',
        displayKey: 'name',
        // `ttAdapter` wraps the suggestion engine in an adapter that
        // is compatible with the typeahead jQuery plugin
        source: countries.ttAdapter()
    });
}

function cityAC101() {
    var cities = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 15,
        prefetch: {
            // url points to a json file that contains an array of city names
            url: $("#autocomplete101").data('source')
            // the json file contains an array of strings, but the Bloodhound
            // suggestion engine expects JavaScript objects so this converts all of
            // those strings
        }
    });

    $.ajax({
        url: $("#autocomplete101").data('source'),
        dataType: "json",
        success: function (cities) {
            $("#autocomplete101").autocomplete({
                source: function (request, response) {
                    var results = $.ui.autocomplete.filter(cities, request.term);
                    response(results.slice(0, 10));
                }
            });
        }
    });
}

var cntAddCity = 101;
function addCity(){
    var items = [];
    var cntNum = cntAddCity-99;
    var cntId = cntAddCity+1;
        items.push('<div class="col-md-1 noBreak">' +
            '<h3 class="noBreak">' + cntNum + '</h3>' +
            '</div>' +
            '<div class="btn-group col-md-5 noBreak">' +
            '<input id="autocomplete' + cntId + '" type="text" class="form-control" data-source="http://localhost:3000/Turkey" placeholder="Cities">' +
            '</div>');
    $('#cities').append(items.join(''));
    cntAddCity++;

    var cities = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 15,
        prefetch: {
            // url points to a json file that contains an array of city names
            url: $("#autocomplete" + cntId).data('source')
            // the json file contains an array of strings, but the Bloodhound
            // suggestion engine expects JavaScript objects so this converts all of
            // those strings
        }
    });

    $.ajax({
        url: $("#autocomplete" + cntId).data('source'),
        dataType: "json",
        success: function (cities) {
            $("#autocomplete" + cntId).autocomplete({
                source: function (request, response) {
                    var results = $.ui.autocomplete.filter(cities, request.term);
                    response(results.slice(0, 10));
                }
            });
        }
    });
}

AnyTime.picker( "normDate",
    {
        format: "%e %b %Y %E",
        formatUtcOffset: "%: (%@)",
        placement: "popup",
        baseYear: 2017,
        latest: new Date(2017, 04, 05)
    }
);

AnyTime.picker( "startDate",
    {
        format: "%e %b %Y %E",
        formatUtcOffset: "%: (%@)",
        placement: "popup",
        baseYear: 2017,
        latest: new Date(2017, 04, 05)
    }
);

AnyTime.picker( "endDate",
    {
        format: "%e %b %Y %E",
        formatUtcOffset: "%: (%@)",
        placement: "popup",
        baseYear: 2017,
        latest: new Date(2017, 04, 05)
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