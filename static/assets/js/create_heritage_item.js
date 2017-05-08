$(function() {

    new Maplace({
        show_markers: true,
        map_div: '#create_new_heritage_item_gmap',
        type: 'marker',
        locations: [{
            lat: 38.9637,
            lon: 35.2433,
            zoom: 4,
            draggable: true
        }],
        dragEnd: function(index, location, marker) {
            //alert("Latitude: " + parseFloat(marker.position.lat()).toFixed(4) + ", Longitude: " + parseFloat(marker.position.lng()).toFixed(4));
            $( "#create_new_heritage_item_lat" ).text(parseFloat(marker.position.lat()).toFixed(4));
            $( "#create_new_heritage_item_lon" ).text(parseFloat(marker.position.lng()).toFixed(4));
        }
    }).Load();

    $( "#create_new_heritage_item_clear_coord_but" ).click(function() {
        $( "#create_new_heritage_item_lat" ).text("");
        $( "#create_new_heritage_item_lon" ).text("");
    });


    AnyTime.picker( "create_new_heritage_item_start_date",
        {
            format: "%e %b %Y %E",
            formatUtcOffset: "%: (%@)",
            placement: "popup",
            latest: new Date()
        }
    );

    AnyTime.picker( "create_new_heritage_item_end_date",
        {
            format: "%e %b %Y %E",
            formatUtcOffset: "%: (%@)",
            placement: "popup",
            latest: new Date()
        }
    );

    AnyTime.picker( "create_new_heritage_item_exact_date",
        {
            format: "%e %b %Y %E",
            formatUtcOffset: "%: (%@)",
            placement: "popup",
            latest: new Date()
        }
    );

    $( "#create_new_heritage_item_clear_start_date_but" ).click(function() {
        $( "#create_new_heritage_item_start_date" ).val("");
    });
    $( "#create_new_heritage_item_clear_end_date_but" ).click(function() {
        $( "#create_new_heritage_item_end_date" ).val("");
    });
    $( "#create_new_heritage_item_clear_exact_date_but" ).click(function() {
        $( "#create_new_heritage_item_exact_date" ).val("");
    });

});








