/*Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function AlphabetSoup(str) { 
    let newstr = str.split(' ')
    let newarr= []
    for (let i=0; i <newstr.length; i++){
        newarr.push(newstr[i].split('').sort().join(''))
    } 
  return newarr.join(' '); 
} 
// keep this function call here 
AlphabetSoup(readline());
