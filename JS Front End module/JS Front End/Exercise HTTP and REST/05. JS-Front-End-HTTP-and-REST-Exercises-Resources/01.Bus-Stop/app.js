function getInfo() {
    const inputField = document.getElementById("stopId");
    const BASE_URL = "http://localhost:3030/jsonstore/bus/businfo/";
    const stopId = inputField.value;
    const stopName = document.getElementById("stopName");
    const ul = document.getElementById("buses");

    ul.innerHTML = "";
    fetch(`${BASE_URL}${stopId}`)
        .then((res) => res.json())

        .then((busInfo) => {
            const {buses, name} = busInfo;
            stopName.textContent = name;
            for (const busID in buses) {
                let li = document.createElement("li");
                li.textContent = `Bus ${busID} arrives in ${buses[busID]} minutes`
                ul.appendChild(li);
            }
            })
    
        .catch(stopName.textContent = "Error");
}