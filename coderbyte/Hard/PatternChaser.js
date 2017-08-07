/*
Have the function PatternChaser(str) take str which will be a string and return the longest pattern within the string. 
A pattern for this challenge will be defined as: if at least 2 or more adjacent characters within the string repeat at 
least twice. So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern.
Your program should return yes/no pattern/null. So if str were "aabejiabkfabed" the output should be yes abe. If str were 
"123224" the output should return no null. The string may either contain all characters (a through z only), integers, or
both. But the parameter will always be a string type. The maximum length for the string being passed in will be 20 characters.
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". You must always return the longest pattern 
possible. 

Hard challenges are worth 15 points and you are not timed for them. Use the Parameter Testing feature in the box below to test your code with different arguments.

*/


function PatternChaser(str) { 
  let value = 2;
  let maxLength = 0;
  let currentPatternLength = 0;
  let currentPattern = '';
  for (let i = 0; i < str.length; i = i + value){
      for (let j = 0; j < str.length; j++){
         let matched = str.slice(j,j+value);
         let re = new RegExp(matched, 'g');
         let final = str.match(re);
         if (( matched.length > 1 && matched.length >= currentPatternLength) && final.length >= 2){
             maxLength = final.length;
             currentPattern = matched;
             currentPatternLength = matched.length;
             
             
         }
          
      }
      value++;
      
  }
  if (maxLength <= 1){
      return "no null";
  }
  return "yes " + currentPattern;
}
PatternChaser(readline());
