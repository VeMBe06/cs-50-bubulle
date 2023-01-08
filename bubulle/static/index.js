

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

// Then get .breathing class queryselector
var breatheclass = document.querySelector(".breathing")


// Add event listeners
profile1.addEventListener("change", function() {
    console.log("clicked on button 1")
    breatheclass.style.animationName = "breathe1"
    breatheclass.style.animationDuration = 6 + "s"
})

profile2.addEventListener("change", function() {
    breatheclass.style.animationName = "breathe2"
    breatheclass.style.animationDuration = 9 + "s"

})

profile3.addEventListener("change", function() {
    breatheclass.style.animationName = "breathe3"
    breatheclass.style.animationDuration = 14 + "s"

})

profile4.addEventListener("change", function() {
    breatheclass.style.animationName = "breathe4"
    breatheclass.style.animationDuration = 17 + "s"

})


