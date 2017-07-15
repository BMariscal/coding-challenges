/*Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function LetterChanges(str) { 
    let newString ='';
    
    for (let i =0; i< str.length; i++){
        // newString=((str.charCodeAt(i)-97)+1)
        if ( str[i].match(/[^a-z]/i)){
              newString += str.charAt(i);
              
        }else{
        let currentChar = str.charCodeAt(i)+1
        let newchar =String.fromCharCode(currentChar)
        
         if ( newchar === 'a' ||newchar === 'e' || newchar === 'i' || newchar === 'o'|| newchar === 'u'){
           newString += String.fromCharCode(currentChar).toUpperCase();
         }else{
           newString += String.fromCharCode(currentChar)
           }
        
        
    }}
    
   

  // code goes here  
  return newString 
         
}
   
   
// keep this function call here 
LetterChanges(readline());
