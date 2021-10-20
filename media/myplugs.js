
// this is for ajax response

$('span.answer').on('click', function(){
    $(this).animate({
    }, 800, function(){
        $(this).addClass('btn-primary').removeClass('btn-success')
    }).parent().children().addClass('disabled')
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