$(document).ready(function(){

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
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

jQuery.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

 
$(".addcomment").click(function(e){
    var post_id = $(this).attr("name");
    alert(post_id);
    var comment = $("#id_comment").val(); 
    $("#id_comment").val('');
    $.ajax({
            type: "POST",
            url: "/blog/add_comment/"+post_id+"/",
            data: {'comment':comment} ,
            success: function(data){
                    // alert(data);
                    $( ".commentbody li:last" ).after( "<li>"+data+"</li>" );
                    },

    });
});
$('#id_comment').keypress(function(e){
	$('.addcomment').attr('disabled',false);
   		 if(e.which == 13){
        $(".addcomment").click();//Trigger search button click event
        e.preventDefault();
    }
     });


// $('#id_q').keypress(function(e){
    
//             var data =$(this).val()
//             if(e.which == 13){


//             if(data == ""){
                
//              e.preventDefault();
//        }
//     }
//      });



});
