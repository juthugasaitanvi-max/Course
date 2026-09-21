// JSON stands for JavaScript Object Notation. It is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. JSON is often used to transmit data between a server and a web application as text.
// Example: 
let data={ name:"Saitanvi",class:"7th",age:10}

// JSON.stringify(): It's a built in JS function that turns a JS object into text(string). Apps use stringify data everytime they need to store or share data.

let jsonText=JSON.stringify(data )

// JSON.parse(): It's like a partner to JSON.stringify, it takes JSON string and turns it back into JSON or JavaScript Object. Every app that receives data from the internet uses JSON.parse(). If we want to show the data on the browser we use JSON.parse().

let loaderData=JSON.parse(jsonText)

// setTimeout(): Its a built in function that waits a set number of milliseconds and then runs a functions.

setTimeout(function(){
    // .....
})
 
