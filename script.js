// Obtenir le modal
var modal = document.getElementById('id01');

// Lorsque l'utilisateur clique n'importe où en dehors du modal, fermez-le
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
