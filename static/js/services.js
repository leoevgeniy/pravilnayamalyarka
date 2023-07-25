if (location.pathname.includes('services')) {
const meters_minus = document.getElementById('meters-minus')
const meters_plus = document.getElementById('meters-plus')
const meters_qty = document.getElementById('meters-quantity')
let meters_amount = 1
meters_minus.onclick = function (e) {
    const qty = Number(meters_qty.value)
    if (qty > 1) {
        meters_qty.value = String(qty - 1)
        meters_amount = qty - 1
        upd()
    }
}
meters_plus.onclick = function (e) {
    const qty = Number(meters_qty.value)
    meters_qty.value = String(qty + 1)
    meters_amount = qty + 1
    upd()
}
meters_qty.onchange = (e) => {
    meters_amount = Number(e.target.value)
    upd()
}
let cost = 325
const objtype = document.getElementById('object_type')
objtype.childNodes.forEach(item => {
    if (item.classList && item.classList.value === 'form-check')
    {

        item.onchange = (e) => {
            cost = Number(e.target.dataset['cost'])
            upd()
        }

    }

})
const covers = document.getElementById('cover_type')
let koeff = 1
covers.childNodes.forEach(item => {
    // if ('form-check' in item.classList)
    if (item.classList && item.classList.value === 'form-check')
    {

        item.onchange = (e) => {
            koeff = Number(e.target.dataset['cost'])
            upd()
        }

    }

})

const total_cost = document.getElementById('total_cost')
const upd = () => {
    total_cost.innerText = String(cost * meters_amount * koeff) + ' р.'
}
upd()}