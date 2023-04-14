function toggle() {
    const button = document.querySelector(".head .button");
    const div = document.querySelector("#extra");
    button.addEventListener("click", show());
    function show(){
        if (button.textContent === "More"){
            div.style.display = "block";
            button.textContent = "Less";
        } else if (button.textContent === "Less"){
            div.style.display = "none";
            button.textContent = "More";
        }
    }
}