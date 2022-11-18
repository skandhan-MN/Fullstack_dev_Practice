// Set of statements that perfoms a task or calculates a value

// Declare a function using functon key workd

// (function keyword) function(name of the function)greet and followed by paranthesis ()
// and the body of the function { inside this curly braces }

// function greet() {
//   console.log("helloworld");
// }
// greet();

// function greet(name) {
//   console.log("hello", name);
// }
// greet("skandhan");

// in the above function name =paraeter and skandhan is the argument(input )

// +++++++++++++++++++++++++++++++++++++++++++
// call back function
// ==========================================

const button = document.querySelector("button");

function toggle() {
  button.classList.toggle("altColor");
}
toggle();
