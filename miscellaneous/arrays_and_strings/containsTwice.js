//practice working with arrays
//source: o'reilly video course, link in README.md


// Write a function called `containsTwice` that accepts a number and an array,
// and returns `true` if that number appears in the array twice, and `false`
// otherwise.


let containsTwice = function (target, arr) {
  let dictionary ={};
  for (let item in arr){
    dictionary[arr[item]] = dictionary[arr[item]]? dictionary[arr[item]]+1:1; //ternary operator to count frequency of items
    
    
  }
  return dictionary[target] === 2 //if value of key is 2, return true. Otherwise return false

    
};

console.log(containsTwice(5, [1, 2, 3, 4, 5]));
//     //=> false
//
console.log(containsTwice("hello", [ "hello", "world", "hello" ]));
//     //=> true
//
console.log(containsTwice(true, [ true, false, false, true ]));
//     //=> true
//
console.log(containsTwice(10, [10, 10, 10, 10, 10]));
//     //=> false
