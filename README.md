# CS50 Final Project: Bubulle, your friendly breathing bubble!

### Video demo: ---

## Introduction
  
Hi, I am VeMBe, and I have been a student-athlete for a couple years now. As a student and as an athlete, one thing I learned is that having a good sleep hygiene is essential to reap the best results from the efforts that you put in, either in your studies or in your sport, and one exercise that helped me get better sleep when it mattered was to do some breathing exercises before going to sleep. In order to do that, I have been using a type of app called "breathing apps", which displays a visual cue (usually a bubble) that shows you when to breathe in and when to breathe out so that you don't have to count in your head and just focus on your breath. 
  
However, after testing several of those breathing apps there was always some feature in them that was bothering me for the use that I had for it: since I use it at night before sleep, it is very important to me that the screen of my phone is as dark as possible so that I don't blind myself with the blue light emitted from screens that would actually prevent me from being sleepy, and even with my phone at the lowest level of brightness possible I felt the design of these apps was just too bright.  

What I needed was an app that was enabled me to do my breathing exercises, but with a design that was almost completely dark: **This idea is what got me to build this app**

## What is Bubulle?

Bubulle is an app that displays a "bubble" that helps you keep the right rhythm for your breathing exercises. With this app, you can select your breathing profile from four different presets, each allowing you to tailor your breathing practice for your personal needs.  
You can do so by going on the "Breathing parameters" page and selecting your preferred breathing profile from the drop down button, and then clicking on "Save changes" to update the breathing profile and be redirected to the homepage. On the homepage, you can see which breathing profile is currently set up.  
Once you're all set, you just have to click on the Start button and start your practice!  
If you want to, you can also change the overall color theme of the webpage by clicking on one of the three buttons at the bottom of each page: there is a Default mode, a classic Dark mode and also a third, special mode call Night mode: this last theme is the reason I wanted to create this app and displays the app with a completely dark background, along with the buttons, words and the bubble being dark gray.  
What is special about this theme? Well, if you happen to have a modern smartphone, chances are that your phone screen has the OLED technology. This type of screen has the advantage of having each pixel being lit independently, which means that a pixel that has to display black will just turn off; and this allows it to have amazing contrasts.  
The strength of Night theme is that it is able to use the properties of OLED displays and make it so that your screen would be almost completely turned off, with only the bubble and the buttons' outlines to be displayed: **this means that using this night mode right before bed would not strain the eyes the way current apps do.**

### The languages used
Bubulle is built using these technologies:
- Python with the Flask framework for handling the backend
- HTML and CSS for rendering the web pages and stylizing them
- Javascript for the interactive components, such as the theme changing buttons

The  bubble was rendered using a simple \<div> that was stylised and animated using CSS  

### How to run the app
In order to run this app, you need to install Flask and Flask-Session by running the following commands:
```
pip install flask
pip install Flask-Session
```
Once you're done installing, you just have to clone the repository to your IDE, then  `cd` into the main directory and run the following command:
```
flask run
```
Your IDE should give you the URL to your local server and after clicking on it you will be redirected to the app's homepage.

### The different files in the app
<br>

#### **app.py**

This is the backbone of the web-app. It contains some boilerplate code to ensure that the application reloads easily during development and it contains three routes:
- "/" renders the homepage with the bubble
- "/parameters" renders the breathing parameters page if it receives a `GET` request. If it receives a `POST` request, this means that the user wants to update the breathing parameters; therefore it will render the homepage with some variables that will impact which breathing profile the bubble will have. This is possible thanks to Jinja, a web template engine that comes with Flask
- "/about" is just a small extra page that basically contains a TL:DR version of what you are reading here.  


#### **style.css**
This stylesheet is probably the most important file of the entire app. Indeed, this is via CSS that I was able to stylize a \<div> and make it look like a bubble, and then animate it using the `animation` property.  
It is also on this sheet that I set up the dark theme and the night theme, by creating a `dark-mode` and a `night-mode` class and changing the color properties of the elements that possessed these classes.  


#### **index.js**
There is not a lot of javascript involved in this project. The two occurrences are for making a Start/Stop button for the bubble animation and to make the color theme buttons.

#### **Templates**
There are a total of four templates in this app:
- layout.html is the base template. It contains the boilerplate code for html files and the global structure for my webpages.
- index.html is the homepage and contains the star of the show: the famous **Bubulle**. There is not much else there since I wanted to make a minimalist app in the first place.
- parameters.html contains a dropdown button to choose the breathing style that you want. This is an html form that posts the desired breathing profile to app.py to be processed and update index.html
- about.html shows a text that explains what this web app is, how to use it and what it's built with.


## Difficulties and shortcomings
With every project comes its set of obstacles, problems and dead-ends. I chose to do this project specifically because it was small enough that I could make it work not matter what, and I hoped that I would not encounter tough problems while building this app: Boy was I wrong.  

### breathing parameters
The first problem was about the bubble animation, and more specifically making the bubble grow and shrink when I wanted to. I didn't know at the time but it turns out that animating things on the web is not easy, and it certainly is NOT intuitive.  

At first I wanted to design the parameters page so that the user could control every parameter: breathing in, holding in, breathing out, holding out. However, after some time spent banging my head against this problem I found out that it was not really possible to do this  without using knowledge that is out of the scope of this project so I re-adjusted this feature to only propose a couple pre-determined profiles.  
This was possible via CSS thanks to the fact that the `animation` property in CSS call an `animation-name`, which in turn holds what we call animation Keyframes which breaks down what your animation does exactly. So, to make the different profiles, I just had to create different animation names which scaled the bubble up and down in different ways. The final touch was to modify the `animation-duration` with a specific duration for each profile.  
The Next hurdle was to make the selected change affect the homepage. Indeed, with CS50 we learned to build what we call a Static Website, and this means that the different webpages are not linked to each other in any way and a change made on one page will not carry over to the next page you visit. I found a workaround by taking out the style of the breathing animation out of the CSS file and passing it into the header of layout.html: That way, I was able to link the parameters page to the homepage via the python backend by posting the selected profile to app.py and have it replace the relevant fields in the CSS in layout.html via Jinja. This use of Jinja inside CSS code makes VS-Code freak out because both use curly-braces but it works fine in the final rendered template.

### Color themes
I encountered a similar problem with the color theme feature as I did with the breathing parameters: they just won't work in different web pages.  
I initially wanted to just use javascript to toggle the dark modes, but it would not work across pages. I then tried to solve this the same way I did for the breathing profiles (by posting the info to app.py and updating the homepage) but it would not work across pages either, which is inconvenient for a color theme.  
In the end, I found a (poor) way around the issue by just... putting the darn buttons on every page. More precisely, I put them on layout.html and that way they would appear on each rendered template. It is clearly not ideal but; after a bit of research, I concluded that really fixing the issue was outside of the scope of what I wanted to do for this project (it involved learning to use cookies or things of that level).

## Potential improvements and new features to implement
Here are some improvements that can be made and features that can be implemented:
- Fixing the color theme changes, by setting up cookies for example. Another way would be to change the rendering pattern of the app to be a single-page app, but that would require an complete overhaul of the project and I don't want it that bad
- Finding a way to have the user choose every parameter for the bubble
- Adding a timer that the user could set up. Once the timer hits zero the bubble would automatically stop its animation
- Making the bubble a bit more lively by stacking animations or changing its design
- The biggest improvement would be to remake the app on Kotlin or Flutter and launch it on the Google Play Store. However, the amount of work required would be significant.

