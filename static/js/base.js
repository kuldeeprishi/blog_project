$(document).ready(function(){
        $('.addcomment').attr('disabled','disabled');


        $(".addcomment").click(function(e){


         var post_id = this.id ;
         var comment = $("#id_comment").val();

        $.ajax({
                type: "POST",
                url: "/blog/detail/"+post_id+"/",
                data: {'comment':comment} ,
                success: function(data){
                        $( ".comentbody div:last" ).after( "<div>"+data+"</div>" );
                        //  $("#bodyContent").html(data);
                        },

                });

        $("#id_comment").val('');

        });
        $('#id_comment').keypress(function(e){
                $('.addcomment').attr('disabled',false);
                 if(e.which == 13){
            $(".addcomment").click();//Trigger search button click event
            e.preventDefault();
        }
         });
});