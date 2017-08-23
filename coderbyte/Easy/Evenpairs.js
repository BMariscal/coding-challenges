/*
Have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the string true, otherwise return false. For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/

function EvenPairs(str) { 
    const num = str.match(/[0-9]+/g);
    if (num){
        let final = num.filter(item => item % 2 === 0 && (item.slice(0,1) % 2 === 0 && item.slice(1) % 2 === 0 ||item.slice(0,2) % 2 === 0 && item.slice(2) % 2 === 0 ));
        if (final.length === 0 || final[0].length === 1){
            return false;
        }else{
            return true;
        }
    
    }else{
        return false;
    }   
}

EvenPairs(readline());
