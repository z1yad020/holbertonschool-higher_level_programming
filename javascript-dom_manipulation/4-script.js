document.getElementById("add_item").onclick = () => {
    const ml = document.getElementsByClassName("my_list");
    const nwl = document.createElement("li");
    nwl.innerHTML = "Item";

    ml[0].appendChild(nwl);
};