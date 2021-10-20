
// this is for ajax response

$('span.answer').on('click', function(){
    $(this).parent().hide()
    $user = $(this).data('user')
    $id = $(this).data('id')
    $quiz = $(this).data('quiz')
    $.ajax({
        url:'/answer/',
        type:'get',
        data:{
            'user':$user,
            'id':$id,
            'quiz':$quiz,
        },
        success:function(response){
            
        }
    })
})