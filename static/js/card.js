// let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
// let event = "click";
//
// if(iOS != null)
//     event = "touchstart";

// const weight_selected = document.querySelectorAll('weight-select-button')
// document.querySelectorAll('goods_index_products_item').forEach((item) => {
//
// })
// weight_selected.forEach( (el) =>  {
//     el.addEventListener("click", (event) => {
//         console.log(el.dataset.price)
//         event.preventDefault();
//         el.parent().prev().find('.card-price').innerText = el.data('price') + 'р.'
//         console.log(el.parent().prev().find('.card-price').innerText)
//     })
// })

$('.weight-select-button').on(event, function (event) {
    event.preventDefault();
    $(this).parent().prev().find('.card-price')[0].innerText = $(this).data('price') + 'р.'
    $(this).parent().next()[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    console.log($(this).parent().prev().find('.card-price')[0].innerText)

    // $(this).parent().next().next().children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    // $(this).parent().next().next().children('.cart-minus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().children().map((item, key) => {
        key.style.backgroundColor = 'gray'
        }
    )
    $(this)[0].style.backgroundColor = 'blue'
});
// $('.weight-select-product-details-button').on("click touchstart", function (event) {
//     event.preventDefault();
//     $(this).parent().parent().next().children('.price').text($(this).data('price') + ' р.')
//     $(this).parent().parent().next().children('.details_to_cart_btn')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
//     $(this).parent().parent().next().children('.cart-qty-wrapper').children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
//     $(this).parent().parent().next().children('.cart-qty-wrapper').children('.cart-minus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
//     $(this).parent().children().map((item, key) => {
//         key.style.backgroundColor = 'gray'
//         }
//     )
//     $(this)[0].style.backgroundColor = '#FF0000'
// });
