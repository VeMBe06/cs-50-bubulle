

// JS For the start-stop button
// Select elements: start button, bubble
var StartStop = document.getElementById("StartStop")
var bubble= document.getElementById("Bubble")

// Initialize with a first event listener
StartStop.addEventListener("click", Start)

// Start breathing, update event listeners
function Start() {
    bubble.classList.add("breathing")
    StartStop.removeEventListener("click", Start)
    StartStop.addEventListener("click", Stop)
    StartStop.value = "Stop"

}

// Stop breathing, update event listeners
function Stop() {
    bubble.classList.remove("breathing")
    StartStop.removeEventListener("click", Stop)
    StartStop.addEventListener("click", Start)
    StartStop.value = "Start"
}




// Set up breathing parameters buttons
// First get buttons ids
var profile1 = document.getElementById("profile1")
var profile2 = document.getElementById("profile2")
var profile3 = document.getElementById("profile3")
var profile4 = document.getElementById("profile4")

// Add event listeners
profile1.addEventListener("click", param("profile1"))
profile2.addEventListener("click", param("profile2"))
profile3.addEventListener("click", param("profile3"))
profile4.addEventListener("click", param("profile4"))

// param() function
function param(str) {
    // Check if there's already a breathing profile
}

