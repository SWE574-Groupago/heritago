$(function() {

    var geo_location_pin_map = new Maplace({
        map_div: '#create_new_heritage_item_pin_gmap',
        type: 'marker',
        locations: [{
            lat: 38.9637,
            lon: 35.2433,
            draggable: true,
            zoom: 5
        }]
    }).Load();

    var geo_location_circle_map = new Maplace({
        map_div: '#create_new_heritage_item_circle_gmap',
        type: 'circle',
        locations: [{
            lat: 38.9637,
            lon: 35.2433,
            circle_options: {
                radius: 150000,
                editable: true
            },
            zoom: 5,
            draggable: true
        }]
    }).Load();

    var geo_location_polygon_map = new Maplace({
        map_div: '#create_new_heritage_item_polygon_gmap',
        type: 'polygon',
        locations: [{
            lat: 39.5,
            lon: 32.2433,
            draggable: true,
            zoom: 5
        },
        {
            lat: 39.5,
            lon: 38.2433,
            draggable: true,
            zoom: 5
        },
        {
            lat: 38,
            lon: 35.2433,
            draggable: true,
            zoom: 5
        }]
    }).Load();

    var geo_location_polyline_map = new Maplace({
        map_div: '#create_new_heritage_item_path_polyline_gmap',
        type: 'polyline',
        locations: [{
            lat: 37,
            lon: 31,
            draggable: true,
            zoom: 5
        },
        {
            lat: 39.5,
            lon: 33,
            draggable: true,
            zoom: 5
        },
        {
            lat: 41,
            lon: 34,
            draggable: true,
            zoom: 5
        },
        {
            lat: 37,
            lon: 36,
            draggable: true,
            zoom: 5
        },
        {
            lat: 40,
            lon: 38,
            draggable: true,
            zoom: 5
        },
        {
            lat: 38.9637,
            lon: 40,
            draggable: true,
            zoom: 5
        }]
    }).Load();



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

    $( "#create_new_heritage_item_select_map_type" ).change(function() {
        var selected_map_type = $( "#create_new_heritage_item_select_map_type" ).val();
        if (selected_map_type == "not-selected") {
            $( ".create_new_heritage_item_map_container" ).css( "display", "none" );
        }
        if (selected_map_type == "pin") {
            $( ".create_new_heritage_item_map_container" ).css( "display", "none" );
            $( "#create_new_heritage_item_pin_gmap_container" ).css( "display", "inline" );
        }
        if (selected_map_type == "circle") {
            $( ".create_new_heritage_item_map_container" ).css( "display", "none" );
            $( "#create_new_heritage_item_circle_gmap_container" ).css( "display", "" );
        }
        if (selected_map_type == "polygon") {
            $( ".create_new_heritage_item_map_container" ).css( "display", "none" );
            $( "#create_new_heritage_item_polygon_gmap_container" ).css( "display", "" );
        }
        if (selected_map_type == "path-polyline") {
            $( ".create_new_heritage_item_map_container" ).css( "display", "none" );
            $( "#create_new_heritage_item_polyline_gmap_container" ).css( "display", "" );
        }
    });


    $('body').on('click', '.add-free-origin-field-but', function() {
        var free_origin_field_value = $(this).parent().prev().children().eq(0).children().eq(0).val();

        if (free_origin_field_value == "") {

        }
        else {
            $(this).parent().prev().children().eq(0).children().eq(0).prop('disabled', true);
            $(this).parent().prev().children().eq(0).children().eq(1).text("");
            $(this).removeClass( "add-free-origin-field-but" ).addClass("remove-free-origin-field-but").addClass("btn-danger");
            $(this).children().eq(0).removeClass( "fa-plus" ).addClass("fa-minus");
            $(this).parent().parent().after("<div class=\"col-md-12\"><div class=\"col-md-11\">"+
                "<div class=\"form-group floating-label\">"+
                "<input type=\"text\" class=\"form-control create_new_heritage_item_free_origin\">"+
                "<label>Origin (free-text field)</label>"+
                "</div>"+
                "</div>"+
                "<div class=\"col-md-1\">"+
                "<button type=\"button\" class=\"btn ink-reaction btn-floating-action btn-primary add-free-origin-field-but\"><i class=\"fa fa-plus\"></i></button>"+
                "</div></div>");
        }

    });

    $('body').on('click', '.remove-free-origin-field-but', function() {
        $(this).parent().parent().remove();
    });

    $('body').on('click', '.add-key-value-field-but', function() {
        var key_field_input = $(this).parent().prev().prev().prev().children().eq(0).children().eq(0).val();
        var value_field_input = $(this).parent().prev().children().eq(0).children().eq(0).val();

        if (key_field_input == "" || value_field_input == "") {

        }
        else {
            $(this).parent().prev().prev().prev().children().eq(0).children().eq(0).prop('disabled', true);
            $(this).parent().prev().prev().prev().children().eq(0).children().eq(1).text("");
            $(this).parent().prev().children().eq(0).children().eq(0).prop('disabled', true);
            $(this).parent().prev().children().eq(0).children().eq(1).text("");
            $(this).removeClass( "add-key-value-field-but" ).addClass("remove-key-value-field-but").addClass("btn-danger");
            $(this).children().eq(0).removeClass( "fa-plus" ).addClass("fa-minus");
            $(this).parent().parent().after("<div class=\"col-md-12\">"+
                "<div class=\"col-md-5\">"+
                "<div class=\"form-group floating-label\">"+
                "<input type=\"text\" class=\"form-control\">"+
                "<label>key</label>"+
                "</div>"+
                "</div>"+
                "<div class=\"col-md-1\">"+
                "&nbsp;"+
                "</div>"+
                "<div class=\"col-md-5\">"+
                "<div class=\"form-group floating-label\">"+
                "<input type=\"text\" class=\"form-control\">"+
                "<label>value</label>"+
                "</div>"+
                "</div>"+
                "<div class=\"col-md-1\">"+
                "<button type=\"button\" class=\"btn ink-reaction btn-floating-action btn-primary add-key-value-field-but\"><i class=\"fa fa-plus\"></i></button>"+
                "</div>"+
                "</div>");
        }


    });

    $('body').on('click', '.remove-key-value-field-but', function() {
        $(this).parent().parent().remove();
    });

    var timeout_for_create_heritage_item_title_input;
    $("#create_new_heritage_item_title").keypress(function(e) {
        if (timeout_for_create_heritage_item_title_input) {clearTimeout(timeout_for_create_heritage_item_title_input);}
        timeout_for_create_heritage_item_title_input = setTimeout(function () {
            $("#create_new_heritage_item_errors").html("");
        }, 150);
    });

    var timeout_for_create_heritage_item_description_input;
    $("#create_new_heritage_item_description").keypress(function(e) {
        if (timeout_for_create_heritage_item_description_input) {clearTimeout(timeout_for_create_heritage_item_description_input);}
        timeout_for_create_heritage_item_description_input = setTimeout(function () {
            $("#create_new_heritage_item_errors").html("");
        }, 150);
    });

    $( "#create_new_heritage_item_create_but" ).click(function() {
        console.log("Pin type map");
        console.dir(geo_location_pin_map);
        console.log("Circle type map");
        console.dir(geo_location_circle_map);
        console.log("Polygon type map");
        console.dir(geo_location_polygon_map);
        console.log(geo_location_polygon_map.markers[0].position.lat());
        console.log(geo_location_polygon_map.markers[0].position.lng());

        var title_input = $( "#create_new_heritage_item_title" ).val();
        var description_input = $( "#create_new_heritage_item_title" ).val();

        if (title_input == "" || description_input == "") {
            $( "#create_new_heritage_item_errors" ).html("<b>You should provide a title and a description while submitting a new heritage item.</b>");
        }
        else {
            // submit form here
        }
    });






});








