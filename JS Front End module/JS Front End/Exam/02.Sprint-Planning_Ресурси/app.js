window.addEventListener('load', solve);

function solve() {
    const titleInput = document.getElementById("title");
    const descriptionInput = document.getElementById("description");
    const label = document.getElementById("label");
    const estimationPointsInput = document.getElementById("points");
    const assigneeInput = document.getElementById("assignee");

    const createTaskButton = document.getElementById("create-task-btn");
    createTaskButton.addEventListener("click", addSprintTask);
    const deleteTaskButton = document.getElementById("delete-task-btn");
    deleteTaskButton.setAttribute("disabled", true);

    const inputFields = [titleInput, descriptionInput, label, estimationPointsInput, assigneeInput]

    const taskContainer = document.getElementById("tasks-section");
    let points = 0;
    let currentId = 0;

    const labelCodes = {
        "Feature" : '&#8865',
        "Low Priority Bug": "&#9737",
        "High Priority Bug": "&#9888"
    }

    const labelClasses = {
        "Feature" : 'feature',
        "Low Priority Bug": "low-priority",
        "High Priority Bug": "high-priority"
    }

    function addSprintTask(event){
        if (event){
            event.preventDefault();
        }

        if (!checkFilledData(inputFields)){
            console.log("ERRORRRR")
            return
        }
        currentId += 1;

        let newArticle = document.createElement("article");
        newArticle.id = `task-${currentId}`;
        newArticle.classList.add("task-card");

        newArticle.innerHTML = `
            <div class="task-card-label">${label.value} ${labelCodes[label.value]}</div>
            <h3 class="task-card-title">${titleInput.value}</h3>
            <p class="task-card-description">${descriptionInput.value}</p>
            <div class="task-card-points">${estimationPointsInput.value}</div>
            <div class="task-card-assignee">${assigneeInput.value}</div>
            <div class="task-card-actions">
                <button>Delete</button>
            </div>
        `
        let divWithLabel = newArticle.getElementsByClassName("task-card-label")[0];
        divWithLabel.classList.add(`${labelClasses[label.value]}`);
        let deleteButtonInTaskContainer = newArticle.querySelector("div.task-card-actions button");
        deleteButtonInTaskContainer.addEventListener("click", deleteFromContainer);

        taskContainer.appendChild(newArticle);

        points += Number(estimationPointsInput.value);
        console.log(points)

        document.getElementById("total-sprint-points").textContent = `Total Points ${points}pts`


        for (const iterator of inputFields) {
            iterator.value = "";
        }


    }


    function checkFilledData(arr){
        allFilled = true;
        for (const input of arr) {
          if (input.value.trim() === ""){
            allFilled = false;
          }
        }
        return allFilled
      }

    function deleteFromContainer(){
        let taskInfo = this.parentNode.parentNode;
        const hiddenId = document.getElementById("task-id");
        hiddenId.value = taskInfo.id;

        createTaskButton.setAttribute("disabled", true);
        deleteTaskButton.removeAttribute("disabled");
        deleteTaskButton.addEventListener("click", deleteGenerally);

        let titleFromContainer = taskInfo.getElementsByClassName("task-card-title")[0];
        let descriptionFromContainer = taskInfo.getElementsByClassName("task-card-description")[0];
        let labelFromContainer = taskInfo.getElementsByClassName("task-card-label")[0];
        let pointsFromContainer = taskInfo.getElementsByClassName("task-card-points")[0];
        let assigneeFromContainer = taskInfo.getElementsByClassName("task-card-assignee")[0];

        let text = labelFromContainer;
        // text = text.split(" ");
        console.log(text);

        titleInput.value = titleFromContainer.textContent;
        descriptionInput.value = descriptionFromContainer.textContent;
        label.value = "Feature";
        estimationPointsInput.value = pointsFromContainer.textContent;
        assigneeInput.value = assigneeFromContainer.textContent;


        for (const iterator of inputFields) {
            iterator.setAttribute("disabled", true);
        }
    }

    function deleteGenerally(){
        const hiddenId = document.getElementById("task-id");
        let elementToDelete = document.querySelector(`#${hiddenId.value}`);
        let selectedPoints = Number(estimationPointsInput.value);
        points -= selectedPoints;
        document.getElementById("total-sprint-points").textContent = `Total Points ${points}pts`


        elementToDelete.remove();
        for (const iterator of inputFields) {
            iterator.removeAttribute("disabled");
            iterator.value = "";
        }
        deleteTaskButton.setAttribute("disabled", true);
        createTaskButton.removeAttribute("disabled");

    }

}