// api endpojt
var api_url = `/api/${current_page}`

// Fix api url for all data
if (api_url.includes("all")) {
    api_url = "/api/"
}

// Get form
const form = document.querySelector('form')

// Update submit event
form.addEventListener('submit', async (e) => {
    // Dont submit form
    e.preventDefault()

    // Show loading screen
    show_loading ()

    // ------------------
    // API DATA
    // ------------------

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
    console.log (api_data)


    // ------------------
    // RESULTS TABLE
    // ------------------
    
    // Clean last results
    const tbody = document.querySelector ("tbody")
    tbody.innerHTML = ""

    // insert rows
    for (row of api_data["data"]) {
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

    console.log (api_data)


    // ------------------
    // PAGINATION
    // ------------------

    // const nav = document.querySelector('#pagination')
    // const nav_ul = nav.querySelector('ul')

    // // Clen paginations last content
    // nav_ul.innerHTML = ""

    // // Calculate and add pages
    // let total_pages = Math.ceil(api_data["data"].length / 20)
    // if (total_pages > 20) {
    //     total_pages = 20
    // }

    // // Generate pages
    // for (let page_num = 1; page_num <= total_pages; page_num++ ) {
    //     // Create and save number page
    //     const page = `<li class="page-item"><button class="page-link">${page_num}</button></li>`
    //     nav_ul.innerHTML += page
    // }

    // // activate pagination
    // nav.classList.remove ("d-none")

    // Hide loading screen
    hide_loading ()
})
