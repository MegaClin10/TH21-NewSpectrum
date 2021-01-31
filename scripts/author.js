window.onload = function() {
    getData();
}

//this will be given by matthew
articleId = "60165e0a6dc412294b299548";

 async function getData() {
    articlejson = await fetch(`https://aqueous-wave-82169.herokuapp.com/article/${articleId}`);
    json = await articlejson.json();
    console.log(json);
    auth = json["data"]["0"]["author"];
    title = json["data"]["0"]["title"];
    desc = json["data"]["0"]["description"];
    src = json["data"]["0"]["source"]["name"];
    console.log(auth);
    console.log(title);
    console.log(desc);
    document.getElementById("artname").innerHTML = title;
    document.getElementById("authname").innerHTML = auth;
    document.getElementById("desc").innerHTML = desc;
    document.getElementById("src").innerHTML = src;
 }