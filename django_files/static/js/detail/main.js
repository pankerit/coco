$(function(){
    $('.slider__img').on('mouseover', function() {
        $('.slider__img').removeClass('active');
        $(this).addClass('active');
        var img = $(this).attr('style');
        $('.product__image .img').attr("style", img);
    })
    $('.product__360').on('click', ()=>{
        $('#popup-360').addClass('active');
    })
    $('.popup-360__close').on('click', ()=>{
        $('#popup-360').removeClass('active');
    })
})