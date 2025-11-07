var form = document.querySelector("form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    var email = document.getElementById("email").value;
    var senha = document.getElementById("senha").value;
    
    if (email === "maycon@dental.com.br" && senha === "senha123") {
        window.location.href = "dashboard.html";
    } else {
        alert("Email ou senha incorretos!");
    }
});

var logoutBtn = document.getElementById("logout");
logoutBtn.addEventListener("click", function(event) {
    event.preventDefault();
    var modal = document.getElementById("modal");
    var cancelarBtn = document.getElementById("cancelar");
    var confirmarBtn = document.getElementById("confirmar");
    
    modal.style.display = "block";
    
    cancelarBtn.addEventListener("click", function() {
        modal.style.display = "none";
    });
    
    confirmarBtn.addEventListener("click", function() {
        window.location.href = "index.html";
    });
});





// -----------------------------|REVELAR SENHA NO REGISTER|---------------------------------//

