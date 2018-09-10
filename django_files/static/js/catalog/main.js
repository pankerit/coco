$(function() {
    // const next = $('.pagination__arrow.next')
    // const prev = $('.pagination__arrow.prev')
    // const showPages = 7;
	$('.menu__category').on('click', function() {
        $(this).toggleClass('active');
        $(this).next().toggleClass('collaps');
    });
    $('.menu__brandCheckBox').on('click', function() {
        $(this).toggleClass('active');
    });

    $('.menu__size').on('click', function() {
        $(this).toggleClass('active');
    });

    

    // const productsNum = 2001;
    // const numPerpage = 100; 
    // renderPages(300, 100);
    // show(showPages)


    // // on click next go next
    // next.on('click', function() {
    //     let position = $('.page.show').last().index();
    //     let i = $('.page').last().index()
    //     if (position !== i){
    //         $('.page.show').first().removeClass('show');
    //         $('.page').slice(position+1, position+2).addClass('show');
    //     } 
        
    // })
    // // on click prex go prev
    // prev.on('click', function() {
    //     let position = $('.page.show').first().index();
    //     let i = $('.page').first().index()
    //     if(position !== i){
    //         $('.page.show').last().removeClass('show');
    //         $('.page').each(function(index){
    //             if ($(this).hasClass('show')){
    //                 $('.page').eq(index-1).addClass('show')
    //                 return
    //             } 
    //         })
    //     }    
    // })



    // function renderPages(num, numPerPage){
    //     pages = Math.ceil(num/numPerPage);
    //     for (var i = 0; i < pages; ++i)
    //     $('.pages').append(`<li class="page">${i+1}</li>`)

    // }

    // function show(firstPages){
    //     // show first ten elements
    //     for (var i = 0; i < firstPages; ++i) {
    //         $('.page:eq('+i+')').addClass('show');
    //     }
          
    // }

    // // pagination active
    // $('.page').on('click', function(){
    //     $('.page').removeClass('active');
    //     $(this).addClass('active');
    // })



});