// // ========================================
// //Conditional statements
// //==========================================

// // const num = -5;
// // // if (conditon) {
// // //     Write the code that will be excuted only if the condition is true
// // // }
// // if (num > 0) {
// //   console.log("Number is positive ");
// // } else if (num < 0) {
// //   console.lgo("Number is negative ");
// // } else {
// //   console.log("Number is zero");
// // }
// // // //Sometimes u may want to run differnt block of code if the condition evaluates to false in such
// // // case we make use of the else statement
// // // else {
// // //   console.log("number is Negative ");

// // // if you have just two blocks of code to run IF and else statement is sufficent
// // // how ever if you decide to have more that two conditions u will need else if statement

// // const num = 0;

// // if (num > 0) {
// //   console.log("This is a positive number");
// // } else if (num < 0) {
// //   console.log("This is a Neagitive numeber");
// // } else {
// //   console.log("This number is Zeror ");
// // }

// //if you have large number of choices and little code to execute in each choice a switch statement is better suited

// // const color= "red"
// // switch(Value or and expression){
// //     you can specify one or more cases

// //     case "red":
// //         console.log(print)
// //         break key word will prevent from next case to be executed

// // }

// // const color = "blue";
// // switch (color) {
// //   case "red":
// //     console.log("color is red");
// //     break;
// //   case "green":
// //     console.log("color is green");
// //     break;
// //   case "blue":
// //     console.log("Color is blue");
// // }
// // const color = "10";
// // //Switch statement evaluates the expression with in the parenthesis
// // switch (color) {
// //   // and Excutes the code corrosponding to the matching case
// //   case "green":
// //     console.log("GO ");
// //     break;
// //   case "red":
// //     console.log("Stop");
// //     break;
// //   case "orange":
// //     console.log("move");
// //     break;
// //   // if there is no matching case the default case will be executed
// //   default:
// //     console.log("Not a valid color");
// // }

// // ========================================
// //lOOPING CODE
// //==========================================

// // for(initializer; condition; final-expression){
// //     code to run
// // }

// // for (i = 1; i <= 5; i++) {
// //   // Condition to loag a message five times
// //   console.log("iteration number" + i); //concanitated with the value of variable i
// // }

// //Initializer i=1( I is set to a value of one )
// // Condition i<=5( if I is less than or equal to 5)
// //The code inside the curly braces is executed
// //Final Expression i++( I is incremented by 1 )
// //now i==2 , next it checks the condition if i is <=5 , again the code inside the curly braces is executed
// // I is increnemted by 1 now I==3 the loop runs and executes the code for 4,5
// // after loging the 5th message  i is incrementd to 6 now the condition (i<=5) evaluates to false because i <=5 not 6
// //When the condition becoems false teh lope is terminated

// //While Loop

// /* INITIALIZER
// WHILE(CONDITION){
//     //cODE TO RUN
//     FINAL EXPRESSION
// }*/

// let i = 1;
// while (i <= 5) {
//   console.log(" Increment by" + i);
//   i++;
// }

// let i = 1;
// while (i <= 5) {
//   console.log("iteration number" + i);
//   i++;
// }

/* let i = 1;
while (i <= 2) {
  console.log("iterate" + i);
  i++;
}*/

//Do. while loop

/* initializer
do{
  //code to run
  final-expression
} while(condition)*/

// let i = 6; // do while executes the code atleast once and then evaluates the condition
// do {
//   console.log("Iteration numner" + i);
//   // Since 6 is greater than 5 the loop is terminated after loging teh message
//   i++;
// } while (i <= 5);

// for..of loop: mainly used to loop over a collection of data [array for example]

// for(const item of array){
//   //code to run
// }

// const numArray = [1, 2, 3, 4, 5];
// for (const num of numArray) {
//   console.log("iteration number" + num);
// }
// for off loop automatically iterates over the array , in each iteration assigns the value
//of the array element to num

//functions

//Synatax

// function name(parameter1, parameter2, parametere3){
//   //code to be executed
// }

// function greet() {
//   console.log("Good morning skandhan");
// }
// greet();// invoking the function

// what if the name is dynamic

// function greet(userName) {
//   // input userName is called parameter
//   console.log("good morning " + userName);
// }
// greet("skandhan"); // when invocing function (skandhan,revathi, natarajan) are called function arguments
// greet("Revathi");
// greet("Natarajan");

// function add(a, b) {
//   return a - b;
//   return a + b;
//   //return is a js key word which will return the value of the function(add) when we invoke it
// }
// const sum = add(5, 10);
// console.log(sum);
// const sub = add(25, 30);
// console.log(sub);

// function mul(a, b) {
//   return a * b;
// }
// const result = mul(25, 10);
// console.log(result);

// arrow functions

// const arrowSum = (a, b) => a + b;
// const sum = arrowSum(3, 4);
// console.log(sum);

// const multiply = (a, b) => a * b;
// const result = multiply(3, 3);
// console.log(result);

for (i = 1; i <= 5; i++) {
  console.log("iterate num" + i);
}

i = 1;
while (i <= 4) {
  console.log("iterate num " + i);
  i++;
}
