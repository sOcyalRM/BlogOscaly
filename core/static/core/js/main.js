
//Ejecutando funciones
document.getElementById("icon-search").addEventListener("click", mostrar_buscador);
document.getElementById("cover-ctn-search").addEventListener("click", ocultar_buscador);
document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

//Ocultar contenido al pulsar esc
document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
      document.getElementById("cover-ctn-search").classList.toggle(ocultar_buscador());
    }
  });

//Declarando variables

bars_search = document.getElementById("ctn-bars-search");       //Variable con la que se recibe la barra de busqueda como un todo
cover_ctn_search = document.getElementById("cover-ctn-search"); //Variable en la que se almacena el cover oscuro
inputSearch = document.getElementById("inputSearch");           //Variable en la que se almacena los valores de la busqueda
box_search = document.getElementById("box-search");             //Variable en la que se almacena los valores de la caja de sugerencias


//Funcion para mostrar el buscador 
function mostrar_buscador(){
    bars_search.style.top= "2px";
    cover_ctn_search.style.display = "block"; //Muestra el cover oscuro al mostrar buscador
    inputSearch.focus();                        // Hace que en la barra de busqueda se haga disponible la escritura 

    if(inputSearch.value === ""){
        box_search.style.display = "none"
    }
}

//Funcion para ocultar el buscador
function ocultar_buscador(){
    bars_search.style.top = "-120px"; //Oculta la barra de busqueda enviandola 120 px hacia arriba
    cover_ctn_search.style.display = "none"; // Oculta el cover oscuro cambiando su display a none
    inputSearch.value = "";                 //Hace que los caracteres en la barra de busqueda desaparezcan al desactivar
    box_search.style.display = "none";      // Hace desaparacer las sugerencias en la caja de busqueda al salir de busqueda
}


//Creando filtrado de busqueda

function buscador_interno(){
    filter = inputSearch.value.toUpperCase();   //Se almacenan los valores de busqueda y se convierten a mayuscula
    li = box_search.getElementsByTagName("li"); //Se almancenan los elementos li

    //Recorriendo elementos a filtrar mediante los "li"

    for (i=0; i<li.length; i++){                //Se iteran los elementos li

        a = li[i].getElementsByTagName("a")[0]; //Se almacenan en a los elementos <a> 
        textValue = a.textContent || a.innerText;

        if(textValue.toUpperCase().indexOf(filter) > -1){

            li[i].style.display = "";
            box_search.style.display = "block";

            if(inputSearch.value === ""){
                box_search.style.display = "none"
            }

        }else{
            li[i].style.display = "none"; //Continuar aqui
        }
    }
}


///////////////////////////////////Section para manejar Ventana Modal//////////////////////////////

const openModal = document.querySelector('.btn_modal');
const modal = document.querySelector('.modal')
const closeModal = document.querySelector('.modal_close')
document.getElementById("cover_modal").addEventListener("click", escape_modal);

document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        modal.classList.remove('modal--show');
    }
  });


openModal.addEventListener('click', (e) =>{
    e.preventDefault();
    modal.classList.add('modal--show');
});
 
closeModal.addEventListener('click', (e) =>{
    e.preventDefault();
    modal.classList.remove('modal--show');
});


//Funcion para ocultar modal
function escape_modal(){
    modal.classList.remove('modal--show');
}


