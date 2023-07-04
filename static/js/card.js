$('.weight-select-button').click(function (event) {
    event.preventDefault();
    $(this).parent().prev()[0].innerText = $(this).data('price')
    $(this).parent().next()[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().next().next().children('.cart-plus')[0].dataset['weight'] = $(this).data('id').split('plus')[1]
    $(this).parent().children().map((item, key) => {
        key.style.backgroundColor = 'gray'
        }
    )
    $(this)[0].style.backgroundColor = 'pink'
});
