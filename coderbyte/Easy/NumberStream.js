/*


Have the function NumberStream(str) take the str parameter being passed which will contain the numbers 2 through 9,
and determine if there is a consecutive stream of digits of at least N length where N is the actual digit value. If so, 
return the string true, otherwise return the string false. For example: if str is "6539923335" then your program should
return the string true because there is a consecutive stream of 3's of length 3. The input string will always contain at 
least one digit. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function NumberStream(str) { 
 let numdict = {"2": "2".repeat(2), "3": "3".repeat(3),"4": "4".repeat(4), "5": "5".repeat(5), "6": "6".repeat(6), "7": "7".repeat(7),"8": "8".repeat(8), "9": "9".repeat(9)};
 let keys = Object.keys(numdict);
 for (let i=0; i <keys.length; i++){
     if (str.match(numdict[keys[i]])){
         return true;
     }
 }
  return false;
}
NumberStream(readline());
