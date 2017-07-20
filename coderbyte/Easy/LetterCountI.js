/*

Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest 
number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's 
(and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words 
will be separated by spaces. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/


function LetterCountI(str) { 
    let mywords = str.split(' ');
    let letterdict = {};
    let words = mywords.map(item =>{
    for(let i=0; i< item.length; i++){
        letterdict[item[i]] = letterdict[item[i]]?letterdict[item[i]]+1: 1 ;
    }
    let mykeys = Object.keys(letterdict);//
    let items =  mykeys.map(key=> [key, letterdict[key]]);
    let mostfrequentLetter = items.sort((a,b)=> b[1]-a[1])[0];
    letterdict = {};
    return mostfrequentLetter;
    });
    let maxcount = words.slice().sort((a,b)=> b[1]-a[1])[0][1];
    if (maxcount === 1){
      return -1;
    }else{
      for (let i=0; i < words.length; i++){
        if (words[i][1] === maxcount){
          return mywords[i];
          }
        }    
      }
}
LetterCountI(readline());
