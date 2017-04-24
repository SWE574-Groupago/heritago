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


    });