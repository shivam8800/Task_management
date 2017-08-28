$(document).ready(function(){


    //For getting CSRF token
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    var count = 0;
    var dataId;
    $('.reply').click(function(e){
        e.preventDefault();
        dataId = $(this).attr("data-id");
        if (count == 0){
            $("#nested" + dataId).append("<input type='text' id='comment" + dataId +"' style='margin-left: 30px; width: 40%; margin-right: 2%;'><button type='submit' id ='post" + dataId + "' style='padding: 1%;'>post</button>");
            count = count +1
        }
        else{
            $("#nested" + dataId).empty();
            count = 0;
        }
        $("#post"+ dataId).click(function(){

            var inputvalue = $("#comment" + dataId).val();
            var csrftoken = getCookie('csrftoken');
            var comment_id = dataId; 

            if (inputvalue !== "" ){
                $.ajax({
                    url: "/postnestedcomment/",
                    type: "POST",
                    data: {input: inputvalue, csrfmiddlewaretoken: csrftoken, comment_id: comment_id,},
                    success: function(json){
                        console.log("yes I got it");
                        $("#nested" + dataId).empty();
                        $("#nestedcomment" + dataId).append("<li class='NESTED'>" +inputvalue + "</li>");
                    },
                    error: function(err){
                        console.log(err);
                    }
                })
            }
            else{
                console.log("fail");
            }
        })

    });
    $('#hide_member').hide();
    var count=0;
    $('.panel_4').click(function(){
        if (count == 0){
            $('#hide_member').show(1000);
            count = count +1;
        }
        else{
            $('#hide_member').hide(1000);
            count =0;
        }
    })
});