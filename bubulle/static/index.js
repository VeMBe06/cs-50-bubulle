

// JS For the start-stop button
// Select elements: start button, bubble
var StartStop = document.getElementById("StartStop");
var bubble= document.getElementById("Bubble");

// Initialize with a first event listener
StartStop.addEventListener("click", Start);

// Start breathing, update event listeners
function Start() {
    bubble.classList.add("breathing");
    StartStop.removeEventListener("click", Start);
    StartStop.addEventListener("click", Stop);
    StartStop.value = "Stop";

}

// Stop breathing, update event listeners
function Stop() {
    bubble.classList.remove("breathing");
    StartStop.removeEventListener("click", Stop);
    StartStop.addEventListener("click", Start);
    StartStop.value = "Start";
}



// JS for the theme change buttons

function defaultmode(){
    bod = document.body;
    bod.className = "";
}

function darkmode(){
    bod = document.body;
    bod.className = "dark-mode";
}

function nightmode(){
    bod = document.body;
    bod.className = "night-mode";
}
