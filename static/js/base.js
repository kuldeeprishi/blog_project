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
    e.preventDefault();
    var post_id = this.id;
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


$("#submit-button").click(function(e){

    var email_field = $('#id_email_field').val();
    
    $('#id_email_field').fadeOut(1000);

    $.ajax({
        type: "POST",
        url: "/subscribe/",
        data: {'email_field': email_field},
        success: function(data){
              
            if(data==""){
             $(".errormsg").text('plaese enter a valid email id ');
            $(".errormsg").fadeIn(2000).fadeOut("1000");
           
           
           
        }
            else{
                $(".errormsg").text('Thanks for subcription');
                 $(".errormsg").fadeIn(2000).fadeOut("1000");
            }
        },
    })
    $('#id_email_field').val("");
    $('#id_email_field').fadeIn(1000);

    e.preventDefault();
});


});


