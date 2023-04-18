function solve() {
    const info = document.querySelector('.info')
    const [departBtn, arriveBtn] = document.querySelectorAll('input')
    const apiURL = 'http://localhost:3030/jsonstore/bus/schedule/'
    let [departId, departLocation] = ['depot', null]



    async function depart() {
        let data = await fetch(`${apiURL}${departId}`)
        data = await data.json()

        departLocation = data['name']
        info.textContent = `Next stop ${departLocation}`
        departId = data['next']
        departBtn.disabled = true
        arriveBtn.disabled = false
    }

    async function arrive() {
        info.textContent = `Arriving at ${departLocation}`
        departBtn.disabled = false
        arriveBtn.disabled = true

    }


    return {
        depart,
        arrive
    };
}

let result = solve();