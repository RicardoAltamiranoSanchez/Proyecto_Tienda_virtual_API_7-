document.getElementById("btn__iniciar-sesion").addEventListener("click", InciarSesion);

document.getElementById("btn__registrarse").addEventListener("click", register);

//Varibles
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var caja_trasera_login = document.querySelector(".caja__trasera_login");
var caja_trasera_register = document.querySelector(".caja__trasera_register");

var formulario_login = document.querySelector(".formulario__login");
var fomulario_register = document.querySelector(".formulario__register");

function InciarSesion() {
    fomulario_register.style.display = "none";
    contenedor_login_register.style.left = "10px";
    formulario_login.style.display = "block";
    caja_trasera_register.style.opcity = "1";
    caja_trasera_login.style.opacity = "0";
}

function register() {
    fomulario_register.style.display = "block";
    contenedor_login_register.style.left = "410px";
    formulario_login.style.display = "none";
    caja_trasera_register.style.opcity = "0";
    caja_trasera_login.style.opacity = "1";
}