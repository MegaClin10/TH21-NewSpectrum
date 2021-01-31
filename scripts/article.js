function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
 }

function pB() {
    rmButton();
}

function nB() {
    rmButton();
}

function cB() {
    rmButton();
}

 function rmButton() {
     var element = document.getElementById("vote-buttons");
     element.innerHTML = "Thank you for your input!";
 }


//this will be given by matthew
articleId = "60165e0a6dc412294b299548";

window.onload = function() {
    getData();
}

 async function getData() {
    articlejson = await fetch(`https://aqueous-wave-82169.herokuapp.com/article/${articleId}`);
    json = await articlejson.json();
    console.log(json);
    auth = json["data"]["0"]["author"];
    title = json["data"]["0"]["title"];
    cont = json["data"]["0"]["content"];
    src = json["data"]["0"]["source"]["name"];
    console.log(auth);
    console.log(title);
    console.log(cont);
    document.getElementById("artname").innerHTML = title;
    document.getElementById("authname").innerHTML = auth;
    document.getElementById("cont").innerHTML = cont;
    document.getElementById("src").innerHTML = src;
 }