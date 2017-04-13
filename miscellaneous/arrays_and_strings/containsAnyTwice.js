// Write a function that accepts two arrays, and returns true if any of the
// values in the first array appear twice in the second array. You might want to
// reuse the function `containsNTimes` or `containsTwice` from above. It should
// throw an error if either of the inputs are not arrays.
//
// Although the tests will not be checking for this, try to make your loop exit
// as soon as it finds an element in the first array that appears twice in the second
// array.
//


var containsAnyTwice = function (target, arr) {
  if (typeof target !== typeof []){
    throw("containsAnyTwice expects two arguments, both of which should be an array.")}
  let dict={};
  for (let item in arr){
    dict[arr[item]]=dict[arr[item]]? dict[arr[item]]+1:1
    if (dict[arr[item]] === 2){return true};
    
  }
  return false
};

console.log(containsAnyTwice([1, 2], ["hello", 1, "world", 1]));
//     //=> true
//
console.log(containsAnyTwice([], ["always", "will", "return", "false"]));
//     //=> false
//
console.log(containsAnyTwice(["hello", "world"], ["hello", "hello", "world", "world"]));
//     //=> true
//
console.log(containsAnyTwice("hello", ["hello", "world"]));
//     //=> containsAnyTwice expects two arguments, both of which should be an array.
//
