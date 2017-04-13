// Generalize the previous solution into a function called `containsNTimes` so
// that it can check for a value an arbitrary number of times.

var containsNTimes = function (frequency,target, arr) {
  let dictionary ={};
  for (let item in arr){
    dictionary[arr[item]] = dictionary[arr[item]]? dictionary[arr[item]]+1:1; //ternary operator to count frequency of items
    
    
  }
  return dictionary[target] === frequency //if value of key is 2, return true. Otherwise return false

    
};






containsNTimes(3, "hello", [ "hello", "hello", "hello" ]);
//     //=> true
//
containsNTimes(5, true, [ true, true, true, true, false ]);
//     //=> false
//
containsNTimes(0, 5, [ 1, 2, 3, 4, 5 ]);
//     //=> false
