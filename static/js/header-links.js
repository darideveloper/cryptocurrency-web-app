// get header elements
const nav_items = document.querySelectorAll (".nav-item")

// Disbale current button
for (const nav_item of nav_items) {
    const link = nav_item.querySelector ("a")
    const content = link.innerHTML.toLocaleLowerCase()

    if (content.includes(current_page)) {
        link.classList.add ("disabled")
    }
}