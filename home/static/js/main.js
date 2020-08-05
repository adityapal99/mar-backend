function border() {    
    const elements = document.querySelectorAll(".form-notch");
    console.log(elements.item);

    elements.forEach(function(item) {
        item.classList.remove("form-notch");
    });
}

border();