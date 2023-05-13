window.onload = init;
let request;


function init() {
    request = new XMLHttpRequest();
    request.open("POST", "manageVille.php",true);

    }

function traitementReponse() {
    console.log(request.readyState + "" + request.status);
    if(request.readyState == 4 && request.status == 200){
        window.location = 'manageVille.php'
        console.log("cc")

    }
}

function filtreObjet(colonne){
    open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    console.log(colonne)
    let data = new FormData();
    data.append("filtrePar",colonne);
    request.send(data);
    request.onreadystatechange = traitementReponse; 
}