function dm() {
    var body = document.body;
    body.classList.toggle("dark-mode");

    var searchBar = document.getElementById("search-bar");
    searchBar.classList.toggle("search-bar-dark");

    var text = document.getElementsByClassName("dm-text");
    for(var i = 0; i < text.length; i++){
		text[i].classList.toggle("dark-mode-text");
    }
}
