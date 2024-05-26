fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
        .then((fullfill) => fullfill.json())
        .then((fullfill) => document.getElementById("character").innerText = fullfill.name);