 $(function() {

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

 });