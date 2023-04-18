function solution(arr){
    let boardInformation = {};

    const numberOfLines = arr.shift();


    for (let index = 0; index < numberOfLines; index++) {
        const boardElement = arr.shift();
        [assignee, taskId, title, taskStatus, estimatedPoints] = boardElement.split(":");

        if (!boardInformation.hasOwnProperty(assignee)){
            boardInformation[assignee] = [{taskId, title, taskStatus, estimatedPoints}]
        } else {
            boardInformation[assignee].push({taskId, title, taskStatus, estimatedPoints});
        }
    }


    for (const line of arr) {
    
        currentLine = line.split(":");
        let command = currentLine[0];
        let assignedPerson = currentLine[1];

        switch (command) {
            case "Add New":
                taskId = currentLine[2];
                title = currentLine[3];
                taskStatus = currentLine[4];
                estimatedPoints = currentLine[5];

                if (!boardInformation.hasOwnProperty(assignedPerson)){
                    console.log(`Assignee ${assignedPerson} does not exist on the board!`);
                    break
                }

                boardInformation[assignedPerson].push({taskId, title, taskStatus, estimatedPoints});

                break;

            case "Change Status":
                currentTaskId = currentLine[2];
                let newStatus = currentLine[3];
                if (!boardInformation.hasOwnProperty(assignedPerson)){
                    console.log(`Assignee ${assignedPerson} does not exist on the board!`);
                    break
                }

                let found = false;

                for (const task of boardInformation[assignedPerson]) {
                    for (const key in task) {
                        if (task[key] === currentTaskId) {
                            task.taskStatus = newStatus;
                            found = true;
                            break
                            
                        }
                    
                    }
                }

                if (!found){
                    console.log(`Task with ID ${currentTaskId} does not exist for ${assignedPerson}!`)
                }

                break;
            
            case "Remove Task":
                let index = currentLine[2];

                if (!boardInformation.hasOwnProperty(assignedPerson)){
                    console.log(`Assignee ${assignedPerson} does not exist on the board!`);
                    break
                }

                if (index >= boardInformation[assignedPerson].length || index < 0){
                    console.log("Index is out of range!");
                    break

                }

                boardInformation[assignedPerson].splice(index, 1);
                break;   
            
       
            default:
                break;
        }

    }

    let toDoTasksTotalPoints = 0;
    let inProgressTasksTotalPoints = 0;
    let codeReviewTasksTotalPoints = 0;
    let doneTasksTotalPoints = 0;


    for (const person in boardInformation) {
        for (const task of boardInformation[person]) {
            if(task.taskStatus === "ToDo"){
                toDoTasksTotalPoints += Number(task.estimatedPoints)
            } else if (task.taskStatus === "In Progress"){
                inProgressTasksTotalPoints += Number(task.estimatedPoints)
            } else if (task.taskStatus === "Code Review"){
                codeReviewTasksTotalPoints += Number(task.estimatedPoints)
            } else if (task.taskStatus === "Done"){
                doneTasksTotalPoints += Number(task.estimatedPoints)
            }
        }
    }

    console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
    console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
    console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
    console.log(`Done Points: ${doneTasksTotalPoints}pts`);

    if(doneTasksTotalPoints >= (toDoTasksTotalPoints + inProgressTasksTotalPoints + codeReviewTasksTotalPoints)){
        console.log("Sprint was successful!")

    } else {
        console.log("Sprint was unsuccessful...")
    }


}

solution([
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1211:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]
);