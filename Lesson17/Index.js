// Form validation:Its a process of making sure that the data a user types into a form is correct before you use it .Example: Checking if a password is long enough, or making sure that the email field is actually an email.

// Example: 
// let password="abce345"
// if (password.length>8){
//     alert("Password is too short")
// }

// Access the form data: Reading what the user typed into an input box. JavaScript uses document.getElementById to find an input by its ID, then .value to get the text inside it.

// Example:
// let name= document.getElementById("name").value;
// let guess= document.getElementById("guess").value;

// Conditions for Validation:  It will use if-e lse statement to check whether a field is correct or not. If the field fails the check, we set a flag to false & show error message to the user.

// let ok=true;
// if(name==" "){
//     ok=false;
// }
// if(ok==true){
//     // continue;
// } 

// Feedback from DOM: It means showing a message on the page to tell the user what is right and wrong.    

// Example:

// document.getElementById('msg').textContent = "Please enter ur name: ";
// document.getElementById('msg').style.color = "red";

// HTML constraints: They are rules we write directly in HTML tag to control what a user can type.
// Timers and Random Numbers: Timers (setInterval() and setTimeout()) let you delay or repeat a code and Random Numbers they come from Math.random(), which will give u random decimals between 0 and 1.



















