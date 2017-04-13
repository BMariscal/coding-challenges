// Using a standard `for` loop, along with the `push` function, write a function
// called `range` that accepts two numbers, `begin` and `end`, and returns an array
// that contains all of the integers starting at `begin` and ending at `end`
// (including `begin` and `end`). For example:
//
//     range(5,10);
//     //=> [5, 6, 7, 8, 9, 10]
//
//     range(0,3);
//     //=> [0, 1, 2, 3]
//
//     range(10,3);
//     //=> [10, 9, 8, 7, 6, 5, 4, 3]
//
// It should throw an error when either of the arguments are not numbers.
//
//     range("hello", "world");
//     //=> arguments to range must be numbers





// Solved with for loop and push
var range = (start,end)=>{
  //throw error if beginning and end values are not numbers
  if((typeof begin  && typeof end) !== typeof 1){
    throw("arguments to range must be numbers")}
    
    
  let finalArr =[];
  if (start < end){
  for (let i=start; i <= end; i++){
    finalArr.push(i);}
  }else{
  for (let i=start; i >= end; i--){
    finalArr.push(i); }  
  }return finalArr  
}

//Solved recursively

let list=[],range = function(begin, end){
  //throw error if beginning and end values are not numbers
  if((typeof begin  && typeof end) !== typeof 1){
    throw("arguments to range must be numbers")}
    
    
  list.push(begin) //create list here
  if (begin === end){//base case
    let newlist = Array.from(list);
    list=[]
    return newlist}
  else{ 
    if (begin < end){ //if new list should count up
    return range(begin+1,end)} //begin increases
    else if(begin > end){ //if new list should count down
      return range(begin-1,end)  //begin decreases 
    }
    
  }
 
}

console.log(range(5,10));
//     //=> [5, 6, 7, 8, 9, 10]
//
console.log(range(0,3));
//     //=> [0, 1, 2, 3]
//
console.log(range(10,3));
//     //=> [10, 9, 8, 7, 6, 5, 4, 3]
