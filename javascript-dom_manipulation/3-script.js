document.getElementById("toggle_header").onclick = () => {
    const el = document.querySelector("header");
    if (el.getAttribute("class") === "green") el.setAttribute("class", "red");
    else el.setAttribute("class", "green");
};