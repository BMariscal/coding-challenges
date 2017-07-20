/*
Have the function Palindrome(str) take the str parameter being passed and return the string true if the 
parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. 
For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/

function Palindrome(str) { 
    let reversed = '';
    let string = str.split(' ').join('');
    for (let i=string.length-1; i >= 0; i--){
        reversed+= string[i];
    }
    return reversed.split(' ').join('') === string ? true: false;
}

Palindrome(readline());
