$(function() {
	$('.menu__category').on('click', function() {
        $(this).toggleClass('active');
        $(this).next().toggleClass('collaps');
    });
});