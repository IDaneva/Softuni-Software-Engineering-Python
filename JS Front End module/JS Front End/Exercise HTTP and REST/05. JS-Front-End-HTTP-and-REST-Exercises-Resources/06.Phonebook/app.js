function attachEvents() {
    const loadButton = document.getElementById("btnLoad");
    const ulPhoneDirectory = document.getElementById("phonebook");
    const  BASE_URL = "http://localhost:3030/jsonstore/phonebook";
    const DELETION_URL = "http://localhost:3030/jsonstore/phonebook/";

    loadButton.addEventListener("click", loadContacts);

    async function loadContacts(){
        ulPhoneDirectory.innerHTML = "";

        let phoneData = await fetch(BASE_URL);
        phoneData = await phoneData.json();

        for (const key in phoneData) {
            let liElement = document.createElement("li");
            liElement.innerHTML = 
            `${phoneData[key]["person"]}:${phoneData[key]["phone"]}
            <button id="delete">Delete</button> 
            <span id="key" style="display: none">${key}</span>`;
            ulPhoneDirectory.appendChild(liElement);
        }
        
        const deleteButton = document.querySelectorAll("#delete");

        for (const button of deleteButton) {
            button.addEventListener("click", deleteEntry);
        }
    }

    async function deleteEntry(){
        const selectedRowToDelete = this.parentElement;
        let id = selectedRowToDelete.lastChild.textContent;

        const httpHeaders = {
            method: "DELETE"
        };

        fetch(`${DELETION_URL}${id}`, httpHeaders).catch();
        loadContacts();    
    }

    const createButton = document.getElementById("btnCreate");
    const nameInputArea = document.getElementById("person");
    const phoneInputArea = document.getElementById("phone");
    

    createButton.addEventListener("click", createEntry)

    async function createEntry(){
        const person = nameInputArea.value;
        const phone = phoneInputArea.value;


        if (!person || !phone) {
            return
        }

        let contact = {person, phone}
        let httpHeaders = {
            method: "POST",
            body: JSON.stringify(contact)
        };
        
        fetch(BASE_URL, httpHeaders)
            .then((res) => res.json()).catch();
    
        nameInputArea.value = "";
        phoneInputArea.value = "";

        loadContacts();
    } 

}

attachEvents();


