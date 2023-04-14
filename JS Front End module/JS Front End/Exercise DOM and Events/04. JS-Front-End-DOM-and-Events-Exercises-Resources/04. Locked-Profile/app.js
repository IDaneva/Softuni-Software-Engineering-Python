function lockedProfile() {
    const buttons = Array.from(document.querySelectorAll("button"));
    const radioButtons = Array.from(document.querySelectorAll(".profile input[type='radio']"))

    buttons.forEach(b => b.addEventListener("click", show));
    function show(e){
        const button = e.target;
        const profile = button.parentNode
        const unlockRadioButton = profile.querySelector("[value^='unlock']")

        if (unlockRadioButton.checked) {
            const hiddenDiv = button.parentNode.querySelector("div")
            if (button.textContent === "Show more"){
                hiddenDiv.style.display = "block";
                button.textContent = "Hide it";
                } else {
                hiddenDiv.style.display = "none";
                button.textContent = "Show more";
                }
        }
    }
}