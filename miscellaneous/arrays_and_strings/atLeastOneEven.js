// Write a function called `atLeastOneEven` that returns `true` if at least one of
// the numbers in input array is even, false otherwise. It should throw an error if
// the argument is not an array.

let atLeastOneEven = function (arr) {
  if (typeof arr !== typeof []){
    throw("input should be an array!")}
    
  for (let item in arr){
     if(arr[item] % 2 === 0){return true}   
  }
  return false
};
//
atLeastOneEven([ 3, 5, 6, 7, 9 ]);
//     //=> true
//
atLeastOneEven([]);
//     //=> false
//
atLeastOneEven([ 101, 203, 401 ]);
//     //=> false
//
atLeastOneEven("hello");
//     //=> input should be an array!
//
