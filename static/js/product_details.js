// let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
// let event = "click";
//
// if(iOS != null)
//     event = "touchstart";
try {
    const product_details_weight_select_button = document.querySelectorAll('.product_details_weight-select-button')
    product_details_weight_select_button.forEach(

    function (elem) {
        elem.addEventListener(event, function (event) {
            // event.preventDefault();
            elem.parentElement.previousElementSibling.children[0].innerText = elem.dataset['price'] + 'р.'
            elem.parentElement.nextElementSibling.dataset['weight'] = elem.dataset['id'].split('plus')[1]
            elem.parentElement.nextElementSibling.dataset['price'] = elem.dataset['price']
            for (let weight=0; weight < elem.parentElement.children.length; weight++) {
                elem.parentElement.children[weight].style.backgroundColor = 'gray'
                elem.style.backgroundColor = 'blue'
            }
        }, passiveEvent);

    })

} catch {}