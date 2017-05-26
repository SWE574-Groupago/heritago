 
var heritageId;
var annotations; 

 var myAnnotator = {
    "onSubmit": function(annotation) {
        
        var $element = $(annotation.highlights[0])
        var selected_motivation = $('#add-annotation-on-description-modal-select-motivation').val();
        var given_textual_body =  $("#add-annotation-on-description-modal-textarea").val();
        var given_url = $("#add-annotation-on-description-modal-url").val();

        var targetId = window.location.href.split("#")[0] + "#description";
        var data = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "creator": "osman",
            "motivation": $("#add-annotation-on-description-modal-select-motivation").val(),
            "body": [{
                "type": "text",
                "value": given_textual_body || given_url,
                "format": "text/plain"
            }],
            "target": [{
                "id": targetId,
                "type": "text",
                "format": "text/plain",
                "selector": [{
                    "type": "FragmentSelector",
                    "conformsTo": "http://tools.ietf.org/rfc/rfc5147",
                    "value": "char=" + annotation.ranges[0].startOffset + ", " + annotation.ranges[0].endOffset
                }]
            }]
        };
        
        $.ajax({
            "url": "/api/v1/heritages/" + heritageId + "/annotations",
            "method": "POST",
            "data": JSON.stringify(data),
            "contentType": "application/json",
        }).always(function(response){
            $element.attr("data-annotation-id", response.id)
            annotations.push(response);
            renderAnnotationNumber(annotations.length);
        });

    }
 };


