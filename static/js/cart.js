window.addEventListener( "pageshow", function ( event ) {
    let historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
    if ( historyTraversal ) {
        // Handle page restore.
        window.location.replace(location.pathname);
    }
});
let iOS = navigator.userAgent.match(/iPhone|iPad|iPod|Mac OS/i);
let event = "click";
let device = ''
if (iOS != null) {
    event = "touchstart";
    device = 'IOS'
}
const hostname = location.hostname
const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('cart');
const current_url = window.location.pathname
let date = new Date(Date.now() + 86400e3);
date = date.toUTCString();
const myModal = new bootstrap.Modal('#cartmodal', {})
let touchEvent = 'ontouchstart' in window ? 'touchend' : 'click';
let passiveEvent = false;
try {
    let opts = Object.defineProperty({}, 'passive', {
        get: function () {
            passiveEvent = true;
        }
    });
    window.addEventListener("test", null, opts);
} catch (e) {
}
try {
    document.getElementById('cartmodal').addEventListener('hidden.bs.modal', function () {
        toproducts()
    })
} catch {}

// in my case I need both passive and capture set to true, change as you need it.
// passiveEvent =  false;
passiveEvent = passiveEvent ? {capture: true, passive: true} : false;
if (myParam === '1') {
    // cart_generate()
    myModal.show()
}
// myModal.onShow(function () {
//     console.log('показан')
// })
// async function cart_generate() {
//
//
//         const csrfToken = document.head.querySelector("[name~=csrf_token][content]").content;
//         const response = await fetch("/getcart/",
//             {
//                 method: 'POST',
//                 body: JSON.stringify(local_cart),
//                 cururl: current_url,
//
//                 credentials: 'same-origin',
//                 headers: {
//                     'X-CSRFToken': csrftoken,
//                     // "Content-Type": "application/json"
//                 },
//
//             }
//         ).then((response) => response.json())
//         // .then((data) => data)
//         console.log(location)
//     }
// }

// const myModalEl = document.getElementById('cartmodal')
// console.log(myModalEl)
// myModalEl.addEventListener('shown.bs.modal', async event => {
//     let local_cart = []
//     try {
//         local_cart = localStorage.getItem('cart')
//     } catch {
//     }
//     const csrfToken = document.head.querySelector("[name~=csrf_token][content]").content;
//     console.log(local_cart)
//     const response = await fetch("/getcart/",
//         {
//             method: 'POST',
//             body: JSON.stringify(local_cart),
//             credentials: 'same-origin',
//             headers: { 'X-CSRFToken': csrftoken,
//                 // "Content-Type": "application/json"
//             },
//
//         }
//         ).then((response) => response.json())
//         .then((data) => data)
//     console.log(response)
// })


