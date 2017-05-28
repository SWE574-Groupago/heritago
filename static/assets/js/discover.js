(function() {
	
    var itemsJSON = "/api/v1/heritages?keyword=";
    
    function bind() {
        $("#search-form button").click(start_search);
        $("#search-form form").submit(start_search); 
    }

    function start_search(e) {
        e.preventDefault();
        load($("#searchInput").val());
    }

    function load(keyword) {
        $.ajax({
            url: itemsJSON + keyword,
            format: "json"
        }).done(function( data ) {
            var items = [];
            var cnt = 0;
            $.each(data, function (key, item) {


                if (item.multimedia.length > 0 ) {
                    for (var i = item.multimedia.length - 1; i >= 0; i--) {
                        if (item.multimedia[i].type == "image") {
                            var preview = item.multimedia[i].url;        
                            break;
                        }
                    }
                    
                }
                else
                    var preview = "placeholder.png";

                items.push('<div class="col-md-4">' +
                    '<a href="heritage.html?id='+item.id+'">' +
                    
                    '<div class="card-head style-primary">' +
                    '<header>' + item.title + '</header>' +
                    '</div>' +
                    '<div id="card0" class="thumbnail">' +
                    '<div class="nopadding">' +
                    '<img src="/api/v1' + preview + '" alt="preview" class="bordered imgimg center-block">' +
                    '</div>' +
                    '<div class="card-body scrollDesc">' + item.description + '</div>' +
                    '</div>' +
                    '</a>' +
                    '</div>');
                cnt++;

            });

            $('#heritages').html(items.join(''));
        });
    }
    
    bind();

    load("santa");

})();


