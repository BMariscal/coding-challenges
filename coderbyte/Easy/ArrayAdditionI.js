/*

Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any
combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the 
string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23.
The array will not be empty, will not contain all the same elements, and may contain negative numbers. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/

function ArrayAdditionI(arr) { 
  let total = 0;
  let sortedarr = arr.slice();
  let largestNum = sortedarr.sort((a,b)=> a-b).pop();
  for(let i=0; i< sortedarr.length; i++){
        total += sortedarr[i];
        if (total === largestNum){
            return true;
        }else if( total > largestNum){
          return true}
    }
    return false;  
}
ArrayAdditionI(readline());
