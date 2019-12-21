numeral.register('locale', 'cl', { delimiters: { thousands: '.', decimal: ',' }})
numeral.locale('cl')

function addUrlParameter(name, value) {
    var searchParams = new URLSearchParams(window.location.search)
    searchParams.set(name, value)
    window.location.search = searchParams.toString()
}

function parseCLP(name) {
    productsPrice = document.getElementsByName(name)

    productsPrice.forEach(function(item) {
        itemPrice = parseInt(item.dataset.price)
        item.innerHTML = "$" + numeral(itemPrice).format()
    })
}