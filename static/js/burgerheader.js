
try {
    const offcanvas_menu = document.getElementById('offcanvasRight')
    const burger = document.getElementById('burgermenu')

    offcanvas_menu.addEventListener('shown.bs.offcanvas', (e) => {
            const searchinput = document.getElementById('search-input')
            const searchbutton = document.getElementById('offcanvassearchbutton')
            searchbutton.click()
            searchinput.focus()
            searchbutton.click()

        }
    )
} catch {}