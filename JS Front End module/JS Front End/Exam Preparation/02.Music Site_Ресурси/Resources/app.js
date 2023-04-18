window.addEventListener('load', solve);

function solve() {
    const genreInput = document.getElementById("genre");
    const nameOfSongInput = document.getElementById("name");
    const authorOfSongInput = document.getElementById("author");
    const creationDateInput = document.getElementById("date");
    const totalLikesParagraph = document.querySelector(".likes p");
    let likes = 0;

    const inputFields = [genreInput, nameOfSongInput, authorOfSongInput, creationDateInput];
    const addButton = document.getElementById("add-btn");



    addButton.addEventListener("click", addSong);

    function addSong(event){
        if (event){
            event.preventDefault();
        }

        if (!checkFilledData(inputFields)){
            console.log("ERRORRRR")
            return
        }
        let genre = genreInput.value;
        let nameOfSong = nameOfSongInput.value;
        let authorOfSong = authorOfSongInput.value;
        let creationDate = creationDateInput.value;

        for (const inputField of inputFields) {
            inputField.value = "";
            
        }

        const divContainer = document.getElementsByClassName("all-hits-container")[0];
        let currentSongContainer = document.createElement("div");
        currentSongContainer.classList.add("hits-info");
        currentSongContainer.innerHTML = `
            <img src="./static/img/img.png">
            <h2>Genre: ${genre}</h2>
            <h2>Name: ${nameOfSong}</h2>
            <h2>Author: ${authorOfSong}</h2>
            <h2>Date: ${creationDate}</h2>
            <button class="save-btn">Save song</button>
            <button class="like-btn">Like song</button>
            <button class="delete-btn">Delete</button>
        `
        let save = currentSongContainer.getElementsByClassName("save-btn")[0];
        save.addEventListener("click", saveSong);
        let like = currentSongContainer.getElementsByClassName("like-btn")[0];
        like.addEventListener("click", likeSong);
        let deleteB = currentSongContainer.getElementsByClassName("delete-btn")[0];
        deleteB.addEventListener("click", deleteSong);
        divContainer.appendChild(currentSongContainer);
    }

    function saveSong(){
        const songRef = this.parentNode;
        const savedContainer = document.getElementsByClassName("saved-container")[0];
        savedContainer.appendChild(songRef);
    }

    function likeSong(){
        likes += 1;
        totalLikesParagraph.textContent = `Total Likes: ${likes}`;
        this.setAttribute("disabled", true);
    }

    function deleteSong(){
        const songContainer = this.parentNode;
        songContainer.remove();
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

}