function validarDato(){
    // usuario administrador
    var contraseña = document.getElementById("contraseña").value;
    var correo = document.getElementById("correo").value;

        var correo1="admin@grupocero.cl";
        var contraseña1="admin123";
        
        var correo2="programador@grupocero.cl";
        var contraseña2 ="prog123";
       
        var correo3="dueño@grupocero.cl";
        var contraseña3="dueño123";
     


    //funcion para validar si los datos son correctos
    if (correo == correo1 | correo == correo2 | correo == correo3 && contraseña ==contraseña1 |
         contraseña ==contraseña2 | contraseña ==contraseña3) {
        alert("Todo esta correcto");
        window.location.href = "../Index_sesion_iniciada.html"
    } else {
        alert("El correo o la contraseña no son validos");
    }
}