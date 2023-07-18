let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
let event = "click";

if(iOS != null)
    event = "touchstart";


function getCookie(name) {

    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? matches[1] : null;

}

const updateQty = () => {
    let totalcost = 0
    $('.t706__cartwin-prodamount-price').each(function () {
        const weight = $(this).data('weight')
        const id = $(this).data('id')
        const sum = $(this).data('price') * Number(getQty(id,weight))
        totalcost += sum
        $(this).html('<strong>Стоимость: </strong></br> ' + sum + ' р.')
    })
    $('.t706__cartwin-prodamount-total-price').text(String(totalcost))
    $('.t706__product-quantity').each(function () {
        try {
            const weight = $(this).data('weight')
            const id = $(this).data('id')
            $(this).text(getQty(id,weight))
        } catch {
            const id = $(this).data('id')
            $(this).text(getQty(id, ''))
        }

    })
    $('.js-carticon-counter').text(getAllQty())
    // $('.cart-amount-footer').text(getAllQty())
    if (getAllQty() === 0 ) {
        // $('.cart-confirm-btn').addClass('disabled')
        $('#cart_sticked').addClass('d-none')
        // $('.cart-amount-footer').addClass('d-none')
    } else {
        // $('.cart-confirm-btn').removeClass('disabled')
        $('#cart_sticked').removeClass('d-none')
        // $('.cart-amount-footer').removeClass('d-none')

    }
    // $('.footer_search').on("click touchend", function () {
    //     $('.search_input').focus()
    // })
    // $('.add-to-cart-btn').each(function () {
    //     const id = $(this).data('id')
    //     let exist = false
    //     if (getCookie('cart')) {
    //         let index = 0
    //         let cart = JSON.parse(getCookie('cart'))
    //         for (let i in cart) {
    //             if (cart[i].id === id) {
    //                 exist = true
    //             }
    //             index++
    //         }
    //
    //     }
    //     if (exist) {
    //         $(this).addClass('d-none')
    //     } else {
    //         $(this).removeClass('d-none')
    //     }
    // })
    // $('.t706__product-quantity').each(function () {
    //     const id = $(this).data('id')
    //     let exist = false
    //     if (getCookie('cart')) {
    //         let index = 0
    //         let cart = JSON.parse(getCookie('cart'))
    //         for (let i in cart) {
    //             if (cart[i].id === id) {
    //                 exist = true
    //             }
    //             index++
    //         }
    //
    //     }
    //     if (exist) {
    //         $(this).removeClass('d-none')
    //
    //     } else {
    //         $(this).addClass('d-none')
    //     }
    // })
}

const addToStorage = (product) => {
    let exist = false


    if (getCookie('cart')) {
        let cart = JSON.parse(getCookie('cart'))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === product.id) {
                if (cart[i].weight === product.weight) {
                    exist = true
                    cart[i]['qty'] += 1
                }
            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            // localStorage.setItem('cart', JSON.stringify(cart))
            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
        } else {
            cart.push(product)
            // localStorage.setItem('cart', JSON.stringify(cart))
            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
        }
    } else {
        // localStorage.setItem('cart', JSON.stringify([product]))
        document.cookie = 'cart=' + JSON.stringify([product]) + ";path=/"
    }
    updateQty()
}
const removeFromStorage = (id, weight) => {
    let exist = false
    if (getCookie('cart')) {
        let cart = JSON.parse(getCookie('cart'))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === id) {
                if (weight === '') {

                    if (cart[i]['qty'] > 1) {
                        cart[i]['qty'] -= 1
                        exist = true
                    } else if (cart[i]['qty'] === 1) {
                        cart.splice(index, 1)
                        // localStorage.setItem('cart', JSON.stringify(cart))
                        document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
                        location.reload();
                    } else {
                        cart.splice(index, 1)
                        // localStorage.setItem('cart', JSON.stringify(cart))
                        document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
                        location.reload();
                    }
                } else {
                    if (cart[i].weight === String(weight)) {

                        if (cart[i]['qty'] > 1) {
                            cart[i]['qty'] -= 1
                            exist = true

                        } else if (cart[index]['qty'] === 1) {
                            cart.splice(index, 1)
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
                            location.reload();
                        } else {
                            cart.splice(index, 1)
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
                            location.reload();
                        }
                    }
                }

            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            // localStorage.setItem('cart', JSON.stringify(cart))
            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"

        }
    }
}

