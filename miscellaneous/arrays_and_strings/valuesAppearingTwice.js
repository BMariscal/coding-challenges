
// In the previous problem, we determined whether or not an array contains any
// of a list of values exactly twice. In this problem, we'll actually return
// those values appearing twice.  Create a new function that returns an array of
// only the values from the first array that appear twice in the second array.
//
// For this problem, you'll create a new array, and you'll use its `push`
// function to add elements to the end. You'll most likely want to use the
// `containsTwice` function you created in the previous exercise.
//
// The difficulty here will be in avoiding duplicates. You may want to use the
// `indexOf` method of the resulting array to confirm that you're not adding a
// value a second time.

//
var getValuesAppearingTwice = function (arr) {
  let dict={};
  for (let item in arr){
    dict[arr[item]]=dict[arr[item]]? dict[arr[item]]+1:1;
    
  }
  let list=[];
  for(let i in dict){
    if(dict[i] === 2){list.push(i)}
  }
  return list
};

//
console.log(getValuesAppearingTwice(["hello", 1, "world", 1]));
//     //=> [ 1 ]
//
console.log(getValuesAppearingTwice(["always", "will", "return", "empty"]));
//     //=> []
//
console.log(getValuesAppearingTwice(["hello", "hello", "world", "world", "goodbye"]));
//     //=> [ "hello", "world" ]
//
console.log(getValuesAppearingTwice(["hello", "world", "goodbye"]))
//     //=> []
