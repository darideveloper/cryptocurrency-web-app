// api endpojt
const api_url = '/api/'

// Get form
const form = document.querySelector('form')

// Update submit event
form.addEventListener('submit', async (e) => {
    // Dont submit form
    e.preventDefault()

    // Get form data
    const start_date_elem = document.querySelector('#start-date')
    const end_date_elem = document.querySelector('#end-date')

    const start_date = start_date_elem.value
    const end_date = end_date_elem.value

    // Format data to send to the api
    const data_form = {
        name: current_page,
        start_date: start_date,
        end_date: end_date,
    }

    // Request data from api and wait for it
    const api_response = await fetch(api_url, {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data_form),
    })

    // Convert response to json and wait for it
    api_data = await api_response.json()

    // Filter data to show, with pagination
    const api_data_show = api_data["data"].slice(0,20)

    // UPDATE TABLE
    
    const tbody = document.querySelector ("tbody")
    tbody.innerHTML = '<tbody class="table-group-divider">' // open tbody tag

    // insert rows
    for (row of api_data_show) {
        row = `
        <tr>
            <td >${row[1]}</td>
            <td >${row[2]}</td>
            <td >${row[3]}</td>
            <td >${row[4]}</td>
            <td >${row[5]}</td>
            <td >${row[6]}</td>
            <td >${row[7]}</td>
            <td >${row[8]}</td>
            <td >${row[9]}</td>
        </tr>
        `
        tbody.innerHTML += row
    }

    tbody.innerHTML += '<tbody class="table-group-divider">' // open tbody tag
})
