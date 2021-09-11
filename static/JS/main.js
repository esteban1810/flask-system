

function mostrarCedula(){
    if(document.getElementById('medico').value === '2'){
        document.getElementById('cedula').style.display = 'block';
    }
}

function ocultarCedula(){
    if(document.getElementById('administrador').value === '1'){
        document.getElementById('cedula').style.display = 'none';
    }
}


function validarPassword(){
    if(document.getElementById('confPass').value != document.getElementById('pass').value){
        alert("Las contraseñas no coinciden");
        return false;
    }
}