
// Write a function called `allStrings` that accepts an array as an argument and
// returns `true` if all of the values in the array are strings. It should
// return false if they are not all strings, and throw an error if the input is
// not an array.

var allStrings = function (arr) {
  if (typeof arr !== typeof []){
    throw("input should be an array!")} . //throws error if arr is not an array
  var tally = arr.filter(function(value){ . //tally is a new array that has the false values(i.e, those values that are not strings) filtered out
    return (typeof value === typeof "")
    
  });
  return (tally.length === arr.length) //so if the length of the new tally array is not the same as the length of the original array, then that means there were non-string items in the original array and the function should return false
};
allStrings([ "these", "are", "all", "strings" ]); //=> true
//
allStrings([ "these", "are", "not", 5 ]); //=> false
//
allStrings([ ]); //=> true
//
allStrings("hello"); //=> input should be an array!





// Although the tests will not be checking for this, try to make your loop exit
// as soon as it finds a non-string entry in the array.
//
var allStrings = function (arr) {
  if (typeof arr !== typeof []){
    throw("input should be an array!")}//throws error if arr is not an array
  let inLoop= true;
  for (var item in arr){
    if(typeof arr[parseInt(item)] !== typeof ''){return false}
    
  }
  return inLoop
  
};
allStrings([ "these", "are", "all", "strings" ]); //=> true
//
allStrings([ "these", "are", "not", 5,'ok' ]); //=> false
//
allStrings([ ]); //=> true
//
allStrings("hello"); //=> input should be an array!
