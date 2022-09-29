// Get loading element
const loading = document.querySelector (".loading") 

function show_loading () {
    // R4move class for hide loading
    loading.classList.remove("d-none")
}

function hide_loading () {
    // Add class for show loading
    loading.classList.add ("d-none")
}