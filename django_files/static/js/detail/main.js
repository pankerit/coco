$(function(){
    $('.slider__img').on('mouseover', function() {
        $('.slider__img').removeClass('active');
        $(this).addClass('active');
        var img = $(this).attr('style');
        $('.product__image .img').attr("style", img);
    })
    // views 360
    $('.product__360').on('click', ()=>{
        $('#popup-360').addClass('active');
    })
    $('.popup-360__close').on('click', ()=>{
        $('#popup-360').removeClass('active');
    })
    // size active 
    let product__pick_one_size = $('.product__pick-one-size')
    product__pick_one_size.on('click', function(){
        product__pick_one_size.removeClass('active');
        $(this).addClass('active');
    })
    // slider 
    const images = $('.slider__img');
    const arrow_down = $('.slider__arrow--down');
    const arrow_up = $('.slider__arrow--up')
    setSlider(images, arrow_down);
    arrow_down.on('click', ()=>slide(images, arrow_down, arrow_up, 'down'))
    arrow_up.on('click', ()=>slide(images,  arrow_down, arrow_up, 'up'))
    //slider
    //ajax post_cart
    $('.product__addToCart').on('click',()=>{
        let shoes_id = $('.product__info').attr('data-id')
        let size = $('.product__pick-one-size.active').html()
        let csrf_token = $('.product__info > input[name="csrfmiddlewaretoken"]').val();
        let data = {};
        data.shoes_id = shoes_id;
        data.size = size;
        data.csrfmiddlewaretoken = csrf_token;
        $.ajax({
            url: '/post_cart',
            type: 'POST',
            data: data,
            success: function(data){
                console.log('OK');
                // location.reload();
            }
        })

    })
    //ajax post_cart
})
//ajax post_cart
//ajax post_cart


//slider
function setSlider(images, arrow_down){
    if (images.length > 4) {
        arrow_down.css('display','block');
    }    
    images.slice(0,4).addClass('show'); 
}
function slide(images, arrow_down, arrow_up, direction){
    let images_show = $('.slider__img.show')
    if(direction === 'down'){
        arrow_up.css('display','block');
        if (images_show.last().index() === images.length - 1) arrow_down.css('display','none');
        images_show.first().removeClass('show');
        images_show.next().addClass('show');
    }
    else{
        arrow_down.css('display','block');
        if (images_show.first().index() === 2) arrow_up.css('display','none');
        images_show.last().removeClass('show');
        images_show.prev().addClass('show');
    }
}
//slider