/*


Have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. 
The input can be any positive integer. For example: if num is 24, then your program should return 33 because that is 
the next largest number that is a palindrome. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/

function NextPalindrome(num) { 
    let newnum = 1;
    num = num+1;
    if (num.toString().length == 1 && num <= 8){
        return num;
    }else{
        while (newnum < (num + 10)){
            if (isPalindrome(num)){
              newnum = num + 10; 
              return num;
            }else{
                newnum = num++;
            }
        }
    }
}
function isPalindrome(num){
    return num.toString() === num.toString().split('').reverse().join('');
}
NextPalindrome(readline());
