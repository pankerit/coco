$(() =>{
    const next = $('.pagination__arrow.next')
    const prev = $('.pagination__arrow.prev')
    const showPages = 7;
    // get data from server
    const json = getJson().responseJSON;
    const productsNum = json.length;
    const numPerpage = 100; 
    viewOnPage(getDataFromPage(json))

    
     

    // all about pages shown
    renderPages(productsNum, numPerpage);
    show(showPages)
    // on click next go next
    next.on('click', function() {
        let position = $('.page.show').last().index();
        let i = $('.page').last().index()
        if (position !== i){
            $('.page.show').first().removeClass('show');
            $('.page').slice(position+1, position+2).addClass('show');
        }
        
    })
    // on click prex go prev
    prev.on('click', function() {
        let position = $('.page.show').first().index();
        let i = $('.page').first().index()
        if(position !== i){
            $('.page.show').last().removeClass('show');
            $('.page').each(function(index){
                if ($(this).hasClass('show')){
                    $('.page').eq(index-1).addClass('show')
                    return
                } 
            })
        }    
    })
    // pagination active
    $('.page').on('click', function(){
        $('.page').removeClass('active');
        $(this).addClass('active');
        viewOnPage(getDataFromPage(json, $(this).html(), numPerpage))
    })

    // all about pages shown end //









    // console.log(filter(json))
})




function filter(shoes_list){
    a = shoes_list.sort(function (a, b) {
        return a.price - b.price;
      });
    return a;
}



    
function viewOnPage(shoes_list){
    let output = '';
    $.each(shoes_list, (index, shoes) => {
        output += `
            <div class="productBox">
                <div class="productBox__img" style="background-image: url(${shoes.image})">
                    <div class="like">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M349.6 64c-36.4 0-70.7 16.7-93.6 43.9C233.1 80.7 198.8 64 162.4 64 97.9 64 48 114.2 48 179.1c0 79.5 70.7 143.3 177.8 241.7L256 448l30.2-27.2C393.3 322.4 464 258.6 464 179.1 464 114.2 414.1 64 349.6 64zm-80.8 329.3l-4.2 3.9-8.6 7.8-8.6-7.8-4.2-3.9c-50.4-46.3-94-86.3-122.7-122-28-34.7-40.4-63.1-40.4-92.2 0-22.9 8.4-43.9 23.7-59.3 15.2-15.4 36-23.8 58.6-23.8 26.1 0 52 12.2 69.1 32.5l24.5 29.1 24.5-29.1c17.1-20.4 43-32.5 69.1-32.5 22.6 0 43.4 8.4 58.7 23.8 15.3 15.4 23.7 36.5 23.7 59.3 0 29-12.5 57.5-40.4 92.2-28.8 35.7-72.3 75.7-122.8 122z"/></svg>
                    </div>
                    <div class="addToCart">Add to cart</div>
                    <div class="new"></div>
                </div>
                <div class="productBox__name">${shoes.name}</div>
                <div class="productBox__price">$${shoes.price}</div>
            </div>
        `;
    })
    $('.row .products').html(output);

} 




function getJson() {
    return $.ajax({
        url: 'http://127.0.0.1:8000/shoes/api/shoes/',
        async:false,
        success: function(data) {
            return data;
        }
    });
}

function getDataFromPage(json, page = 1, resPerPage = 100){
    const start = (page-1)*resPerPage;
    const end = page*resPerPage;
    return json.slice(start, end);
}


// all about pages
function renderPages(num, numPerPage){
        pages = Math.ceil(num/numPerPage);
        for (var i = 0; i < pages; ++i)
        $('.pages').append(`<li class="page">${i+1}</li>`)
    
    }
    
    function show(firstPages){
        // show first ten elements
        for (var i = 0; i < firstPages; ++i) {
            $('.page:eq('+i+')').addClass('show');
        }
          
    }
// end all about pages //