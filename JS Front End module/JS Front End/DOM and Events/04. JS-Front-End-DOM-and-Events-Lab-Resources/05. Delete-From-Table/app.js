function deleteByEmail() {
    const emailAddress = document.querySelector("body label input").value;
    let tableAddresses = Array.from(document.querySelectorAll("#customers tr td"))
        .map((t) => t.textContent)
        .filter((t) => t.includes("@"));

    if (!(tableAddresses.includes(emailAddress))) {
        document.getElementById("result").textContent = "Not found.";
    } else {
        let foundElement = Array.from(document.getElementsByTagName("td")).find(t =>t.textContent === emailAddress);
        let row = foundElement.parentElement;
        row.parentElement.removeChild(row);
        document.getElementById("result").textContent = "Deleted.";
        document.querySelector("body label input").value = "";
    }
}