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
                elem.parentElement.nextElementSibling.href = elem.parentElement.nextElementSibling.href.split('&weight=')[0] + '&weight=' + elem.dataset['id'].split('plus')[1]
            } else {
                elem.parentElement.nextElementSibling.href = elem.parentElement.nextElementSibling.href.split('?weight=')[0] + '?weight=' + elem.dataset['id'].split('plus')[1]
            }


            elem.parentElement.previousElementSibling.children[2].textContent = elem.dataset['price'] + ' p.'
            elem.parentElement.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            elem.parentElement.nextElementSibling.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            for (let weight = 0; weight < elem.parentElement.children.length; weight++) {
                elem.parentElement.children[weight].style.borderWidth = '1px'
                elem.style.borderWidth = '2px'
            }
        })

    }, passiveEvent)
    // .on(event, function (event) {

    // $(this).parent().prev().find('.card-price')[0].innerText = $(this).data('price') + 'р.'
} catch {
}
try {
    const dropdown_weight_select = document.querySelectorAll('.dropdown-weight-select-button')
    dropdown_weight_select.forEach(function (elem) {

        elem.addEventListener('click', function (event) {
            if (location.pathname.includes('/search')) {
                elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.href = elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.href.split('&weight=')[0] + '&weight=' + elem.dataset['id'].split('plus')[1]
            } else {
                elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.href = elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.href.split('?weight=')[0] + '?weight=' + elem.dataset['id'].split('plus')[1]
            }
            elem.parentElement.parentElement.previousElementSibling.innerText = elem.dataset['weight']
            elem.parentElement.parentElement.parentElement.parentElement.previousElementSibling.children[2].textContent = elem.dataset['price'] + ' p.'
            elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            // for (let weight = 0; weight < elem.parentElement.parentElement.parentElement.children.length; weight++) {
            //     elem.parentElement.parentElement.parentElement.children[weight].style.borderWidth = '1px'
            //     elem.style.borderWidth = '2px'
            // }
        })

    }, passiveEvent)
    // .on(event, function (event) {

    // $(this).parent().prev().find('.card-price')[0].innerText = $(this).data('price') + 'р.'
} catch {
}
try {
    const buybtncard = document.querySelectorAll('.buy_button_card');
    buybtncard.forEach(function (elem) {
        elem.addEventListener('click', function (event) {
            try {
                const carticon = document.getElementById('cart_sticked')
                // carticon.classList.remove('cart_icon_animation')

                carticon.classList.add('cart_icon_animation')
                setTimeout(() => {
                    carticon.classList.remove('cart_icon_animation')
                }, 1000)
            } catch {
            }
            let weight = ''
            try {
                weight = elem.dataset['weight']
            } catch {
                weight = ''
            }
            const product = {'id': elem.dataset['id'], 'name': elem.dataset['name'], 'qty': 1, 'weight': weight}
            addToStorage(product);
            updateQty()

        })
    }, passiveEvent)
} catch {
}
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
} catch {
}
try {
    const service_nail = document.querySelectorAll('.service_nail')
    let nail_selected = false
    service_nail.forEach((item, index) => {
        if (categories.length > 4) {
                item.parentElement.style.width = String((item.parentElement.parentElement.offsetWidth) / categories.length) + 'px'
            if (window.innerWidth > 470) {
                item.style.height = '150px'
            }
            else {
                item.style.height = '100px'
            }
            item.style.objectfit = 'fill'
        } else {
            item.style.width = '220px'
            item.style.height = '150px'
            item.style.objectfit = 'fill'
        }
        item.addEventListener(touchEvent, ev => {
            nail_selected = true
            changeworkcategory(item)
        })
    })
    if (!nail_selected) {
        const service_big_photo = document.querySelectorAll(".service_big_photo")
        let first = 0
        service_big_photo.forEach((serv, index) => {
            try {
                serv.classList.remove('active')
                serv.classList.remove('carousel-item')
                serv.classList.add('d-none')
            } catch {}
            if (serv.children[0].dataset['category'] === categories[0]) {
                first += 1
                if (first === 1) {
                    serv.classList.remove('d-none')
                    serv.classList.add('active')
                    serv.classList.add('carousel-item')
                }
                else {
                    serv.classList.remove('d-none')

                    serv.classList.add('carousel-item')
                }
            }
        })

    }
} catch {
}

try {
    const description = document.getElementById('description')
    const descr = document.getElementById('descr')
    const characteristics = document.getElementById('characteristics')
    const charact = document.getElementById('charact')

    description.addEventListener(touchEvent, e => {
        e.preventDefault()
        const text_area_text = document.getElementById('text_area_text')
        text_area_text.innerHTML = descr.value
        description.style.borderBottom = "1px solid black"
        characteristics.style.borderBottom = "1px none black"

    })

    characteristics.addEventListener(touchEvent, e => {
        e.preventDefault()
        const text_area_text = document.getElementById('text_area_text')
        text_area_text.innerHTML = charact.value
        description.style.borderBottom = "1px none black"
        characteristics.style.borderBottom = "1px solid black"

    })
} catch {}
function changeworkcategory(item) {
    const service_big_photo = document.querySelectorAll(".service_big_photo")
    let first = 0
    service_big_photo.forEach((serv, index) => {
        try {
            serv.classList.remove('active')
            serv.classList.remove('carousel-item')
            serv.classList.add('d-none')
        } catch {}
        if (serv.children[0].dataset['category'] === item.dataset["category"]) {
            first += 1
            if (first === 1) {
                serv.classList.remove('d-none')
                serv.classList.add('active')
                serv.classList.add('carousel-item')
            }
            else {
                serv.classList.remove('d-none')

                serv.classList.add('carousel-item')
            }
        }
    })
}
