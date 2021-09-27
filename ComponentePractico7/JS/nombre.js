function validar_formulario() {
    var nombre = document.getElementById("txtNombre");
    var apellido = document.getElementById("txtApellido");
    var email = document.getElementById("txtEmail");
    var password = document.getElementById("txtPassword");

    if (nombre.value.length == 0 || nombre.value.length < 8) {
        alert(
            "El nombre de usuario es un campo requerido y debe tener más de 8 caracteres"
        );
        return false;
    }

    var formato_email =
        /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    if (!email.value.match(formato_email)) {
        alert("Correo electronico no valido");
        return false;
    }

    if (password.value.length == 0 || password.value.length < 8) {
        alert("Correo electronico no valido");
        return false;
    }
}

window.addEventListener("DOMContentLoaded", function () {
    var img = document.getElementById("imgPassword");
    var password = document.getElementById("txtPassword");
    img.addEventListener("mouseover", (event) => {
        var password = document.getElementById("txtPassword");
        password.type = "text";
        img.src = "images/eyes_cross.png";
    });

    img.addEventListener("mouseout", (event) => {
        var password = document.getElementById("txtPassword");
        password.type = "password";
        img.src = "images/eye.png";
    });
});
