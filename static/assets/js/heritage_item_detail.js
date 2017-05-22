 $(function() {

    function bind() {
        $('#heritage-item-description-read-more').click(function() {
            var reducedHeight = $('#heritage-item-description').height();
            $('#heritage-item-description').css('height', 'auto');
            var fullHeight = $('#heritage-item-description').height();
            $('#heritage-item-description').height(reducedHeight);
            $('#heritage-item-description').animate({height: fullHeight}, 500);
            $('#heritage-item-description-read-more').attr( "hidden", "true" );
            $('#heritage-item-description-read-less').removeAttr( "hidden" );
        });

        $('#heritage-item-description-read-less').click(function() {
            var fullHeight = $('#heritage-item-description').height();
            $('#heritage-item-description').css('height', '16em', 'overflow', 'hidden');
            var reducedHeight = $('#heritage-item-description').height();
            $('#heritage-item-description').height(fullHeight);
            $('#heritage-item-description').animate({height: reducedHeight}, 500);
            $('#heritage-item-description-read-less').attr( "hidden", "true" );
            $('#heritage-item-description-read-more').removeAttr( "hidden" );
        });

        new Maplace({
            show_markers: true,
            locations: [{
                lat: 41.0054,
                lon: 28.9768,
                zoom: 14
            }]
        }).Load();

        $('#heritage-item-description').annotator();

        $('.annotator-adder button').attr( "data-toggle", "modal" );
        $('.annotator-adder button').attr( "data-target", "#add-annotation-on-description-modal" );
        $('.annotator-adder button').attr( "data-backdrop", "static" );
        $('.annotator-adder button').attr( "data-keyboard", "false" );

        $('.annotator-adder button').click(function() {
            $('.annotator-outer.annotator-editor').css('display','none');
        });

         $('#annotate-description-modal-submit-text-but').click(function() {
             // if textarea is not empty, user can click submit
             console.log("Button, for submitting text annotation, clicked.");
             // if adding annotation is successful, then following lines will be done
             $('.annotator-save').click();
             $('#add-annotation-on-description-modal-close-but').click();
         });

         $('#annotate-description-modal-submit-image-but').click(function() {
             // if uploaded image file is validated, user can click submit
             console.log("Button, for submitting image annotation, clicked.");
             // if adding annotation is successful, then following lines will be done
             $('.annotator-save').click();
             $('#add-annotation-on-description-modal-close-but').click();
         });

         $('#annotate-description-modal-submit-video-but').click(function() {
             // if uploaded video file is validated, user can click submit
             console.log("Button, for submitting video annotation, clicked.");
             // if adding annotation is successful, then following lines will be done
             $('.annotator-save').click();
             $('#add-annotation-on-description-modal-close-but').click();
         });

         $('#annotate-description-modal-submit-audio-but').click(function() {
             // if uploaded audio file is validated, user can click submit
             console.log("Button, for submitting audio annotation, clicked.");
             // if adding annotation is successful, then following lines will be done
             $('.annotator-save').click();
             $('#add-annotation-on-description-modal-close-but').click();
         });

         $('#add-annotation-on-description-modal-cancel-but').click(function() {
             $('.annotator-cancel').click();
         });

         $('#add-annotation-on-description-modal-close-but').click(function() {
             $('.annotator-cancel').click();
         });

         $('.annotator-hl').attr( "data-toggle", "modal" );
         $('.annotator-hl').attr( "data-target", "#display-annotations-on-highlighted-text-modal" );
         $('.annotator-hl').click(function() {
             $('#display-annotations-modal-highlighted-text').text('"' + $(this).text() + '"');
         });



         $('#heritage-item-guide-but').click(function() {
             introJs().start();
         });




    // heritage-item-total-no-annotations
    // heritage-item-title
    // heritage-item-description
    // heritage-item-owner


        $('.heritage-item-details-thumbnail-img-to-expand').click(function() {
             $('#heritage-item-details-add-annotation-on-image-modal-target-image').attr( "src", $( this ).children('img').attr('src') );
         });
    }

    var $title = $("#heritage-item-title");
    var $description = $("#heritage-item-description");
    var $basicInformation = $("#basic-information");
    var $origin = $("#heritage-origin");
    var $images = $("#heritage-images");

    function render(heritage) {
        $title.html(heritage.title);
        $description.html(heritage.description);
        var $basicInformationTemplate = $("template-basic-information")

        var $template = $('#template-basic-information').html();
        Mustache.parse($template);
        var rendered = Mustache.render($template, heritage);
        $basicInformation.html(rendered);


        var $template = $('#template-origin').html();
        Mustache.parse($template);
        var rendered = Mustache.render($template, heritage);
        $origin.html(rendered);

        var $template = $('#template-images').html();
        Mustache.parse($template);
        var images = [];
        for (var i = heritage.multimedia.length - 1; i >= 0; i--) {
            if (heritage.multimedia[i].type == "image")
                images.push(heritage.multimedia[i])
        }
        var rendered = Mustache.render($template, images);
        $images.html(rendered);

        // LOCATION
        for (var i = heritage.multimedia.length - 1; i >= 0; i--) {
            var mm = heritage.multimedia[i];

            if (mm.type == "location") {
                var locationData = JSON.parse(mm.meta);
                console.log(locationData)
                new Maplace({
                    map_div: '#gmap',
                    type: locationData.type,
                    locations: locationData.markers
                }).Load();
            }
        }


        bind();
    }

    function fetch(id) {
        var url = "/api/v1/heritages/" + id;
        $.getJSON(url, {
            format: "json"
        })
        .fail(function(xhr, status){
            toastr.error("heritage not found");
        })
        .done(function( data ) {
            render(data);
            $("#content").show();
        }).always(function(data){
            $("#page-loading").hide();
        });
    }

    var heritageId = getParameterByName("id");
    if (!heritageId)
        toastr.error("heritage item id not found in the url");
    else
        fetch(heritageId);

 });