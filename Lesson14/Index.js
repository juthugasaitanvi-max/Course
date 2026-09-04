//Class is a blueprint for making objects, a class can be used to make multiple objects each having different values of its own.
// Constructor: It's a special method that runs automatically when we create a new object from a class, its used to set up the initial values or properties.
// this keyword: It refers to the specific object currently being used.
// new keyword: It will be used to create a new object.
// Class Methods: They are defined inside a class that describes what object of the class can do. Think of methods as actions the objects knows how to perform.
// Example:

class Car{
    constructor(brand,color,seats){
        this.brand=brand
        this.color=color
        this.seat=seats
    }

    honk(){
        console.log(`${this.brand} says: Beep Beep!`)
    }
}

//const myCar=new Car("Toyota","Gray")
//console.log(myCar.brand)

const myCar=new Car("Kia","Midnight black","7")
myCar.honk()
console.log(myCar.brand)
console.log(myCar.color)
console.log(myCar.seat)


const mynewCar=new Car("Maruti Suzuki","Dark Blue","6 or 7 ") 
mynewCar.honk()
console.log(mynewCar.brand)
console.log(mynewCar.color)
console.log(mynewCar.seat)











