$(function() {
    $('.product__remove > span').on('click', function(){
        let shoes_id = $(this).parent().attr('data-id');
        let csrf_token = $(this).parent().attr('data-csrf');
        console.log(shoes_id)
        $(this).closest('.product').remove()
        let data = {};
        data.shoes_id = shoes_id;
        data.csrfmiddlewaretoken = csrf_token;
        $.ajax({
            url: '/post_cart_remove',
            type: 'POST',
            data: data,
            success: function(data){
                console.log('OK');
                // location.reload();
            }
        })
    })
})