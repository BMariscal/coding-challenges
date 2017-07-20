/*

Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second 
greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should 
be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers! 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function SecondGreatLow(arr) { 
    let secondsmallest;
    let secondlarget;
    let sorted = arr.sort((a,b)=> a-b);
    let lastIdx = sorted.lastIndexOf(sorted[0]);
    if (sorted[0] === sorted[1] && sorted.length >2){
        sorted = sorted.slice(lastIdx);
        secondsmallest = sorted[1];
        secondlargest = sorted[sorted.length-2];
    }else{
        secondsmallest = sorted[1];
        secondlargest = sorted[sorted.length-2];
    }
  return secondsmallest +' '+ secondlargest; 
}

SecondGreatLow(readline());
