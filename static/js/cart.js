function getCookie(name) {

    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? matches[1] : null;

}

const updateQty = () => {

    $('.price_info').each(function () {
        const weight = $(this).data('weight')
        const id = $(this).data('id')
        const sum = $(this).data('price') * Number(getQty(id,weight))
        console.log(sum)
        $(this).text('Стоимость: ' + sum + ' р.')
    })
    $('.cart-qty').each(function () {
        try {
            const weight = $(this).data('weight')
            const id = $(this).data('id')
            $(this).text(getQty(id,weight))
        } catch {
            const id = $(this).data('id')
            console.log($(this).data('id'))
            $(this).text(getQty(id, ''))
        }

    })
    $('.cart-amount').text(getAllQty())
    if (getAllQty() === 0) {
        $('.cart-confirm-btn').addClass('disabled')
    }
    $('.add-to-cart-btn').each(function () {
        const id = $(this).data('id')
        let exist = false
        if (getCookie('cart')) {
            let index = 0
            let cart = JSON.parse(getCookie('cart'))
            for (let i in cart) {
                if (cart[i].id === id) {
                    exist = true
                }
                index++
            }

        }
        if (exist) {
            $(this).addClass('d-none')
        } else {
            $(this).removeClass('d-none')
        }
    })
    $('.cart-qty-wrapper').each(function () {
        const id = $(this).data('id')
        let exist = false
        if (getCookie('cart')) {
            let index = 0
            let cart = JSON.parse(getCookie('cart'))
            for (let i in cart) {
                if (cart[i].id === id) {
                    exist = true
                }
                index++
            }

        }
        if (exist) {
            $(this).removeClass('d-none')

        } else {
            $(this).addClass('d-none')
        }
    })
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
                        console.log(weight)
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

$('.cart-minus').click(function (e) {
    e.preventDefault();
    let id = $(this).data('id')
    const weight = $(this).data('weight')
    removeFromStorage(id, weight)
    updateQty()

})
$('.cart-plus').click(function (e) {
    e.preventDefault();
    const weight = $(this)[0].dataset['weight']

    const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
    console.log(product)
    addToStorage(product);
    updateQty()

})
$('.add-to-cart-btn').click(function (event) {
    event.preventDefault();
    let weight = ''
    if ($(this)[0].dataset['weight']) {
        weight = $(this)[0].dataset['weight']
    } else {
        weight = ''
    }

    const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
    addToStorage(product);
    updateQty()
});

$('.remove-from-cart').click(function (e) {
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
    // document.cookie = 'cart=' + JSON.stringify([]) + ";path=/"
    // localStorage.setItem('cart', JSON.stringify([]))
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