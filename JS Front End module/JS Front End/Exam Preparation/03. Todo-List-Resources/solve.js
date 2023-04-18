function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const loadAllButton = document.getElementById("load-button");
    const addButton = document.getElementById("add-button");
    const ulContainer = document.getElementById("todo-list");

    loadAllButton.addEventListener("click", loadEntries);
    addButton.addEventListener("click", addEntries);

    async function loadEntries(event){
        if (event){
            event.preventDefault();
        }

        ulContainer.innerHTML = "";

        try {
            let data = await fetch(BASE_URL);
            let json = await data.json();

            if (Object.keys(json).length === 0) {
            console.error("Empty JSON response");
            } else {
            for (const iterator in json) {

                let liElement = document.createElement("li");
                liElement.innerHTML = `
                    <span>${json[iterator].name} </span>
                    <span class="hidden" style="display: none">${json[iterator]._id}</span>
                    <button id="remove">Remove</button>
                    <button id="edit">Edit</button>
                `
                ulContainer.appendChild(liElement);

                };
            }
        } catch (err) {
            console.error(err);
        }

        const removeButtons = Array.from(document.querySelectorAll("#remove"));
        const editButtons = Array.from(document.querySelectorAll("#edit"));
    
        for (const removeBtn of removeButtons) {
            removeBtn.addEventListener("click", removeEntry);
        }

        for (const editBtn of editButtons) {
            editBtn.addEventListener("click", editEntries);
        }

    }


    async function removeEntry(){
        const selectedRow = this.parentElement;
        const idToDelete = selectedRow.children[1].textContent.trim();

        const headers ={
            method: "DELETE",
        };

        try{
            let data = await fetch(`${BASE_URL}${idToDelete}`, headers);
            console.log(idToDelete);
            console.log(data);
            loadEntries();

        }
        catch (err){
            console.error(err);
        }

    }

    async function addEntries(event){
        if (event){
            event.preventDefault();
        }

        const inputField = document.getElementById("title");
        const name = inputField.value;


        const httpHeaders = {
            method: "POST",
            body: JSON.stringify({name})
        }

        await fetch(BASE_URL, httpHeaders).then((res) => res.json());

        loadEntries();
        inputField.value = "";
    }

    let idToEdit = null;

    async function editEntries(event){

        const selectedRow = this.parentElement;
        let spanElement = selectedRow.getElementsByTagName("span")[0];
        // const hiddenIdElement = selectedRow.getElementsByTagName("span")[1];
        // idToEdit = hiddenIdElement.textContent;

        let content = spanElement.textContent;
        spanElement.remove();

        let inputField = document.createElement("input");
        inputField.value = content; 
        selectedRow.prepend(inputField);

        idToEdit = inputField.value;
        this.textContent = "Submit";
        this.addEventListener("click", submitEditedEntry);

    }

    async function submitEditedEntry(){
        const selectedRow = this.parentElement;
        let inputField = selectedRow.getElementsByTagName("input")[1];
        let content = inputField.value;

        console.log(idToEdit);
        console.log(content)

        const headers ={
            method: "PATCH",
            body: JSON.stringify({"name": content})
        };

        try{
            let data = await fetch(`${BASE_URL}${idToEdit}`, headers);
            data = await data.json();
            loadEntries();
        }
        catch (err){
            console.error(err);
        }
    }

}

attachEvents();
