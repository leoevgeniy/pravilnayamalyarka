// let iOS = navigator.userAgent.match(/iPhone|iPad|iPod/i);
// let event = "click";
//
// if(iOS != null)
//     event = "touchstart";

$(function() {
    $(document).on(event, ".element_class", function(e) {
        //действия
    });
});
const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('cart');
const myModal = new bootstrap.Modal('#cartmodal', {

})

if (myParam === '1') {
    myModal.show()
}
// myModal.onclose(e=> {
//     location.replace('/category')
// })
function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('element-show');
        }
    });
}

let options = {
    threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');

for (let elm of elements) {
    observer.observe(elm);
}

$('.select_location').on('change', function(){
    window.location = $(this).val();
});


// $(document).ready(function() {
//     $("#lightSlider").lightSlider({
//         item: 5,
//         autoWidth: false,
//
//         slideMove: 2, // slidemove will be 1 if loop is true
//         slideMargin: 5,
//
//         addClass: '',
//         mode: "slide",
//         useCSS: true,
//         cssEasing: 'ease', //'cubic-bezier(0.25, 0, 0.25, 1)',//
//         easing: 'linear', //'for jquery animation',////
//
//         speed: 400, //ms'
//         auto: true,
//         loop: true,
//         slideEndAnimation: false,
//         pause: 2000,
//
//         keyPress: false,
//         controls: true,
//         prevHtml: '',
//         nextHtml: '',
//
//         rtl:false,
//         adaptiveHeight:false,
//
//         vertical:false,
//         verticalHeight:100,
//         vThumbWidth:100,
//
//         thumbItem:10,
//         pager: true,
//         gallery: false,
//         galleryMargin: 5,
//         thumbMargin: 5,
//         currentPagerPosition: 'middle',
//
//         enableTouch:true,
//         enableDrag:true,
//         freeMove:true,
//         swipeThreshold: 40,
//
//         responsive : [],
//
//         onBeforeStart: function (el) {},
//         onSliderLoad: function (el) {},
//         onBeforeSlide: function (el) {},
//         onAfterSlide: function (el) {},
//         onBeforeNextSlide: function (el) {},
//         onBeforePrevSlide: function (el) {}
//     });
// });
// $(document).ready(function() {
//     $("#lightSlider_work_landscape").lightSlider({
//         item: 5,
//         autoWidth: false,
//
//         slideMove: 2, // slidemove will be 1 if loop is true
//         slideMargin: 5,
//
//         addClass: '',
//         mode: "slide",
//         useCSS: true,
//         cssEasing: 'ease', //'cubic-bezier(0.25, 0, 0.25, 1)',//
//         easing: 'linear', //'for jquery animation',////
//
//         speed: 600, //ms'
//         auto: true,
//         loop: true,
//         slideEndAnimation: false,
//         pause: 3000,
//
//         keyPress: false,
//         controls: true,
//         prevHtml: '',
//         nextHtml: '',
//
//         rtl:false,
//         adaptiveHeight:false,
//
//         vertical:false,
//         verticalHeight:100,
//         vThumbWidth:100,
//
//         thumbItem:10,
//         pager: true,
//         gallery: false,
//         galleryMargin: 5,
//         thumbMargin: 5,
//         currentPagerPosition: 'middle',
//
//         enableTouch:true,
//         enableDrag:true,
//         freeMove:true,
//         swipeThreshold: 40,
//
//         responsive : [],
//
//         onBeforeStart: function (el) {},
//         onSliderLoad: function (el) {},
//         onBeforeSlide: function (el) {},
//         onAfterSlide: function (el) {},
//         onBeforeNextSlide: function (el) {},
//         onBeforePrevSlide: function (el) {}
//     });
// });
// $(document).on("click.bs.dropdown.data-api", ".noclose", function (e) { e.stopPropagation() });
// window.onload = () => {
//     updateQty()
// }
// window.onpopstate = () => {
//     updateQty()
// }
// // window.history.pushState('', null, './');
updateQty()
//
//
//
//
//
//
//
//
