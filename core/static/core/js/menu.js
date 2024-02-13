////////////////////// Codigo para transicion de barra superior al hacer scroll////////////////
const header = document.querySelector('.header');

 window.addEventListener("scroll", function(){
        
        header.classList.toggle("abajo", window.scrollY>0);
    }) 


