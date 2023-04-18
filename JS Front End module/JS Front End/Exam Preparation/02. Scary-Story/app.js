window.addEventListener("load", solve);

function solve() {
  const inputFieldsToFill = Array.from(document.querySelectorAll("input"));
  inputFieldsToFill.pop();
  inputFieldsToFill.push(document.getElementById("story"));



  function checkFilledData(arr){
    allFilled = true;
    for (const input of arr) {
      if (input.value.trim() === ""){
        allFilled = false;
      }
    }
    return allFilled
  }

  const publishButton = document.getElementById("form-btn");

  publishButton.addEventListener("click", previewInformation);

  let storyData = {}

  function previewInformation(){

    if (!checkFilledData(inputFieldsToFill)){
      return
    }

    this.disabled = true;
    const firstNameInput = inputFieldsToFill[0];
    const firstNameInputValue = firstNameInput.value;


    const lastNameInput = inputFieldsToFill[1];
    const lastNameInputValue = lastNameInput.value;


    const ageInput = inputFieldsToFill[2];
    const ageInputValue = ageInput.value;


    const titleInput = inputFieldsToFill[3];
    const titleInputValue = titleInput.value;


    const genreInput = document.getElementById("genre");
    const genreInputValue = genreInput.value;


    const storyInput = inputFieldsToFill[4];
    const storyInputValue = storyInput.value;


    storyData["firstName"] = firstNameInputValue;
    storyData['lastName'] = lastNameInputValue;
    storyData["age"] = ageInputValue;
    storyData["title"] = titleInputValue;
    storyData["genre"] = genreInputValue;
    storyData["story"] = storyInputValue;


    console.log(storyData);


    const previewContainer = document.getElementById("preview-list");
    let liElement = document.createElement("li");
    liElement.className = "story-info"
    liElement.innerHTML = `
      <article>
        <h4>Name: ${storyData["firstName"]} ${storyData["lastName"]}</h4>
        <p>Age: ${storyData["age"]}</p>
        <p>Title: ${storyData["title"]}</p>
        <p>Genre: ${storyData["genre"]}</p>
        <p>${storyData["story"]}</p>
      </article>
      <button class="save-btn">Save Story</button>
      <button class="edit-btn">Edit Story</button>
      <button class="delete-btn">Delete Story</button>
    `

    firstNameInput.value = "";
    lastNameInput.value = "";
    ageInput.value = "";
    titleInput.value = "";
    genreInput.value = "";
    storyInput.value = "";

    previewContainer.appendChild(liElement);

    const editStoryButton = document.getElementsByClassName("edit-btn")[0];
    editStoryButton.addEventListener("click", editStory);

    const saveStoryButton = document.getElementsByClassName("save-btn")[0];
    saveStoryButton.addEventListener("click", saveStory)

    const deleteStoryButton = document.getElementsByClassName("delete-btn")[0];
    deleteStoryButton.addEventListener("click", deleteStory)

  }

  
  function editStory(){
    publishButton.removeAttribute("disabled");
    const firstNameInput = inputFieldsToFill[0];
    firstNameInput.value = storyData["firstName"];

    const lastNameInput = inputFieldsToFill[1];
    lastNameInput.value = storyData["lastName"];

    const ageInput = inputFieldsToFill[2];
    ageInput.value = storyData["age"];

    const titleInput = inputFieldsToFill[3];
    titleInput.value = storyData["title"];

    const genreInput = document.getElementById("genre");
    genreInput.value = storyData["genre"];

    const storyInput = inputFieldsToFill[4];
    storyInput.value = storyData["story"];

    const previewContainer = document.getElementById("preview-list");
    previewContainer.innerHTML = "<h3>Preview</h3>";
  }


  function saveStory(){
    divSaveSection = document.getElementById("main");
    divSaveSection.innerHTML = "<h1>Your scary story is saved!</h1>"
  }

  function deleteStory(){
    publishButton.removeAttribute("disabled");
    const previewContainer = document.getElementById("preview-list");
    previewContainer.innerHTML = "<h3>Preview</h3>";
  }

}
