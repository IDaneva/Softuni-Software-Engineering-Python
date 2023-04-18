function shoppingList(shopArr){
    let initialList = shopArr.shift();
    initialList = initialList.split("!");
    
    
    while (true){
        line = shopArr.shift();

        if (line === "Go Shopping!"){
            break
        }

        line = line.split(" ");

        let command = line[0];
        let item = line[1];

        switch (command) {
            case "Urgent":

                if (!initialList.includes(item)){
                    initialList.unshift(item);
                }

                break;

            case "Unnecessary":

                if (initialList.includes(item)){
                    let index = initialList.indexOf(item);
                    initialList.splice(index, 1);
                }

                break;
            
            case "Correct":
                let newItem = line[2];

                if (initialList.includes(item)){
                    let index = initialList.indexOf(item);
                    initialList[index] = newItem;
                }

                break;   
            
            case "Rearrange":
                if (initialList.includes(item)){
                    let index = initialList.indexOf(item);
                    initialList.splice(index, 1);
                    initialList.push(item);
                }
                break;  
        
            default:
                break;
        }

    }

    console.log(initialList.join(", "))

}

shoppingList(["Milk!Pepper!Salt!Water!Banana",

"Urgent Salt",

"Unnecessary Grapes",

"Correct Pepper Onion",

"Rearrange Grapes",

"Correct Tomatoes Potatoes",

"Go Shopping!"])