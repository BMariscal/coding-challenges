/*

Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/

function VowelCount(str) { 

  // code goes here  
  return str.toLowerCase().split('').filter(item=> item.match(/(a|e|i|o|u)/gi)).length;
         
}
   
// keep this function call here 
VowelCount(readline());
