/*
Have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces. 

Use the Parameter Testing feature in the box below to test your code with different arguments.


*/

function LetterCount(str) { 

    let wordArr = str.split(' ');
    let wordDict = {};
    let newArr = wordArr.map((word,idx)=>{
    wordArr[idx].slice().split('').forEach(item=> wordDict[item] = wordDict[item]? wordDict[item]+1: 1);
    let dictEntries = [];
    let keys = Object.keys(wordDict);
    for (let i =0; i < keys.length; i++){
        dictEntries.push([keys[i], wordDict[keys[i]]]);
      }
    let sorted = dictEntries.sort((a,b)=> b[1]-a[1]);
    
    wordDict = {};
    return [word,sorted[0][1]];
        
    });
  return newArr.sort((a,b)=> b[1]-a[1])[0][1] < 2? -1: newArr.sort((a,b)=> b[1]-a[1])[0][0]; 
}
LetterCount(readline());
