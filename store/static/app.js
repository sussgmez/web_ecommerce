function display(name_obj) {
    const obj = document.querySelector(name_obj)
    obj.classList.remove('hide')
}

function close(name_obj) {
    const obj = document.querySelector(name_obj)
    obj.classList.add('hide')
}

function display_or_close(name_obj) {
    const obj = document.querySelector(name_obj)
    if (obj.classList.contains('hide')) {
        obj.classList.remove('hide')
    } else {
        obj.classList.add('hide')
    }  
}

function closeAll() {
    const navbar = document.querySelector('.navbar')
    const login = document.querySelector('.login')

    navbar.classList.add('hide')
    login.classList.add('hide')
}

function changeImage(imagen_url) {
    const image_max = document.querySelector('.img_max')
    image_max.attributes['src'].value = imagen_url

    const min_images = document.querySelectorAll('.im-min')
    min_images.forEach(element => {
        element.classList.remove('active')
    });
}

const btn_navbar = document.querySelector('.icon-navbar')
btn_navbar.addEventListener('click', () => {
    close('.login')
    display_or_close('.navbar')
}) 

try {
    const btn_login = document.querySelector('.option-login')
    btn_login.addEventListener('click', () => {
        close('.navbar')
        display_or_close('.login')
    })  
} catch (error) {} 

try {
    const filter = document.querySelector('.filtro-tag')
    filter.addEventListener('click', () => {display_or_close('.filters')})  
} catch (error) {}

try {
    const min_images = document.querySelectorAll('.im-min')
    min_images.forEach(element => {
        element.addEventListener('mouseover', () => 
        {
            changeImage(element.attributes['src'].value)
            element.classList.add('active')
        })
    });
} catch (error) {}

try {
    const section = document.querySelectorAll('.section')
    section.forEach(element => {
        element.addEventListener('click', closeAll)
    });
} catch(error) {}

try {
    const login = document.querySelector('.login');
    if (login.classList.contains('no-hide')) {
        login.classList.remove('hide')
    }
} catch (error) {}