// let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
// let event = "click";
//
// if(iOS != null)
//     event = "touchstart";
let fullmyModal = ''
try {
    fullmyModal = new bootstrap.Modal('#fullimg', {})
} catch {}
try {
    const product_details_weight_select_button = document.querySelectorAll('.product_details_weight-select-button')
    product_details_weight_select_button.forEach(

    function (elem) {
        elem.addEventListener(event, function (event) {
            // event.preventDefault();
            elem.parentElement.previousElementSibling.children[0].innerText = elem.dataset['price'] + 'р.'
            elem.parentElement.nextElementSibling.firstElementChild.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            elem.parentElement.nextElementSibling.firstElementChild.dataset['price'] = elem.dataset['price']
            for (let weight=0; weight < elem.parentElement.children.length; weight++) {
                elem.parentElement.children[weight].style.borderWidth = '1px'
                elem.style.borderWidth = '2px'
            }
        }, passiveEvent);

    })

} catch {}
try {
    const dropdown_product_details_weight_select_button = document.querySelectorAll('.dropdown-product-details-weight-select-button')
    dropdown_product_details_weight_select_button.forEach(

    function (elem) {
        elem.addEventListener(event, function (event) {
            // event.preventDefault();
            elem.parentElement.parentElement.previousElementSibling.innerHTML = elem.dataset['weight']
            elem.parentElement.parentElement.parentElement.parentElement.previousElementSibling.children[0].innerText = elem.dataset['price'] + 'р.'
            elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.firstElementChild.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            elem.parentElement.parentElement.parentElement.parentElement.nextElementSibling.firstElementChild.dataset['price'] = elem.dataset['price']
            // for (let weight=0; weight < elem.parentElement.children.length; weight++) {
            //     elem.parentElement.children[weight].style.borderWidth = '1px'
            //     elem.style.borderWidth = '2px'
            // }
        }, passiveEvent);

    })

} catch {}

try {
    item_photo = document.querySelectorAll('.item_photo')
    item_photo.forEach(function (item) {
        item.addEventListener(event, function (event) {
            event.preventDefault()
            fullmyModal.show()
        }, passiveEvent)

    })
} catch {}
function close_product_view() {
    const referer = document.referrer
    if (referer.includes('?cart=1')) {
        history.go(-2)
    }
    else {
        history.back()
        // document.location.replace(referer)
    }

}