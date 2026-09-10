//let Short_forms=['IDK','GTG','BRB','LOL']
//Short_forms.sort()      
//Short_forms.reverse()         
//console.log(Short_forms)
//.sort()-Arranges items alphabetically by default that is a to z

// let numbers=[1,2,3,4,5,6]
// numbers.reverse()
// console.log(numbers)
// .reverse()- it just flips the whole order.

// Sorting number: To simply sort numbers we give .sort() a little instruction known as 'comparator'. (a-b):Smallest fist & (b-a):Biggest first.       
// Example:
// let numbers=[40,30,14,25,45,78,5,67,29,44,15]

// numbers.sort((a,b)=>b-a)
// console.log(numbers)  

// Mapping an array: Transforms the whole array into a brand new array by running a function on each and every item.
// let numbers=[1,2,3,4,5,6]
// let double=numbers.map(num=>num*2)
// console.log(double)

let names=["Sahithi","Ekta","Anu",'Simran']
let withTitles=names.map(name=>"Ms. "+name)

console.log(withTitles)
