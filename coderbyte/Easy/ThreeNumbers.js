/*
Have the function ThreeNumbers(str) take the str parameter being passed and determine if exactly three unique, 
single-digit integers occur within each word in the string. The integers can appear anywhere in the word, but they 
cannot be all adjacent to each other. If every word contains exactly 3 unique integers somewhere within it, then 
return the string true, otherwise return the string false. For example: if str is "2hell6o3 wor6l7d2" then your 
program should return "true" but if the string is "hell268o w6or2l4d" then your program should return "false" because
all the integers are adjacent to each other in the first word. Use the Parameter
Testing feature in the box below to test your code with different arguments.


*/


function ThreeNumbers(str) { 
  let newarr = str.split(' ');
  if (str.match(/[\d]{3}/g)){return false}
  let dict = {};
    let numarr =  newarr.map(item=>item.split('').filter(i=> !isNaN(parseInt(i)))); 
    for (let i=0; i < numarr.length; i++){
        for (let j=0; j < numarr[i].length; j++){
            dict[numarr[i][j]] = dict[numarr[i][j]]? dict[numarr[i][j]]+1: 1; 
        } 
     if (Object.values(dict).filter(item=> item > 1).length >= 1){
        return false;
     }else{
         dict = {};
     }
        
    }
    return true;
}
ThreeNumbers(readline());
