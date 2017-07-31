/*
Have the function PalindromeCreator(str) take the str parameter being passed and determine if it is possible to create a palindromic string of at least 3 characters by removing 1 or 2 characters. For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible. If the input string is already a palindrome, your program should return the string palindrome. 

The input will only contain lowercase alphabetic characters. Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). The 2 characters you remove do not have to be adjacent in the string. 

Use the Parameter Testing feature in the box below to test your code with different arguments.

*/


function PalindromeCreator(str) {
    let newstr = str.split('');
    let newarr = newstr.slice();
    if (isPalindrome(newstr)){
        return "palindrome";
    }else if (isPalindrome(newstr.slice(1,newstr.length-1))){
        return newstr[0]+ newstr[newstr.length-1];
    }
    for (let i=0; i < newstr.length; i++){
        let newcopy = newstr.slice();
        newcopy.splice(i,1);
        let spliced = newcopy;
        if (isPalindrome(spliced)){
            return newstr[i]; } }
    for (let i=0; i < newstr.length; i++){
        let copy = newstr.slice();
        copy.splice(i,1);
        copy.splice(i,1);
        if(isPalindrome(copy) && copy.length > 2){
            return newstr[i]+ newstr[i+1];}}
  return "not possible";}
  
function isPalindrome(arr){
    return arr.slice().join('') === arr.slice().reverse().join('');
}
PalindromeCreator(readline());
