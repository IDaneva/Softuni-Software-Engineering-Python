function addItem() {
    const ulContainer = document.getElementById("items");
    const input = document.getElementById("newItemText");
    const newLi = document.createElement("li");
    newLi.textContent = input.value;
    ulContainer.appendChild(newLi);
    input.value = "";
    linkToDelete = document.createElement("a");
    linkToDelete.textContent = "[Delete]"
    linkToDelete.setAttribute("href", "#");
    Array.from(document.querySelectorAll("#items li")).forEach((l) => {l.appendChild(linkToDelete);});
    linkToDelete.addEventListener("click", (e) => {
        const anchor = e.currentTarget;
        anchor.parentElement.remove();
    })
}