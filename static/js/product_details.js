// let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
// let event = "click";
//
// if(iOS != null)
//     event = "touchstart";

$('.product_details_weight-select-button').on(event, function (event) {
    event.preventDefault();
    console.log($(this).parent().prev().children('#price')[0].innerText)

    $(this).parent().prev().children('#price')[0].innerText = $(this).data('price') + 'р.'
    $(this).parent().next()[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().next()[0].dataset['price'] = $(this).data('price')

    // $(this).parent().next().next().children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    // $(this).parent().next().next().children('.cart-minus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().children().map((item, key) => {
            key.style.backgroundColor = 'gray'
        }
    )
    $(this)[0].style.backgroundColor = 'blue'
});