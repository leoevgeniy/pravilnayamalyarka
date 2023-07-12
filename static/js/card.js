$('.weight-select-button').on("click touchend", function (event) {
    event.preventDefault();
    $(this).parent().prev()[0].innerText = $(this).data('price') + 'р.'
    $(this).parent().next()[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().next().next().children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().next().next().children('.cart-minus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().children().map((item, key) => {
        key.style.backgroundColor = 'gray'
        }
    )
    $(this)[0].style.backgroundColor = 'pink'
});
$('.weight-select-product-details-button').on("click touchend", function (event) {
    event.preventDefault();
    $(this).parent().parent().next().children('.price').text($(this).data('price') + ' р.')
    $(this).parent().parent().next().children('.details_to_cart_btn')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().parent().next().children('.cart-qty-wrapper').children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().parent().next().children('.cart-qty-wrapper').children('.cart-minus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().children().map((item, key) => {
        key.style.backgroundColor = 'gray'
        }
    )
    $(this)[0].style.backgroundColor = '#FF0000'
});
