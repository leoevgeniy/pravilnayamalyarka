let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
let event = "click";

if(iOS != null)
    event = "touchstart";
    device = 'IOS'
const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('cart');
const myModal = new bootstrap.Modal('#cartmodal', {

})
let touchEvent = 'ontouchstart' in window ? 'touchend' : 'click';
let passiveEvent = false;
try {
    let opts = Object.defineProperty({}, 'passive', {
        get: function () {
            passiveEvent = true;
        }
    });
    window.addEventListener("test", null, opts);
} catch (e) { }
console.log(passiveEvent)
// in my case I need both passive and capture set to true, change as you need it.
// passiveEvent =  false;
passiveEvent = passiveEvent ? { capture: true, passive: true } : false;
if (myParam === '1') {
    myModal.show()
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
const addToStorage = (product) => {
    let exist = false

    try {
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
    }}
    catch {}

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

    window.sessionStorage.setItem('cart', JSON.stringify([{"id":"2398476283","name":"Абразив 2","qty":1,"weight":"402"}]))
let sessionstorage = JSON.parse(sessionStorage.getItem('cart'))
console.log(sessionstorage)
    function getCookie(name) {

    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? matches[1] : null;

}
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
const updateQty = () => {
    let totalcost = 0
    try {
        const price = document.querySelectorAll('.t706__cartwin-prodamount-price')
        price.forEach(function (item) {
            const weight = item.dataset['weight']
            const id = item.dataset['id']
            const sum = Number(item.dataset['price']) * Number(getQty(id, weight))
            totalcost += sum
            item.innerHTML = '<strong>Стоимость: </strong></br> ' + sum + ' р.'
        })
    } catch {}
    try {
        const totalprice = document.querySelectorAll('.t706__cartwin-prodamount-total-price')[0]
        totalprice.innerHTML = String(totalcost)
    } catch {}
    try {
        const qty = document.querySelectorAll('.t706__product-quantity')

        qty.forEach(function (item) {
            try {
                const weight = item.dataset['weight']
                const id = item.dataset['id']
                item.innerHTML = String(getQty(id, weight))
            } catch {
                const id = item.dataset('id')
                item.innerHTML = String(getQty(id, ''))
            }

        })
    } catch {}
    try {
        const counter = document.getElementsByClassName('.js-carticon-counter')[0]
        counter.text(getAllQty())
    } catch {}
    // $('.cart-amount-footer').text(getAllQty())
    try {
        const cartstick = document.getElementById('cart_sticked')
        if (getAllQty() === 0) {
            // $('.cart-confirm-btn').addClass('disabled')

            cartstick.style.display = 'none'
            // $('.cart-amount-footer').addClass('d-none')
        } else {
            // $('.cart-confirm-btn').removeClass('disabled')
            cartstick.style.display = 'block'
            cartstick.children[1].textContent = String(getAllQty())
            // $('.cart-amount-footer').removeClass('d-none')

        }
    } catch {}
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
try {
    const minusbtn = document.querySelectorAll('.t706__product-minus')
    minusbtn.forEach(item => {
    //     item.addEventListener(touchEvent, function (e) {
    //
    //         // e.preventDefault();
    //         let id = item.dataset['id']
    //         const weight = item.dataset['weight']
    //         removeFromStorage(id, weight)
    //         updateQty()
    //
    //     })
    // }, passiveEvent)
        item.ontouchend = function () {
            // e.preventDefault();
            let id = item.dataset['id']
            const weight = item.dataset['weight']
            removeFromStorage(id, weight)
            updateQty()

        }

    })
} catch {}
try {
    const plusbtn = document.querySelectorAll('.t706__product-plus')
    plusbtn.forEach(item => {
        //     item.addEventListener(touchEvent, function (e) {
        //         // e.preventDefault();
        //         const weight = item.dataset['weight']
        //
        //         const product = {'id': item.dataset['id'], 'name': item.dataset['name'], 'qty': 1, 'weight': weight}
        //         addToStorage(product);
        //         updateQty()
        //
        //     }, passiveEvent)
        // })
        item.ontouchend = function () {
            // e.preventDefault();
            const weight = item.dataset['weight']

            const product = {'id': item.dataset['id'], 'name': item.dataset['name'], 'qty': 1, 'weight': weight}
            addToStorage(product);
            updateQty()

        }
    })
    } catch {}
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

try {
const buybtn = document.querySelector('.buy_button');
// buybtn.addEventListener(touchEvent, function (event) {
//     event.preventDefault();
//     event.stopPropagation();
//     let weight = ''
//     try {        weight = buybtn.dataset['weight']
//     } catch {
//         weight = ''
//     }
//     const product = {'id': buybtn.dataset['id'], 'name': buybtn.dataset['name'], 'qty': 1, 'weight': weight}
//     addToStorage(product);
//
//     window.location.href = document.referrer.split('?')[0] + '?cart=1'
//     updateQty()
// }, passiveEvent)
buybtn.ontouchend = function () {
    let weight = ''
    try {        weight = buybtn.dataset['weight']
    } catch {
        weight = ''
    }
    const product = {'id': buybtn.dataset['id'], 'name': buybtn.dataset['name'], 'qty': 1, 'weight': weight}
    addToStorage(product);

    window.location.href = document.referrer.split('?')[0] + '?cart=1'
    updateQty()
}
}
catch {}

// $('#buy_button').bind(event, null, function (event) {
//     event.preventDefault();
//     event.stopPropagation()
//     let weight = ''
//     try {        weight = $(this)[0].dataset['weight']
//     } catch {
//         weight = ''
//     }
//     const product = {'id': $(this).data('id'), 'name': $(this).data('name'), 'qty': 1, 'weight': weight}
//     addToStorage(product);
//     console.log(product)
//     location.replace($(this).data('categoryurl')+'?cart=1')
//     updateQty()
//     // location.reload();
// });
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
try {
    const cart_remove = document.querySelectorAll('.t706__product-del')
    cart_remove.forEach(item => {
        item.addEventListener(touchEvent, function (e) {
            // e.preventDefault()
            deleteFromStorage(item.dataset['id'])
            location.reload();
        }, passiveEvent)
    })

} catch {}

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