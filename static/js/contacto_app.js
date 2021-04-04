//Varibles
const botonReset=document.querySelector('#resetBtn');
const botonEnviar=document.querySelector('#enviar');
const email=document.querySelector('#correo');
const nombre=document.querySelector('#nombre');
const mensaje=document.querySelector('#mensaje');
const formulario=document.querySelector('#enviar-mail');

const er=/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

IniciandoEventos();
function IniciandoEventos(){

    document.addEventListener('DOMContentLoaded',IniciarApp)

    email.addEventListener('blur',validarFormulario);
    nombre.addEventListener('blur',validarFormulario);
    mensaje.addEventListener('blur',validarFormulario);

    formulario.addEventListener('submit',enviandoCorreo);
    botonReset.addEventListener('click',reiniciarFormulario);
}

//funciones
function IniciarApp(){
  botonEnviar.disabled=true;
  botonEnviar.classList.add('cursor-not-allowed','opacity-50');

}
function validarFormulario(e){

  if(e.target.value.length > 0){
    const quitarErrores = document.querySelector('p.error');
    if(quitarErrores){
      quitarErrores.remove();
    }
    e.target.classList.remove('border', 'border-red-500');
    e.target.classList.add('border', 'border-green-500');


  }else{
    e.target.classList.remove('border', 'border-green-500');
    e.target.classList.add('border', 'border-red-500');
    mostrarError('Debes insertar todos los campos son obligatorios');
  }
  if(e.target.type === 'email'){

    if(er.test(e.target.value)){
       const quitarErrores = document.querySelector('p.error');
       if(quitarErrores){
          quitarErrores.remove();
         }
       e.target.classList.remove('border', 'border-red-500');
       e.target.classList.add('border', 'border-green-500');

    }else{
      e.target.classList.remove('border', 'border-green-500');
      e.target.classList.add('border', 'border-red-500');
      mostrarError('Correo de email no valido');
    }
  }
  if(er.test(email.value) && nombre.value !=='' && mensaje.value !==''){
    botonEnviar.disabled=false;
    botonEnviar.classList.remove('cursor-not-allowed','opacity-50');
  }else{
    botonEnviar.disabled=true;
    botonEnviar.classList.add('cursor-not-allowed','opacity-50');
  }
}
function mostrarError(mensaje){
  const errores=document.createElement('p');
        errores.textContent=mensaje;
        errores.classList.add('border','border-red-500','background-red-100','text-red-500','p-3','mt-5','text-center','error');
        const error=document.querySelectorAll('.error');
        if(error.length === 0){
          formulario.appendChild(errores);
        }

}
function enviandoCorreo(e){
  e.preventDefault();
  console.log("Enviando correo");
  const spiner =document.querySelector('#spinner');
  spiner.style.display='flex';
  setTimeout( () => {
          spiner.style.display='none';
          const parrafo=document.createElement('p');
          parrafo.textContent='Mensaje enviado con exito';
          parrafo.classList.add('text-center','my-10','p-2','bg-green-500','text-white','font-bold','uppercase')
          formulario.insertBefore(parrafo,spiner);




           setTimeout( ()=>{
               parrafo.remove();
               reiniciarFormulario();
             },3000)


  },3000)

}

function reiniciarFormulario(){
  formulario.reset();
  IniciarApp();
}