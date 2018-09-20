$(function() {
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
    let brands;
    let sizes;
    let prices;
    let sorting;
    let urlFilter;



    $('.menu__filter').on('click', filterUrl)


    // funtion 
    function filterUrl(){
        brands = []; sizes = []; prices = []; sorting = []; urlFilter = {};
        //brand
        const brandList = document.querySelectorAll('.menu__brandElement');
        brandList.forEach(el=>{
            if (el.firstElementChild.classList.contains('active')){
                brands.push(el.lastElementChild.innerHTML)  
                // brands = brands.join();
                urlFilter.brand = brands;
            }  
        })
        //sizes
        const sizeList = document.querySelectorAll('.menu__size');
        sizeList.forEach(el=>{
           if (el.classList.contains('active')) {
                sizes.push(el.innerHTML)
                // sizes = sizes.join();
                urlFilter.size = sizes;
           }
        })
        //prices
        const priceList = document.querySelector('.menu__priceBox');
        if (priceList.firstElementChild.value || priceList.lastElementChild.value){
            if (priceList.firstElementChild.value) prices.push(priceList.firstElementChild.value)
            else (prices.push('0'))
            if (priceList.lastElementChild.value) prices.push(priceList.lastElementChild.value)
            else (prices.push('0'))
            prices = prices.join();
            urlFilter.price = prices;
        }
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
        console.log(url)
    }




});