function utenti()
{
    let email = document.getElementById("InputEmail").value
    let pass = document.getElementById("InputPassword").value

    if(email == "emma@gmail.com" && pass == "emma")
    {
        Notification(brava)
    }
}
function Notification(messaggio) {
    let divMessaggio = document.getElementById("messaggio")
    divMessaggio.innerHTML = messaggio

    //tolgo il d-none per mostrare il div
    divMessaggio.classList.remove("d-none")

    //per mostrare il div rosso
    divMessaggio.classList.add("alert-danger")
}