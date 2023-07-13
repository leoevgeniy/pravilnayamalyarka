
    const catalog_small = document.getElementById('catalog_small')
    catalog_small.addEventListener('click', () => {
        const catalog_items_small = document.getElementById('catalog_items_small')

        if (catalog_small.dataset.clecked === 'false') {
            catalog_small.dataset.clecked =  'true'
            catalog_items_small.classList.remove('d-none')
        } else {
            console.log(catalog_small.getAttribute('data-clecked'))
            catalog_small.dataset.clecked = 'false'
            catalog_items_small.classList.add('d-none')
        }


    })
