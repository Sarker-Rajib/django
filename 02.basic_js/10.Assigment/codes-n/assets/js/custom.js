fetch("https://openapi.programming-hero.com/api/videos/categories")
    .then(res => res.json())
    .then(data => {
        const categories = data.data;
        console.log(categories);
        const buttonWrapper = document.getElementById("button-wrapper")
        categories.forEach(element => {
            const button = document.createElement('button')
            button.innerText = element.category
            button.classList.add("button-custom")
            button.addEventListener('click', () => {
                alert(`${element.category_id}`);
            })
            buttonWrapper.appendChild(button)
        })

    })