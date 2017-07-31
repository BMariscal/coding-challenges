/*


Have the function PalindromeSwapper(str) take the str parameter being passed and determine if a palindrome can 
be created by swapping two adjacent characters in the string. If it is possible to create a palindrome, then your
program should return the palindrome, if not then return the string -1. The input string will only contain alphabetic
characters. For example: if str is "rcaecar" then you can create a palindrome by swapping the second and third characters, 
so your program should return the string racecar which is the final palindromic string. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function PalindromeSwapper(str) { 
    for (let i=0; i < str.length-1; i++){
        let j = i+1;
        let swapped = swapper(str,i,j);
        if (isPalindrome(swapped)){
            return swapped.join('');
        } else{
            continue;
        }        
    }
   return -1;      
}
function swapper(str,i,j){
    let newarr = str.split('');
    [newarr[i], newarr[j]] = [newarr[j], newarr[i]];
    return newarr;
}
function isPalindrome(arr){
   return  arr.join('') === arr.slice().reverse().join('');
}
PalindromeSwapper(readline());
