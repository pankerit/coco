$(function(){
    $('#header-slider').owlCarousel({
        loop:true,
        items:1,
        smartSpeed: 500,

        animateOut: 'fadeOut',
        animateIn: 'fadeIn',


        // responsive:{
        //     0:{
        //         items:1
        //     },
        //     600:{
        //         items:3
        //     },
        //     1000:{
        //         items:7
        //     }
        // }
    });

    // clone owl dot to slider dot
    $('.owl-dots button').each(function() {
      $('.slider__dots').append('<div class="slider__dot"></div>'); 
    });
    $('.slider__dot:eq(0)').addClass('active');
    $('.slider__dots-line').css('width', $('.slider__dots').width());


    $('#header-slider').on('changed.owl.carousel', function(event) {
        // console.log('1');
        $('.slider__dot').removeClass('active');
        $('.owl-dots button').each(function(index) {
            if ($(this).hasClass("active")) {
                 $('.slider__dot:eq('+index+')').addClass('active');

            }
        });
    });
    // cand apasa pe slider dot automat sa apese pe owl-dow
    $('.slider__dot').on('click', function() {
        var i = $(this).index();
        $('.owl-dot:eq('+i+')').click();
    });

    // on drag animation fade

});


