function toDark() {
    var element = document.getElementById("claro")
    if (element.classList == "light-mode") {
        element.classList.replace("light-mode", "dark-mode");
    }

    else {
        element.classList.replace("dark-mode", "light-mode")
    }
}