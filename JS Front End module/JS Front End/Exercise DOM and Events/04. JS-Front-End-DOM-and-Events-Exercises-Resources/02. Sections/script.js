function create(words) {
   for (const word of words) {
      const newDiv = document.createElement("div");
      const paragraph = document.createElement("p");
      paragraph.textContent = word;
      paragraph.style.display = "none";
      newDiv.appendChild(paragraph);
      const containerDiv = document.getElementById("content");
      containerDiv.appendChild(newDiv);
      newDiv.addEventListener("click", () =>paragraph.style.display = "block");
   };
}