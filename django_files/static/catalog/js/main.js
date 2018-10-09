$(function() {
	$('.menu__category').on('click', function() {
        $(this).toggleClass('active');
        // $(this).next().toggleClass('collaps');
    });
    $('.menu__brandCheckBox').on('click', function() {
        $(this).toggleClass('active');
    });

    $('.menu__size').on('click', function() {
        $(this).toggleClass('active');
    });

    //pagination
    const active_page = $('.page.active');
    const pages = $('.pages .page');
    const arrow_prev = $('.pagination__arrow.prev');
    const arrow_next = $('.pagination__arrow.next');
    arrow_prev.on('click',()=>pager(pages, 'prev'))
    arrow_next.on('click',()=>pager(pages, 'next'))
    setPages(active_page);
    //pagination

    let sizes, sorting, urlFilter, page;


    // go to next page
    $('.pages .page').on('click', function(){
        page = $(this).text();
        filterUrl(page);
    })

    $('.menu__filter').on('click', ()=>filterUrl(page))


    // funtion 
    function filterUrl(page=$('.pages .page.active').text()){
        brands = []; sizes = []; sorting = []; urlFilter = {};
        //page
        urlFilter.page = page;
        // brand
        const brandList = document.querySelectorAll('.menu__brandElement');
        brandList.forEach(el=>{
            if (el.firstElementChild.classList.contains('active')){
                brands.push(el.lastElementChild.innerHTML)  
                urlFilter.brand = brands;
            }  
        })
         
        //sizes
        const sizeList = document.querySelectorAll('.menu__size');
        sizeList.forEach(el=>{
           if (el.classList.contains('active')) {
                sizes.push(el.innerHTML)
                urlFilter.size = sizes;
           }
        })
        //prices
        if ($('.menu__price').first().val()) urlFilter.minPrice = $('.menu__price').first().val()
        if ($('.menu__price').last().val()) urlFilter.maxPrice = $('.menu__price').last().val()

        // return encodeQueryData(urlFilter)
        return encodeQueryData(urlFilter)
    }
    // functia e luate de pe net, din object data formeaza url
    function encodeQueryData(data) {
        let ret = [];
        for (let d in data)
          ret.push(d + '=' + encodeURIComponent(data[d]));
        return createUrl(ret.join('&'));
    }
    function createUrl(data){
        let url = window.location.href;
        url = url.split('?')[0]
        url = url+'?'+data
        location.href = url
    }

    // test
    $('.tool__hideSidebar').on('click', ()=>{
        if ($('.menu__category.active').data('type')) console.log($('.menu__category.active').data('type'))
    })


});

//pagination
function setPages(active_page){
    active_page.addClass('show');
    let next, prev;
    let show_prev_length = active_page.prevAll().filter('.page').slice(0,3).length;
    let show_next_length = active_page.nextAll().filter('.page').slice(0,3).length;

    show_prev_length===0 ? next = 6 : show_prev_length===1 ? next = 5 : show_prev_length===2 ? next = 4 : next=3
    show_next_length===0 ? prev = 6 : show_next_length===1 ? prev = 5 : show_next_length===2 ? prev = 4 : prev=3

    active_page.nextAll().filter('.page').slice(0,next).addClass('show');
    active_page.prevAll().filter('.page').slice(0,prev).addClass('show');

}
function pager(pages, direction){
    let pages_show = $('.page.show');
    if(direction === 'next'){
        if (pages_show.last().index() !== pages.length-1){
            pages_show.first().removeClass('show');
            pages_show.next().addClass('show');
        }
    }
    else{
        if (pages_show.first().index() !== 0){
            pages_show.last().removeClass('show');
            pages_show.prev().addClass('show');
        }
    }
}
//pagination