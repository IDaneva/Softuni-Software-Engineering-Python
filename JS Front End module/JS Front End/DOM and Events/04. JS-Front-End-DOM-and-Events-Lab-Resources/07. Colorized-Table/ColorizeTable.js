function colorize() {
    const rows = document.querySelectorAll("table tr:nth-child(even)");
    const button = document.querySelector("button").addEventListener("click", doTheColor());
    function doTheColor(){
        Array.from(rows).forEach((row) =>{row.style.backgroundColor ="teal"});
    }
}