const deleteFromStorage = (id) => {
    let exist = false
    if (getCookie('cart')) {
        let cart = JSON.parse(getCookie('cart'))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === id) {
                exist = true
                cart.splice(index, 1)
            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            // localStorage.setItem('cart', JSON.stringify(cart))
            document.cookie = 'cart=' + JSON.stringify(cart) + ";path=/"
        }
    }

}

$('.t706__product-minus').on(event, function (e) {
    e.preventDefault();
    let id = $(this).data('id')
    const weight = $(this).data('weight')
    removeFromStorage(id, weight)
    updateQty()

})
$('.t706__product-plus').on(event, function (e) {
    e.preventDefault();
    const weight = $(this)[0].dataset['weight']

    const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
    addToStorage(product);
    updateQty()

})
// function onBuyButton(weight, id, name, categoryurl) {
//     // try {        weight = $(this)[0].dataset['weight']
//     // } catch {
//     //     weight = ''
//     // }
//     const product = {'id': id, 'name':name, 'qty': 1, 'weight': weight}
//     addToStorage(product);
//     location.replace(categoryurl +'?cart=1')
//     updateQty()
// }
$('#buy_button').on(event, function (event) {
    // event.preventDefault();
    event.stopPropagation()
    let weight = ''
    try {        weight = $(this)[0].dataset['weight']
    } catch {
        weight = ''
    }
    const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
    addToStorage(product);
    location.replace($(this).data('categoryurl')+'?cart=1')
    updateQty()
    // location.reload();
});
// $('.add-to-cart-btn').on("touchstart", function (event) {
//     event.preventDefault();
//     let weight = ''
//     if ($(this)[0].dataset['weight']) {
//         weight = $(this)[0].dataset['weight']
//     } else {
//         weight = ''
//     }
//     const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
//     addToStorage(product);
//     location.replace($(this).data('categoryurl')+'?cart=1')
//     updateQty()
//     // location.reload();
// });

$('.t706__product-del').on(event, function (e) {
    e.preventDefault()
    deleteFromStorage($(this).data('id'))
    location.reload();
})

const getQty = (id, weight) => {
    if (getCookie('cart')) {
        let cart = JSON.parse(getCookie('cart'))
        let qty = 0
        for (let i in cart) {
            if (cart[i]['id'] === id) {
            // if (cart[i]['id'] === 60256) {
                if (weight !== '') {

                    if (cart[i]['weight'] === String(weight)) {

                        qty += cart[i]['qty']
                    }
                } else {
                    qty += cart[i]['qty']
                }

            }
        }
        return qty
    } else {
        return 0
    }
}
const getAllQty = () => {
    if (getCookie('cart')) {
        let amount = 0
        // let cart = JSON.parse(localStorage.getItem('cart'))
        let cart = JSON.parse(getCookie('cart'))
        for (let i in cart) {
            amount += cart[i]['qty']
        }
        return amount
    } else
        return 0
}


const clearcart = () => {
    document.cookie = 'cart=' + JSON.stringify([]) + ";path=/"
    localStorage.setItem('cart', JSON.stringify([]))
}
// const cartConfirm = (input, init) => {
//     let cart = JSON.parse(localStorage.getItem('cart'))
//     const csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
//     fetch('/ordercreate/', {
//         method: 'POST', headers: {
//             "X-CSRFToken": csrf_token
//         }, body: JSON.stringify(cart)
//     }).then()
// }