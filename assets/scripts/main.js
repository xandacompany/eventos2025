AOS.init();

// Función para abrir el menú del celular
function abrir_menu() {
    document.getElementById('menu_celular').style.display = 'flex';
}





// Función para cerrar el menú del celular
function cerrar_menu() {
    document.getElementById('menu_celular').style.display = 'none';
}

const menuItems = document.querySelectorAll('.nav-1-ul .nav-1-li a');
const contenedorMenu = document.querySelector('.contenedor-menu-celular-main');

contenedorMenu.innerHTML = ''; // Limpiar el contenedor antes de agregar los nuevos elementos

menuItems.forEach(item => {
    // Crea el div contenedor de la opción
    const div = document.createElement('div');
    div.classList.add('menu-celular-opciones');
    
    // Crea el enlace
    const enlace = document.createElement('a');
    enlace.href = item.href;  // Copia el enlace
    enlace.textContent = item.textContent;  // Copia el texto del enlace
    
    // Agregar el enlace al div
    div.appendChild(enlace);
    
    // Agregar el div al contenedor
    contenedorMenu.appendChild(div);
    
    // Agregar un eventListener al enlace para cerrar el menú cuando se haga clic
    enlace.addEventListener('click', () => {
        cerrar_menu();  // Llama a la función para cerrar el menú
    });
});





// Función para manejar la visibilidad del menú en función del tamaño de la ventana
function ajustarMenu() {
    const menuCelular = document.getElementById('menu_celular');
    
    if (window.innerWidth > 800) {
        // Si la ventana es más grande que 800px, ocultamos el menú
        menuCelular.style.display = 'none';
    } else {
        // Si la ventana es menor o igual a 800px, dejamos el menú según el estado de la variable
        if (menuCelular.style.display === 'flex') {
            // Si el menú está visible, lo mantenemos visible
            menuCelular.style.display = 'flex';
        } else {
            // Si no está visible, lo dejamos oculto
            menuCelular.style.display = 'none';
        }
    }
}

ajustarMenu();

window.addEventListener('resize', ajustarMenu);