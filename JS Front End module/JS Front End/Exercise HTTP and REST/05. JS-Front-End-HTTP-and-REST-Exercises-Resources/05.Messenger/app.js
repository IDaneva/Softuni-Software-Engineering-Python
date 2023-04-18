function attachEvents() {
    const nameInputSpace = document.querySelectorAll("#controls div input")[0];
    const messageInputSpace = document.querySelectorAll("#controls div input")[1];
    const sendButton = document.getElementById("submit");
    const refreshButton = document.getElementById("refresh");

    const BASE_URL = "http://localhost:3030/jsonstore/messenger"

    sendButton.addEventListener("click", sendEvent);
    refreshButton.addEventListener("click", refreshEvent);

    async function sendEvent(){

        const author = nameInputSpace.value;
        const content = messageInputSpace.value;

        const httpHeaders = {
            method: "POST",
            body: JSON.stringify({author, content})
        };

        try{

        fetch (BASE_URL, httpHeaders)
            .then((res) => res.json())
            .then((data)=> console.log(data));

        nameInputSpace.value = "";
        messageInputSpace.value = "";
        }
        catch (err){}
    }


    async function refreshEvent(){
        const messageArea = document.getElementById("messages");
        messageArea.value = ""
        try {
        let messageData = await fetch(BASE_URL);
        messageData = await messageData.json();

        for (const key in messageData) {
            messageArea.value += `${messageData[key]["author"]}: ${messageData[key]["content"]}\n`
        }
        }

        catch (err ){

        }


        
    }
}

attachEvents();