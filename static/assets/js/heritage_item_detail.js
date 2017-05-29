 
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
            "creator": "demouser",
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
            $("#annotation-form-resource-type").val("text");
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
             var resourceType = $("#annotation-form-resource-type").val();

             // Checks if motivation selected
             var selected_motivation = $('#add-annotation-on-description-modal-select-motivation').val();
             var given_textual_body =  $("#add-annotation-on-description-modal-textarea").val();
             var given_url = $("#add-annotation-on-description-modal-url").val();

             if (selected_motivation == "linking") {
                if (given_url == "") {
                    // Give error since given URL cannot be empty string
                    $("#add-annotation-on-description-modal-text-errors").html("Given URL cannot be empty string while selected motivation is 'linking'.");
                     return
                }
            }
            else if (given_textual_body == "") {
                 // Give error since entered textual body cannot be empty string
                 $("#add-annotation-on-description-modal-text-errors").html("Textual body cannot be empty string while selected motivation is '" + selected_motivation + "'." );
                 return;
            }

            if (resourceType == "text") {
                $('.annotator-save').click();
                $('#add-annotation-on-description-modal-close-but').click();
            } else {
                var targetId = $("#image-target-id").val();
                submit_image_annotation_form(targetId, selected_motivation, given_textual_body, given_url, function(response){
                    stop_image_annotation();
                    show_image_annotations();
                    $('#add-annotation-on-description-modal-close-but').click();
                });
            }

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
         var $displayDescriptionAnnotationModalDescriptionAnnotations = $("#display-text-annotations-on-highlighted-text-tab");
         var $templateDisplayTextAnnotation = $('#template-display-text-annotations-on-highlighted-text-tab').html();
         $('.annotator-hl').click(function() {
             $('#display-annotations-modal-highlighted-text').text('"' + $(this).text() + '"');
             var selected_highlighted_text_id = parseInt($(this).attr("data-annotation-id").split("annotations/")[1]);
             console.log(selected_highlighted_text_id);
             var selected_highlighted_text_url = "/api/v1/heritages/" + heritageId + "/annotations/" + selected_highlighted_text_id;
              $.getJSON(selected_highlighted_text_url)
              .fail(function(xhr, status){
                  toastr.error("annotation not found");
              })
              .done(function( response ) {
                  console.log("annotation response for highlighted text");
                  console.log(response);
                  Mustache.parse($templateDisplayTextAnnotation);
                  var rendered = Mustache.render($templateDisplayTextAnnotation, response);
                  $displayDescriptionAnnotationModalDescriptionAnnotations.html(rendered);
              });


         });

         var $allAnnotationsModalDescriptionAnnotations = $("#all-annotations-modal-description-tab");
         var $templateDisplayAllAnnotationsOnDescription = $('#template-all-annotations-modal-description-tab').html();
         $('#heritage-item-all-annotations').click(function() {
             $('#all-annotations-on-heritage-item-modal-item-title').text($('#heritage-item-title').text());
             Mustache.parse($templateDisplayAllAnnotationsOnDescription);
             var filteredAnnotations = filterAnnotations("text");
             var rendered = Mustache.render($templateDisplayAllAnnotationsOnDescription, filteredAnnotations);
             $allAnnotationsModalDescriptionAnnotations.html(rendered);
         });

        var $allAnnotationsModalImageAnnotations = $("#all-annotations-modal-image-tab");
        var $templateDisplayAllAnnotationsOnImage = $('#template-all-annotations-modal-image-tab').html();
        $('#all-annotations-modal-image-tab-button').click(function() {
             Mustache.parse($templateDisplayAllAnnotationsOnImage);
             var filteredAnnotations = filterAnnotations("image");
             var rendered = Mustache.render($templateDisplayAllAnnotationsOnImage, filteredAnnotations);
             $allAnnotationsModalImageAnnotations.html(rendered);
         });


        $('.heritage-item-details-thumbnail-img-to-expand').click(function() {
            init_image_popup($(this).children('img').attr('src'));
        });

        $("#btn-start-annotate").click(function(){
            start_image_annotation();
        })

        $("#btn-cancel-annotate").click(function(){
            stop_image_annotation();
            show_image_annotations();
        })

        $("#btn-continue-annotate").click(function(){
            show_image_annotation_form();
        })

         $('#heritage-item-guide-but').click(function() {
             introJs().start();
         });


    }

    function filterAnnotations(type) {
       var filteredAnnotationsList = [];
          for(var i = 0; i < annotations.length; i++){
            if (annotations[i].target[0].type == type) {
               filteredAnnotationsList.push(annotations[i]);
            }
        }
        console.log(filteredAnnotationsList);
        return filteredAnnotationsList;

    }

    var $imageExpandedModalImageAnnotations = $("#heritage-item-details-add-annotation-on-image-annotations");
    var $templateDisplayImageAnnotationOnExpandedModal = $('#template-heritage-item-details-add-annotation-on-image-annotations').html();
    function init_image_popup(src) {
        // $('#heritage-item-details-add-annotation-on-image-modal-target-image').attr( "src", );
        $("#image-target-id").val(src);
        v = VGG({
          "single_region": false,
          "url": src,
          "canvas_container": document.getElementById("canvas_panel"),
          "onLoaded": function(status) {
            
          },
          "show_message": function(msg, t) {
            
          },
          "new_region_created": function(region) {
            console.log(region)
          },
          "initialized": function(status) {
            show_image_annotations();
          }
        });
        Mustache.parse($templateDisplayImageAnnotationOnExpandedModal);
        var filteredAnnotations = filterAnnotations("image");
        var rendered = Mustache.render($templateDisplayImageAnnotationOnExpandedModal, filteredAnnotations);
        $imageExpandedModalImageAnnotations.html(rendered);
    }

    function start_image_annotation() {
        $("#btn-start-annotate").hide();
        $("#image-region-form").show();
        v.clearRegions();
    }
    
    function stop_image_annotation() {
        $("#btn-start-annotate").show();
        $("#image-region-form").hide();
    }
    
    function show_image_annotation_form() {
        $("#annotation-form-resource-type").val("image");
    }
    function show_image_annotations() {
        

        setTimeout(function(){

            var regions = {};
            var region_id = 0;
            for (var i = annotations.length - 1; i >= 0; i--) {
                var a = annotations[i];
                if (a.target[0].type == "image") {
                    var annotation_regions = JSON.parse(a.target[0].selector[0].value);
                    for (var j = annotation_regions.length - 1; j >= 0; j--) {
                        regions[region_id] = {"shape_attributes": annotation_regions[j], "region_attributes": {}};
                        region_id++;
                    }
                }
            }
            v.setRegions([]);
            console.log(regions);
            v.import_region(regions);
        }, 400);
    }

    function submit_image_annotation_form(targetId, selected_motivation, given_textual_body, given_url, callback) {
        var regions = [];
        for(var i = 0; i < v.getRegions().length; i++) {
             regions.push(JSON.parse(v.map_to_json(v.getRegions()[i].shape_attributes)));
        }

        var data = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "creator": "demouser",
            "motivation": selected_motivation,
            "body": [{
                "type": "text",
                "value": given_textual_body || given_url,
                "format": "text/plain"
            }],
            "target": [{
                "id": targetId,
                "type": "image",
                "format": "image/jpeg",
                "selector": [{
                    "type": "FragmentSelector",
                    "conformsTo": "http://tools.ietf.org/rfc/rfc5147",
                    "value": JSON.stringify(regions)
                }]
            }]
        };
        
        $.ajax({
            "url": "/api/v1/heritages/" + heritageId + "/annotations",
            "method": "POST",
            async: false,
            "data": JSON.stringify(data),
            "contentType": "application/json",
        }).always(function(response){
            callback(response);
            annotations.push(response);
            renderAnnotationNumber(annotations.length);
        });
    }

    var $title = $("#heritage-item-title");
    var $description = $("#heritage-item-description");
    var $basicInformation = $("#basic-information");
    var $origin = $("#heritage-origin");
    var $images = $("#heritage-images");
    var $startDate = $("#heritage-item-start-date");
    var $endDate = $("#heritage-item-end-date");
    var $exactDate = $("#heritage-item-exact-date");

    function render(heritage) {
        $title.html(heritage.title);
        $description.html(heritage.description);
        console.log(heritage);
        $startDate.html(heritage.startDate);
        $endDate.html(heritage.endDate);
        $exactDate.html(heritage.exactDate);
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

                if (a.target[0].format == "text/plain") {
                    var position = a.target[0].selector[0].value.split("=")[1].split(",");
                    
                    annotator.annotator("loadAnnotations", [{
                        "id": a.id, 
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
            annotations = [];
            for (var i = 0; i<data.length; i++) {
                if ((((data[i].target[0].target_id).split("heritages/")[1]).split("/annotations")[0]) == heritageId) {
                    annotations.push(data[i]);
                }

            }

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
            console.log(data);
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