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
//     }, passiveEvent)
// })
try {
    const weight_select = document.querySelectorAll('.weight-select-button')
    weight_select.forEach(function (elem) {

        elem.addEventListener('click', function (event) {
            if (location.pathname.includes('/search')) {
                elem.parentElement.nextElementSibling.href =elem.parentElement.nextElementSibling.href.split('&weight=')[0] + '&weight='+ elem.dataset['id'].split('plus')[1]
            }
            else {
                elem.parentElement.nextElementSibling.href = elem.parentElement.nextElementSibling.href.split('?weight=')[0] + '?weight=' + elem.dataset['id'].split('plus')[1]
            }


            elem.parentElement.previousElementSibling.children[2].textContent = elem.dataset['price'] + 'p'
            elem.parentElement.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            for (let weight=0; weight < elem.parentElement.children.length; weight++) {
                elem.parentElement.children[weight].style.backgroundColor = 'gray'
                elem.style.backgroundColor = 'blue'
            }
        })

    }, passiveEvent)
    // .on(event, function (event) {

    // $(this).parent().prev().find('.card-price')[0].innerText = $(this).data('price') + 'р.'
    } catch {}
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
try {
    const search_close = document.getElementById('search_close')
    search_close.onclick = (e) => {
        location.href = location.pathname.split('?')[0]
    }
}
catch {}