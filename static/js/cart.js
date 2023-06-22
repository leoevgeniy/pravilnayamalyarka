const updateQty = () => {
    $('.cart-qty').each(function () {
        const id = $(this).data('id')
        $(this).text(getQty(id))
    })
    $('.add-to-cart-btn').each(function () {
        const id = $(this).data('id')
        let exist = false
        if (localStorage.getItem('cart') !== null) {
            let index = 0
            let cart = JSON.parse(localStorage.getItem('cart'))
            for (let i in cart) {
                if (cart[i].id === id) {
                    exist = true
                }
                index++
            }
            if (exist) {
                $(this).addClass('d-none')
            } else {
                $(this).removeClass('d-none')
            }
        }
    })
    $('.cart-qty-wrapper').each(function () {
        const id = $(this).data('id')
        let exist = false
        if (localStorage.getItem('cart') !== null) {
            let index = 0
            let cart = JSON.parse(localStorage.getItem('cart'))
            for (let i in cart) {
                if (cart[i].id === id) {
                    exist = true
                }
                index++
            }
            if (exist) {
                $(this).removeClass('d-none')

            } else {
                $(this).addClass('d-none')
            }
        }
    })
}

const addToStorage = (product) => {
    let exist = false
    if (localStorage.getItem('cart') !== null) {
        let cart = JSON.parse(localStorage.getItem('cart'))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === product.id) {
                exist = true
                cart[index]['qty'] += 1
            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            localStorage.setItem('cart', JSON.stringify(cart))
        } else {
            cart.push(product)
            localStorage.setItem('cart', JSON.stringify(cart))
        }
   } else {
        localStorage.setItem('cart', JSON.stringify([product]))
    }
    updateQty()
}
const removeFromStorage = (id) => {
    let exist = false
    if (localStorage.getItem('cart') !== null) {
        let cart = JSON.parse(localStorage.getItem('cart'))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === id) {
                exist = true
                if (cart[index]['qty'] > 1) {
                    cart[index]['qty'] -= 1
                } else if (cart[index]['qty'] === 1) {
                    cart.splice(index, 1)
                } else {
                    cart.splice(index, 1)
                }
            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            localStorage.setItem('cart', JSON.stringify(cart))
        }
   }
}

$('.cart-minus').click(function (e) {
    e.preventDefault();
    let id = $(this).data('id')
    removeFromStorage(id)
    updateQty()

})
$('.cart-plus').click(function (e) {
    e.preventDefault();
    const product = {'id':$(this).data('id'), 'name':$(this).data('name'), 'price':$(this).data('price'), 'qty':1}
    addToStorage(product);
    updateQty()

})
$('.add-to-cart-btn').click(function (event) {
    event.preventDefault();
    const product = {'id':$(this).data('id'), 'name':$(this).data('name'), 'price':$(this).data('price'), 'qty':1}
    addToStorage(product);
    updateQty()
});



const getQty = (id) => {
    if (localStorage.getItem('cart') !== null) {
        let cart = JSON.parse(localStorage.getItem('cart'))
        for (let i in cart) {
            if (cart[i]['id'] === id) {
                return cart[i]['qty']
            }
        }
        return 0
    } else {
        return 0
    }
}