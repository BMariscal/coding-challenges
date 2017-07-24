/*

Have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them together, 
then return that final number. For example: if str is "88Hello 3World!" the output should be 91. You will have to 
differentiate between single digit numbers and multiple digit numbers like in the example above. So "55Hello" and "5Hello 5" 
should return two different answers. Each string will contain at least one letter or symbol. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function NumberAddition(str) { 
  let numArray = str.match(/[0-9]+/gi); 
  return numArray.reduce((acc, item)=> acc+=parseInt(item,10),0);
}
NumberAddition(readline());
