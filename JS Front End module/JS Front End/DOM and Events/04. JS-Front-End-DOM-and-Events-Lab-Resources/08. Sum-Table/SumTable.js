function sumTable() {
    const costs = Array.from(document.querySelectorAll("table tbody tr td:nth-child(even")).slice(0,3);
    const button = document.querySelector("button");
    button.addEventListener("click", giveResult());
    function giveResult(){
        let sum = 0;
        for (const n of costs) {
            sum += Number(n.textContent);
        }
        cell = document.querySelector("#sum");
        cell.textContent = String(sum);
    }
}

