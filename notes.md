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

### let var const and scopes

- ES2015 introduced two important new JavaScript keywords: let and const.These two keywords provide Block Scope variables (and constants) in JavaScript.Before ES2015, JavaScript had only two types of scope: Global Scope and Function Scope.

- Global Scope__Variables declared Globally (outside any function) have Global Scope.Global variables can be accessed from anywhere in a JavaScript program.

- var carName = "Volvo";
- // code here can use carName
- function myFunction() {
-  // code here can also use carName
- }

- Local Scope__


