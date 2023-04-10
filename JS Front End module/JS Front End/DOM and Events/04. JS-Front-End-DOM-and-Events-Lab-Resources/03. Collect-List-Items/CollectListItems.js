function extractText() {
    const liElements = Array.from(document.querySelectorAll("#items li"));
    const results = document.querySelector("#result");
    liElements.forEach((li) => results.textContent += li.textContent + "\n")
}