const getAllQty = () => {
    if (getCookie('cart')) {
        let amount = 0
        // let cart = JSON.parse(localStorage.getItem('cart'))
        let cart = JSON.parse(decodeURIComponent(getCookie('cart')))
        for (let i in cart) {
            amount += cart[i]['qty']
        }
        return amount
    } else
        return 0
}
const addToStorage = (product) => {
    let exist = false;
    // alert(device)
    // if (device !== 'IOS') {

        // else {
        try {
            if (getCookie('cart')) {
                let cart = JSON.parse(decodeURIComponent(getCookie('cart')))
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
                    document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
                } else {
                    cart.push(product)
                    // localStorage.setItem('cart', JSON.stringify(cart))
                    document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) +  ";path=/" + ";expires=" + date
                }
            } else {
                // localStorage.setItem('cart', JSON.stringify([product]))
                document.cookie = 'cart=' + encodeURIComponent(JSON.stringify([product])) + ";path=/" + ";expires=" + date
            }
            // if (localStorage.getItem('cart')) {
            //     let cart = JSON.parse(localStorage.getItem('cart'))
            //     let index = 0
            //     for (let i in cart) {
            //         if (cart[i].id === product.id) {
            //             if (cart[i].weight === product.weight) {
            //                 exist = true
            //                 cart[i]['qty'] += 1
            //             }
            //         }
            //         index++
            //     }
            //     if (exist) {
            //         // localStorage.removeItem('cart')
            //         // localStorage.setItem('cart', JSON.stringify(cart))
            //         localStorage.setItem('cart', JSON.stringify(cart))
            //     } else {
            //         cart.push(product)
            //         // localStorage.setItem('cart', JSON.stringify(cart))
            //         localStorage.setItem('cart', JSON.stringify(cart))
            //     }
            //
            // } else {
            //     localStorage.setItem('cart', JSON.stringify([product]))
            // }
        } catch {
        }
    // } else {
    //     let local_cart = []
    //     try {
    //         try {
    //             local_cart = getCookie('cart')
    //             alert('корзина' + local_cart)
    //         } catch {
    //             alert("Не смог прочитать куки")
    //         }
    //         try {
    //             document.cookie = 'cart=' + encodeURIComponent(JSON.stringify([product])) + ";domain=" + hostname + ";path=/" + ";expires=" + date
    //             alert(product)
    //             alert([product])
    //             alert('Записал куки  cart=' + encodeURIComponent(JSON.stringify([product])) + ";domain=" + hostname + ";path=/" + ";expires=" + date)
    //             local_cart = getCookie('cart')
    //             alert('Вот что в куки' + document.cookie)
    //         } catch {
    //             alert("не смог записать куки")
    //         }
    //     } catch {
    //
    //     }
    //     try {
    //         const ios_cart = getCookie('cart')
    //         if  (ios_cart) {
    //             let cart = JSON.parse(getCookie('cart'))
    //             let index = 0
    //             for (let i in cart) {
    //                 if (cart[i].id === product.id) {
    //                     if (cart[i].weight === product.weight) {
    //                         exist = true
    //                         cart[i]['qty'] += 1
    //                     }
    //                 }
    //                 index++
    //             }
    //             if (exist) {
    //                 // localStorage.removeItem('cart')
    //                 // localStorage.setItem('cart', JSON.stringify(cart))
    //                 document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=" + hostname + ";path=/" + ";expires=" + date
    //             } else {
    //                 cart.push(product)
    //                 // localStorage.setItem('cart', JSON.stringify(cart))
    //                 document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=" + hostname + ";path=/" + ";expires=" + date
    //             }
    //         }
    //         alert(decodeURIComponent(getCookie('cart')))
    //     } catch {
    //         document.cookie = 'cart=' + JSON.stringify([product]) + ";domain=" + hostname + ";path=/" + ";expires=" + date
    //         alert(decodeURIComponent(getCookie('cart')))
    //     }
    // }


    // }


    updateQty()
}
const removeFromStorage = (id, weight) => {
    let exist = false
    if (getCookie('cart')) {
        let cart = JSON.parse(decodeURIComponent(getCookie('cart')))
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
                        // localStorage.setItem('cart', JSON.stringify(cart))
                        document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
                        product_element = document.getElementById(id + '/' + weight)
                        product_element.parentNode.removeChild(product_element)
                        try {
                            if (getAllQty() === 0) {
                                myModal.close()
                                console.log(getAllQty())
                            }
                        } catch {
                        }

                        // location.reload();
                    } else {
                        cart.splice(index, 1)
                        // localStorage.setItem('cart', JSON.stringify(cart))
                        // localStorage.setItem('cart', JSON.stringify(cart))

                        document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
                        // location.reload();
                    }
                } else {
                    if (cart[i].weight === String(weight)) {

                        if (cart[i]['qty'] > 1) {
                            cart[i]['qty'] -= 1
                            exist = true

                        } else if (cart[index]['qty'] === 1) {
                            cart.splice(index, 1)
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            try {
                                if (getAllQty() === 0) {
                                    myModal.close()
                                    console.log(getAllQty())
                                }
                            } catch {
                            }

                            product_element = document.getElementById(id + '/' + weight)
                            product_element.parentNode.removeChild(product_element)

                            // location.reload();
                        } else {
                            cart.splice(index, 1)
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
                            // localStorage.setItem('cart', JSON.stringify(cart))
                            try {
                                if (getAllQty() === 0) {
                                    myModal.close()
                                    console.log(getAllQty())
                                }
                            } catch {
                            }

                            product_element = document.getElementById(id + '/' + weight)
                            product_element.parentNode.removeChild(product_element)

                            // location.reload();
                        }
                    }
                }

            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            // localStorage.setItem('cart', JSON.stringify(cart))
            // localStorage.setItem('cart', JSON.stringify(cart))

            document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date


        }
    }
    updateQty()
}
const deleteFromStorage = (id, weight) => {
    let exist = false
    if (getCookie('cart')) {
        let cart = JSON.parse(decodeURIComponent(getCookie('cart')))
        let index = 0
        for (let i in cart) {
            if (cart[i].id === id && cart[i].weight === weight) {
                exist = true
                cart.splice(index, 1)
            }
            index++
        }
        if (exist) {
            // localStorage.removeItem('cart')
            // localStorage.setItem('cart', JSON.stringify(cart))
            product_element = document.getElementById(id + '/' + weight)
            product_element.parentNode.removeChild(product_element)
            // localStorage.setItem('cart', JSON.stringify(cart))

            document.cookie = 'cart=' + encodeURIComponent(JSON.stringify(cart)) + ";path=/" + ";expires=" + date
        }
    }
    try {
        if (getAllQty() === 0) {
            myModal.close()
            console.log(getAllQty())
        }
    } catch {
    }

    updateQty()

}

