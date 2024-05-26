fetch("https://hellosalut.stefanbohacek.dev/?lang=az")
        .then((fullfill) => fullfill.json())
        .then((fullfill) => {
            const ml = document.getElementById("hello");
            ml.innerText = fullfill.hello;
        });