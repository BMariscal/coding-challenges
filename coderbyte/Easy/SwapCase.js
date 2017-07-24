

/*
Have the function SwapCase(str) take the str parameter and swap the case of each character. 
For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/

function SwapCase(str) { 
    let final = '';
 for (let i =0; i < str.length; i++){
     if (str[i] === str[i].toLowerCase()){
         final+= str[i].toUpperCase();
     }else if (str[i] === str[i].toUpperCase()){
         final+= str[i].toLowerCase();
     }else{
         final+= str[i];
     }
 }
  return final;       
}
   
// keep this function call here 
SwapCase(readline());