function renderAnnotationNumber(n) {
    $("#heritage-item-total-no-annotations").text(n);
}

 $(function() {
    var annotator;

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

        annotator = $('#heritage-item-description').annotator();

        $('.annotator-adder button').attr( "data-toggle", "modal" );
        $('.annotator-adder button').attr( "data-target", "#add-annotation-on-description-modal" );
        $('.annotator-adder button').attr( "data-backdrop", "static" );
        $('.annotator-adder button').attr( "data-keyboard", "false" );

        $('.annotator-adder button').click(function() {
            $('.annotator-outer.annotator-editor').css('display','none');
            $('#add-annotation-on-description-modal-textarea').val("");
            $('#add-annotation-on-description-modal-url').val("");
            $('#add-annotation-on-description-modal-select-motivation').val("");
            $("#add-annotation-on-description-modal-textarea").attr( "disabled", "disabled" );
            $("#add-annotation-on-description-modal-url").attr( "disabled", "disabled" );
            $("#add-annotation-on-description-modal-text-errors").html("&nbsp;");
        });

         $('#annotate-description-modal-submit-text-but').click(function() {
             $("#add-annotation-on-description-modal-text-errors").html("&nbsp;");
             // Checks if motivation selected
             var selected_motivation = $('#add-annotation-on-description-modal-select-motivation').val();
             var given_textual_body =  $("#add-annotation-on-description-modal-textarea").val();
             var given_url = $("#add-annotation-on-description-modal-url").val();
             if (selected_motivation == "linking" && given_url == "") {
                 // Give error since given URL cannot be empty string
                 $("#add-annotation-on-description-modal-text-errors").html("Given URL cannot be empty string while selected motivation is 'linking'.");
                 return
            }
            else if (selected_motivation == "linking") {
                 // successful, pass
             }
            else if (given_textual_body == "") {
                 // Give error since entered textual body cannot be empty string
                 $("#add-annotation-on-description-modal-text-errors").html("Textual body cannot be empty string while selected motivation is '" + selected_motivation + "'." );
                 return;
             }

            $('.annotator-save').click();
            $('#add-annotation-on-description-modal-close-but').click();

         });


        $('#add-annotation-on-description-modal-select-motivation').on('change', function() {
          $("#add-annotation-on-description-modal-text-errors").html("&nbsp;");
          if (this.value == "") {
              $("#add-annotation-on-description-modal-textarea, #add-annotation-on-description-modal-url").attr( "disabled", "disabled" );
              $("#add-annotation-on-description-modal-textarea, #add-annotation-on-description-modal-url").val( "" );
          } else if (this.value == "linking") {
              // Enable URL field for entry
              $("#add-annotation-on-description-modal-textarea").attr( "disabled", "disabled" );
              $("#add-annotation-on-description-modal-textarea").val( "" );
              $("#add-annotation-on-description-modal-url").removeAttr( "disabled" );
              $("#add-annotation-on-description-modal-url").focus();
          } else {
              // Selected motivation other than linking
              // Enable Textarea field for entry
              $("#add-annotation-on-description-modal-url").attr( "disabled", "disabled" );
              $("#add-annotation-on-description-modal-url").val( "" );
              $("#add-annotation-on-description-modal-textarea").removeAttr( "disabled" );
              $("#add-annotation-on-description-modal-textarea").focus();
          }
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
            init_image_popup($( this ).children('img').attr('src') );

             
        });

        $("#btn-start-annotate").click(function(){
            start_image_annotation();
        })

        $("#btn-cancel-annotate").click(function(){
            stop_image_annotation();
        })


    }

    function init_image_popup(src) {
        // $('#heritage-item-details-add-annotation-on-image-modal-target-image').attr( "src", );
        v = VGG({
          "single_region": true,
          "url": src,
          "canvas_container": document.getElementById("canvas_panel"),
          "onLoaded": function(status) {
            console.log(status);
          },
          "show_message": function(msg, t) {
            console.log(msg)
          },
          "new_region_created": function(region) {
            console.log(region)
          },
          "initialized": function(status) {
            setTimeout(function(){
            v.import_region({
              "0": {
                "shape_attributes": {
                  "name": "polygon",
                  "all_points_x": [
                    119,
                    102,
                    196,
                    406,
                    395,
                    433,
                    413,
                    336,
                    332,
                    247,
                    164,
                    119
                  ],
                  "all_points_y": [
                    175,
                    218,
                    285,
                    288,
                    232,
                    227,
                    140,
                    138,
                    210,
                    182,
                    195,
                    175
                  ]
                },
                "region_attributes": {
                  "name": "Swan",
                  "color": "white"
                }
              }
            });}, 200);
          }
        });
    }

    function start_image_annotation() {
        $("#btn-start-annotate").hide();
        $("#image-region-form").show();

    }
    
    function stop_image_annotation() {
        $("#btn-start-annotate").show();
        $("#image-region-form").hide();
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
    
    function renderAnnotations() {
        for (var i = annotations.length - 1; i >= 0; i--) {
            var a = annotations[i];

            if (a.target[0].target_id == heritageId) {
                if (a.target[0].format == "text/plain") {
                    var position = a.target[0].selector[0].value.split("=")[1].split(",");
                    
                    annotator.annotator("loadAnnotations", [{
                        "id": a.id, // TODO: duzgun bir id
                        "ranges": [
                            {
                              "start": "",
                              "end": "",
                              "startOffset": position[0],
                              "endOffset": position[1]
                            }
                          ]
                    }]);

                }
            }


        }
        renderAnnotationNumber(annotations.length);
    }

    function fetchAnnotations() {
        var url = "/api/v1/heritages/" + heritageId + "/annotations";
        $.getJSON(url, {
            format: "json"
        })
        .fail(function(xhr, status){
            toastr.error("annotations not found");
        })
        .done(function( data ) {
            annotations = data;
            console.log("fetched annotations")
            renderAnnotations();
        });
    }

    function fetch() {
        var url = "/api/v1/heritages/" + heritageId;
        $.getJSON(url, {
            format: "json"
        })
        .fail(function(xhr, status){
            toastr.error("heritage not found");
        })
        .done(function( data ) {
            render(data);
            $("#content").show();
            fetchAnnotations();
        }).always(function(data){
            $("#page-loading").hide();
        });
    }

    heritageId = getParameterByName("id");
    if (!heritageId)
        toastr.error("heritage item id not found in the url");
    else
        fetch(heritageId);


    



 });