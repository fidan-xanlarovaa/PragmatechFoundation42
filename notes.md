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

'''
var x = 2;       // Allowed
let x = 3;       // Not allowed

{
  var x = 4;   // Allowed
  let x = 5   // Not allowed
}
'''
- Redeclaring a let variable with var, in the same scope, or in the same block, is also not allowed:

- Variables defined with let are hoisted to the top of the block, but not initialized.**Meaning: The block of code is aware of the variable, but it cannot be used until it has been declared.**Using a let variable before it is declared will result in a ReferenceError. But contarary to let **var** variables **can be used** before it declared.

- JavaScript const variables must be assigned a value when they are declared: 

- Incorrect:
'''
const PI;
PI = 3.14159265359;
'''
- Correct: ''' const PI = 3.14159265359; '''

- You can change the elements of a constant array, but you can NOT reassign a constant object.



### Functions

-





