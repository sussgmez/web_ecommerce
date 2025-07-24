function hideAll(element=undefined) {
    let items = htmx.findAll('.menu-xs')

    
    items.forEach(item => {
        if (item != element) {
            htmx.addClass(item, 'hidden-xs')
        }  
    });
}

function showPrice(element, price, discount) {
    if (element != null)
        element.innerHTML = Intl.NumberFormat('en-us', { style: "currency", currency: "USD" }).format((price-price*discount/100))
}