// function getCookie(name) {
//
//     let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
//     return matches ? matches[1] : null;
//
// }
function getCookie(name) {
    let match = document.cookie
        .split('; ')
        .find(row => row.startsWith(`${name}=`));

    return match ? match.split('=')[1] : undefined;
}

const getQty = (id, weight) => {
    if (getCookie('cart')) {
        let cart = JSON.parse(decodeURIComponent(getCookie('cart')))
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
        const local_cart = localStorage.getItem('cart')
        const local_cart_element = document.getElementById('local_cart')
        local_cart_element.value = JSON.stringify(local_cart)
        sessionStorage.setItem('cart', local_cart)
    } catch {
    }
    try {
        const price = document.querySelectorAll('.t706__cartwin-prodamount-price')
        price.forEach(function (item) {
            const weight = item.dataset['weight']
            const id = item.dataset['id']
            const sum = parseFloat((parseFloat(item.dataset['price'].replace(',','.')) * Number(getQty(id, weight))).toFixed(2))

            totalcost += sum
            item.innerHTML = '<strong>Стоимость: </strong></br> ' + sum.toFixed(2) + ' р.'
        })
    } catch {
    }
    try {
        const totalprice = document.querySelectorAll('.t706__cartwin-prodamount-total-price')[0]
        totalprice.innerHTML = String(totalcost.toFixed(2))
    } catch {
    }
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
    } catch {
    }
    try {
        const counter = document.querySelector('.js-carticon-counter')
        counter.innerHTML = String(getAllQty())
    } catch {
    }
    // $('.cart-amount-footer').text(getAllQty())
    try {
        const cartstick = document.getElementById('cart_sticked')
        if (getAllQty() === 0) {
            // $('.cart-confirm-btn').addClass('disabled')

            cartstick.style.display = 'none'
            // $('.cart-amount-footer').addClass('d-none')
        } else {
            // $('.cart-confirm-btn').removeClass('disabled')
            if (window.innerWidth < 480) {
                cartstick.style.cssText = 'display: block;   position: fixed; z-index: 1030; top: 120px; right: 20px;'
            } else {
                cartstick.style.cssText = 'display: block;   position: fixed; z-index: 1030; top: 180px; right: 20px;'
            }
            // cartstick.children[1].textContent = String(getAllQty())
            // $('.cart-amount-footer').removeClass('d-none')

        }
    } catch {
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
try {
    const minusbtn = document.querySelectorAll('.t706__product-minus')
    minusbtn.forEach(item => {
        item.onclick = function (e) {

            // e.preventDefault();
            let id = item.dataset['id']
            const weight = item.dataset['weight']
            removeFromStorage(id, weight)
            updateQty()

        }

        // item.ontouchend = function () {
        //     // e.preventDefault();
        //     let id = item.dataset['id']
        //     const weight = item.dataset['weight']
        //     removeFromStorage(id, weight)
        //     updateQty()
        //
        // }
    })

} catch {
}
try {
    const plusbtn = document.querySelectorAll('.t706__product-plus')
    plusbtn.forEach(item => {
        item.onclick = function (e) {
            // e.preventDefault();
            const weight = item.dataset['weight']

            const product = {'id': item.dataset['id'], 'name': item.dataset['name'], 'qty': 1, 'weight': weight}
            addToStorage(product);
            updateQty()

        }

        // item.ontouchend = function () {
        //     // e.preventDefault();
        //     const weight = item.dataset['weight']
        //
        //     const product = {'id': item.dataset['id'], 'name': item.dataset['name'], 'qty': 1, 'weight': weight}
        //     addToStorage(product);
        //     updateQty()
        //
        // }
    })
} catch {
}
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
    const buybtn = document.getElementById('buy_button');
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
// buybtn.ontouchend = function () {
//     let weight = ''
//     try {        weight = buybtn.dataset['weight']
//     } catch {
//         weight = ''
//     }
//     console.log('1', weight, '1')
//     const product = {'id': buybtn.dataset['id'], 'name': buybtn.dataset['name'], 'qty': 1, 'weight': weight}
//     addToStorage(product);
//
//     window.location.href = document.referrer.split('?')[0] + '?cart=1'
//     updateQty()
// }

    buybtn.onclick = function () {
        let weight = ''
        try {
            weight = buybtn.dataset['weight']
        } catch {
            weight = ''
        }
        const product = {'id': buybtn.dataset['id'], 'name': buybtn.dataset['name'], 'qty': 1, 'weight': weight}
        try {
            const carticon = document.getElementById('cart_sticked')
            // carticon.classList.remove('cart_icon_animation')

            carticon.classList.add('cart_icon_animation')
            setTimeout(() => {carticon.classList.remove('cart_icon_animation')}, 1000)
        }catch {}

        addToStorage(product);
        // let query = ''
        // try {
        //     if (location.href.split('text=')[1])
        //     query = '?text=' + location.href.split('text=')[1]
        // }
        // catch {}
        // window.location.href = document.referrer.split('?')[0]+query
            // + '?cart=1'
        updateQty()

    }
} catch {
}
const toproducts = () => {
    let query = ''
    try {
        if (location.href.split('text=')[1])
        query = '?text='+location.href.split('text=')[1]
    }
    catch {}
    location.replace(location.pathname.split('?')[0]+query)
}
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
            deleteFromStorage(item.dataset['id'], item.dataset['weight'])
            // location.reload();
        }, passiveEvent)
    })

} catch {
}

const clearcart = () => {
    // document.cookie = 'cart=' + JSON.stringify([]) + ";path=/"
    localStorage.setItem('cart', JSON.stringify([]))
}
try {

} catch {}
// const cartConfirm = (input, init) => {
//     let cart = JSON.parse(localStorage.getItem('cart'))
//     const csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
//     fetch('/ordercreate/', {
//         method: 'POST', headers: {
//             "X-CSRFToken": csrf_token
//         }, body: JSON.stringify(cart)
//     }).then()
// }

// const small_cart = document.getElementById('cart_sticked')
// console.log(window.ready)
// alert(small_cart.style.position)


let slideIndex = 1;
let flex_video = document.getElementsByClassName("flex-video")
if (flex_video) {
   slideIndex = 2; }
try {
    showSlides(slideIndex);
}
catch {}
// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    if (slides.length <= 1) {
        document.getElementsByClassName("thumbnail_prev")[0].style.display = "none";
        document.getElementsByClassName("thumbnail_next")[0].style.display = "none";

    }
    let dots = document.getElementsByClassName("demo");
    // let captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    // captionText.innerHTML = dots[slideIndex-1].alt;
}