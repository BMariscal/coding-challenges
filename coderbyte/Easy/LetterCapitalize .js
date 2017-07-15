/*
Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word.
Words will be separated by only one space. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/

function LetterCapitalize(str) { 
    let newstr = str.split('')
    let newarr =[newstr[0].toUpperCase()]
   

    
    for (let i =1; i < newstr.length; i++){
            if (newstr[i-1] === ' '){
  
                newarr.push(newstr[i].toUpperCase())
            }else{
                newarr.push(newstr[i])
            }
    }
    
    
  // code goes here
  let finalarr =newarr.join('')
  return finalarr; 
         
}
// keep this function call here 
LetterCapitalize(readline());
