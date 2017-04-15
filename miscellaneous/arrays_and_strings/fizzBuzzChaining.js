//FizzBuzz with chaining functions that return arrays

//Range function creates array, map changes each element in that array to fizz/buzz/fizzBuzz/number depending on conditons met.
//Each element in this array is then printed out with forEach()

//My range function. Takes in start, end, step. Sets start to 0 and step  to 1 as default 
let range = function(start,end,step){
  var args = Array.prototype.slice.call(arguments);
  var args = [].slice.call(arguments);
  if (args.length === 1){
  end = args[0],start =0;
  step = 1}
  if (args.length === 2){
     step = 1;    
  }

  let newArr =[];
  return start < end ? ascending(): descending();
  function ascending(){
    for (let i=start; i <= end; i=i+step){
      newArr.push(i);} return newArr;}
  function descending(){
    for (let i=start; i >= end; i=i-step){
      newArr.push(i);} return newArr;}
  
}
//Chaining functions
range(1,20).map(function(number){
    if (number % 3 == 0 && number % 5 === 0){
      return "FIZZBUZZ";
      
    }else if (number % 3 === 0){
      return "FIZZ";
        
    }else if (number % 5 === 0){
      return "BUZZ"
    }else{
      return number
    }
    
}).forEach(function(number){
  console.log(number);  
})


//Output:


// 1
// 2
// FIZZ
// 4
// BUZZ
// FIZZ
// 7
// 8
// FIZZ
// BUZZ
// 11
// FIZZ
// 13
// 14
// FIZZBUZZ
// 16
// 17
// FIZZ
// 19
// BUZZ
