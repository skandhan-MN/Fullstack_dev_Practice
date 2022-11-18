// for (i = 1; i <= 10; i++) {
//   rem = i % 2;
//   if (rem == 0) {
//     console.log("the square of even numbers in ranje 1-10 are", i);
//   }
// }

//Array litrals//
// let base = 120;
// let table = [base, base + 1, base + 2, base + 3];
// console.log(table);

// let sparseArray = [1, , , , 5];
// console.log(sparseArray);

// const companies = [
//   { name: "Company One", category: "Finance", start: 1981, end: 2004 },
//   { name: "Company Two", category: "Retail", start: 1992, end: 2008 },
//   { name: "Company Three", category: "Auto", start: 1999, end: 2007 },
//   { name: "Company Four", category: "Retail", start: 1989, end: 2010 },
//   { name: "Company Five", category: "Technology", start: 2009, end: 2014 },
//   { name: "Company Six", category: "Finance", start: 1987, end: 2010 },
//   { name: "Company Seven", category: "Auto", start: 1986, end: 1996 },
//   { name: "Company Eight", category: "Technology", start: 2011, end: 2016 },
//   { name: "Company Nine", category: "Retail", start: 1981, end: 1989 },
// ];

// const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

// // for (i = 0; i < companies.length; i++) {
// //   console.log(companies[i]);
// // }

// companies.forEach(function (Company) {
//   console.log(Company);
// });

// =====================================================
// Arrays
// =====================================================

// let age = [20, 45, 3, 23, 57, 46, 73];
// console.log(age);

// let num2 = age.shift();
// let num = age[1];

// console.log(num);
// console.log(num2);
// console.log(age);
// for (let i = 0; i < age.length; i++) {
//   console.log(age[i]);
// }

// const x = 1;
// console.log(x);

// let y = 2;
// y = 32;
// y = true;
// console.log(y);

// const a = Array.of(1, 2, 3, 4);
// console.log(a);

// const matrix = [
//   [1, 2, 3],
//   [3, 4, 5],
//   [4, 5, 6],
// ];
// matrix[0][0];

// console.log(matrix[2][2]);

// const a = Array(12).fill(121);
// console.log(a);

// let b = [1, 2, 3, 4, 5];
// b.push(1234);
// console.log(b);

//Adding element to the begining of the array( unshift( ))

// let a = [1, 2, 3, 4, 5];
// a.unshift(1234);
// console.log(a);
// console.log(a[5]);

//Removing an element from the end of an array(pop())

// let a = [8, 7, 6, 5, 4];
// a.pop();
// console.log(a);

//Removing an element form the start of an array ( shift())

// let a = [23, 24, 25, 26];
// a.shift();
// console.log(a);

//Joining multiple arrays

// let a = [1, 2, 3, 4, 5, 6];
// let b = [7, 8, 9, 10, 11, 12];
// let c = a.concat(b);
// console.log(c);

// using spread operator

// let a = [1, 2, 3, 4, 5, 6];
// let b = [7, 8, 9, 10, 11, 12];
// const c = [...a, ...b];
// console.log(c);

//to find the specific element in an array
// const a = [1, 2, 3, 4, 5, 6];

// const found = a.find((mix) => mix < 3);
// console.log(found);
