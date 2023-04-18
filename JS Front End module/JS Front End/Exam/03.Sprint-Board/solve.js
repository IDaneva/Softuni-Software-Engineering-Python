// TODO:
function attachEvents() {
    const loadAllButton = document.getElementById("load-board-btn");
    loadAllButton.addEventListener("click", loadServerEntries);
    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const toDoSectionList = document.querySelector("#todo-section .task-list");
    const inProgressSectionList = document.querySelector("#in-progress-section .task-list");
    const codeReviewSectionList = document.querySelector("#code-review-section .task-list");
    const doneSectionList = document.querySelector("#done-section .task-list");

    const addTaskButton = document.getElementById("create-task-btn");
    addTaskButton.addEventListener("click", addTaskToServer);
    const taskTitleInput = document.getElementById("title");
    const descriptionInput = document.getElementById("description");
    let containers = [toDoSectionList, inProgressSectionList, codeReviewSectionList, doneSectionList];

    async function loadServerEntries(){

        for (const iterator of containers) {
            iterator.innerHTML = "";
        }

        try {
            const serverResponse = await fetch(BASE_URL);
            let taskData = await serverResponse.json();
            console.log(taskData);
            let info = Object.values(taskData);
            let liElement = null;
            for (const key in info) {
                console.log(info[key]);

                if (info[key].status === "ToDo"){
                    liElement = document. createElement("li");
                    liElement.classList.add("task")
                    liElement.id = info[key]._id;
                    liElement.innerHTML = `
                        <h3>${info[key].title}</h3>
                        <p>${info[key].description}</p>
                        <button>Move to In Progress</button>
                    `
                    let moveProgressButton = liElement.getElementsByTagName("button")[0];
                    moveProgressButton.addEventListener("click", moveToInProgress);
                    toDoSectionList.appendChild(liElement);

                } else if (info[key].status === "In Progress"){

                    liElement = document. createElement("li");
                    liElement.classList.add("task")
                    liElement.id = info[key]._id;
                    liElement.innerHTML = `
                        <h3>${info[key].title}</h3>
                        <p>${info[key].description}</p>
                        <button>Move to Code Review</button>
                    `
                    let moveReviewButton = liElement.getElementsByTagName("button")[0];
                    moveReviewButton.addEventListener("click", moveToReview);
                    inProgressSectionList.appendChild(liElement);

                } else if (info[key].status === "Code Review"){

                    liElement = document. createElement("li");
                    liElement.classList.add("task")
                    liElement.id = info[key]._id;
                    liElement.innerHTML = `
                        <h3>${info[key].title}</h3>
                        <p>${info[key].description}</p>
                        <button>Move to Done</button>
                    `
                    let moveDoneButton = liElement.getElementsByTagName("button")[0];
                    moveDoneButton.addEventListener("click", moveToDone);
                    codeReviewSectionList.appendChild(liElement);
                    
                } else if (info[key].status === "Done"){

                    liElement = document. createElement("li");
                    liElement.classList.add("task")
                    liElement.id = info[key]._id;
                    liElement.innerHTML = `
                        <h3>${info[key].title}</h3>
                        <p>${info[key].description}</p>
                        <button>Close</button>
                    `
                    doneSectionList.appendChild(liElement);
                    
                }

            }

            
        } catch (error) {
            console.error(error);
        }
    }

    async function addTaskToServer(){
        let title = taskTitleInput.value;
        let description = descriptionInput.value;
        let status = "ToDo";

        const httpHeaders = {
            method: "POST",
            body: JSON.stringify({title, description, status})
        }

        await fetch(BASE_URL, httpHeaders);
        loadServerEntries();
        taskTitleInput.value = "";
        descriptionInput.value = "";

    }

    async function moveToInProgress(){
        let container = this.parentNode;
        let idToEdit = container.id
        let status = "In Progress";

        const httpHeaders = {
            method: "PATCH",
            body: JSON.stringify({status})
        }

        await fetch(`${BASE_URL}${idToEdit}`, httpHeaders);

        loadServerEntries();

    }

    async function moveToReview(){
        let container = this.parentNode;
        let idToEdit = container.id
        let status = "Code Review";

        const httpHeaders = {
            method: "PATCH",
            body: JSON.stringify({status})
        }

        await fetch(`${BASE_URL}${idToEdit}`, httpHeaders);

        loadServerEntries();
    }

    async function moveToDone(){
        let container = this.parentNode;
        let idToEdit = container.id
        let status = "Done";

        const httpHeaders = {
            method: "PATCH",
            body: JSON.stringify({status})
        }

        await fetch(`${BASE_URL}${idToEdit}`, httpHeaders);

        loadServerEntries();
    }
}

attachEvents();