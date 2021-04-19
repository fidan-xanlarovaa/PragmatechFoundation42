### Value = undefined
- In computer programs, variables are often declared without a value. The value can be something that has to be calculated, or something that will be provided later, like user input.A variable declared without a value will have the value undefined.The variable carName will have the value undefined after the execution of this statement.

### example1

- var x = "5" + 2 + 3;  // answer is 523

### Variable naming

- Remember that JavaScript identifiers (names) must BEGIN with:
- A letter (A-Z or a-z)
- A dollar sign ($)
- Or an underscore (_)
- Since JavaScript treats a dollar sign as a letter, identifiers containing $ are valid variable names: 

- var $$$ = "Hello World";
- var $ = 2;
- var $myMoney = 5;
- var a2 = "Hello World";
- var _money = 2;
- var height = 5;

```
var b; // declare a variable
b=5; asign a value to variable b
```



### LET , VAR , CONST AND SCOPES

- ES2015 introduced two important new JavaScript keywords: let and const.These two keywords provide Block Scope variables (and constants) in JavaScript.Before ES2015, JavaScript had only two types of scope: Global Scope and Function Scope.

- Global Scope__Variables declared Globally (outside any function) have Global Scope.Global variables can be accessed from anywhere in a JavaScript program.

```
 var carName = "Volvo";
// code here can use carName
 function myFunction() {
  // code here can also use carName
 }
```

- Local Scope__Variables declared Locally (inside a function) have Function Scope.Local variables can only be accessed from inside the function where they are declared.

```
// code here can NOT use carName

function myFunction() {
  var carName = "Volvo";
  // code here CAN use carName
}

// code here can NOT use carName
```

Block Scope:

- Variables declared with the var keyword cannot have Block Scope.Variables declared inside a block {} can be accessed from outside the block.

```
{
  var x = 2;
}
// x CAN be used here
```

- Variables declared with the let keyword can have Block Scope.Variables declared inside a block {} cannot be accessed from outside the block:

```
{
  let x = 2;
}
// x can NOT be used here

```

- Redeclaring a var variable with let, in the same scope, or in the same block, is not allowed:

```
var x = 2;       // Allowed
let x = 3;       // Not allowed

{
  var x = 4;   // Allowed
  let x = 5   // Not allowed
}
```
- Redeclaring a let variable with var, in the same scope, or in the same block, is also not allowed:

- Variables defined with let are hoisted to the top of the block, but not initialized.**Meaning: The block of code is aware of the variable, but it cannot be used until it has been declared.**Using a let variable before it is declared will result in a ReferenceError. But contarary to let **var** variables **can be used** before it declared.

- JavaScript const variables must be assigned a value when they are declared: 

- Incorrect:
```
const PI;
PI = 3.14159265359;
```
- Correct: ``` const PI = 3.14159265359; ```

- You can change the elements of a constant array, but you can NOT reassign a constant object.


##### Differences between let var and const

- var declarations are globally scoped or function scoped while let and const are block scoped.
- var variables can be updated and re-declared within its scope; let variables can be updated but not re-declared; const variables can neither be updated nor re-declared.
- They are all hoisted to the top of their scope. But while var variables are initialized with undefined, let and const variables are not initialized.
- While var and let can be declared without being initialized, const must be initialized during declaration.



### Functions

- Function parameters are listed inside the parentheses () in the function definition.Function arguments are the values received by the function when it is invoked.
- The () Operator Invokes the Function. Accessing a function without () will return the function object instead of the function result. 


# JavaScript objects are containers for named values called properties or methods. ??????????

### Objects

- This code assigns many values (Fiat, 500, white) to a variable named car:
``` var car = {type:"Fiat", model:"500", color:"white"}; ```

- The name:values pairs in JavaScript objects are called properties

- You can access object properties in two ways: ``` objectName.propertyName ``` - ``` person.lastName; ``` , ``` objectName["propertyName"] ``` - ``` person["lastName"]; ```The difference is in how x is interpreted. When using a dot, the word after the dot is the literal name of the property. When using square brackets, the expression between the brackets is evaluated to get the property name. Whereas value.x fetches the property of value named “x”, value[x] tries to evaluate the expression x and uses the result, converted to a string, as the property name.
 
- Objects Methods___Objects can also have methods.Methods are actions that can be performed on objects.Methods are stored in properties as function definitions. A method is a function stored as a property.
``` 
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```


### Classes

- A JavaScript class is not an object.It is a template for JavaScript objects.Class methods are created with the same syntax as object methods.Use the keyword class to create a class.Always add a constructor() method.Then add any number of methods.
```
```

```
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    let date = new Date();
    return date.getFullYear() - this.year;
  }
}
```


### Arrays

- The elements in an array are stored as the array’s properties, using numbers as property names. Because you can’t use the dot notation with numbers and usually want to use a binding that holds the index anyway, you have to use the bracket notation to get at them.

### Hoca veren methodlar

#### document.getElementById(id)
- The Document method getElementById() returns an Element object representing the element whose id property matches the specified string. Since element IDs are required to be unique if specified, they're a useful way to get access to a specific element quickly.
- void function, id-si olan elementin uzerinde yazilan emelleri gorur
- teleb etdiyi arqument elemetlerin id-sidir
- EXAMPLE:
- HTML
```
<html>
<head>
  <title>getElementById example</title>
</head>
<body>
  <p id="para">Some text here</p>
  <button onclick="changeColor('blue');">blue</button>
  <button onclick="changeColor('red');">red</button>
</body>
</html>
```

- JS
```
function changeColor(newColor) {
  var elem = document.getElementById('para');
  elem.style.color = newColor;
}
```

- Result
- Some text here

```blue```   ``` red```


#### document.getElementsByTagName(name)
#### document.getElementsByClassName(name)


#### document.querySelector()

- return function
- The Document method querySelector() returns the first Element within the document that matches the specified selector, or group of selectors. If no matches are found, null is returned.Between () we should rite the selector which we want to find. 
```var el = document.querySelector(".myclass");```
- A more complex selector ```var el = document.querySelector("div.user-panel.main input[name='login']");```
- This will select an input with a parent div with the user-panel and the main class.
- Negation
As all CSS selector strings are valid, you can also negate selectors:
```var el = document.querySelector("div.user-panel:not(.main) input[name='login']");```
- This will select an input with a parent div with the user-panel class but not the main class.

#### document.querySelectorAll()

- same as document.querySelector() but returns not only first but all elements  that matches the specified selector


#### document.createElement(element)
- creates the element which we write between(" ").


#### node.removeChild(element)
```
let d = document.getElementById("top");
let d_nested = document.getElementById("nested");
let throwawayNode = d.removeChild(d_nested);
```

#### node.appendChild(element)

- The Node.appendChild() method adds a node to the end of the list of children of a specified parent node. If the given child is a reference to an existing node in the document, appendChild() moves it from its current position to the new position (there is no requirement to remove the node from its parent node before appending it to some other node).
```
// Create a new paragraph element, and append it to the end of the document body
let p = document.createElement("p");
document.body.appendChild(p);
```
#### document.replaceChild(new, old)
#### document.write(text)
- element.addEventListener
- onclick event 
- onload event
- element.style object

#### document.querySelectorAll().length
- eyni adda nece element var mueyyen edir


### Some notes
- arguments[1] rezerv key worddur