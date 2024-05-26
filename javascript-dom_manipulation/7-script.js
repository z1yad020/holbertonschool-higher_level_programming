fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then((fullfill) => fullfill.json())
        .then((fullfill) => {
            const ml = document.getElementById("list_movies");
            
            for (res of fullfill.results) {
                const nwl = document.createElement("li");

                nwl.innerText = `"${res.title}"`;
                ml.appendChild(nwl);
            }
        });