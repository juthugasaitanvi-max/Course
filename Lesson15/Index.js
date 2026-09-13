//Checking Data types using typeof 
//Think of typeof as a magic magnifying glass.Point it at anything and it will tell you what kind of thing it is.(A number,a text or a string, a true or false etc.)
 
// let age = 10
// console.log(typeof age) 
// let name = "Tanvi"
// console.log(typeof name)

//Converting Data Types:JavaScript has 2 built-in functions that can convert data types: Number() and String().

// let age = 10
// let age1 = String(age) 
// console.log(typeof age)
// console.log(typeof age1)

// let name1 = "Tanvi"
// let name2 = Number(name1)
// console.log(typeof name1)
// console.log(typeof name2)

//Searching and Replacing Text:JavaScript has 2 built-in functions that can search and replace text: search() and replace().

// let sentence = "I love JavaScript"
// sentence.search("love") 
// sentence.search ("HTML")
// console.log(sentence.search("love"))
// console.log(sentence.replace("JavaScript", "Science"))

//To handle errors JavaScript has a built-in error handling mechanism called try...catch. The try statement allows you to define a block of code to be tested for errors while it is being executed. The catch statement allows you to define a block of code to be executed, if an error occurs in the try block.

let userInput = "a";
try {
let n = Number(userInput);
  if (isNaN(n)) { throw "Please type a valid number!"; }
  console.log(100 / n);
} catch(err) {
  console.log("Error: " + err);
}





































































































































































