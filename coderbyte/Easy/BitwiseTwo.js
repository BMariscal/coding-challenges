/*
Have the function BitwiseTwo(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers, and return a final binary string that performed the bitwise AND operation on both strings. A bitwise AND operation places a 1 in the new string where there is a 1 in both locations in the binary strings, otherwise it places a 0 in that spot. For example: if strArr is ["10111", "01101"] then your program should return the string "00101" 

Use the Parameter Testing feature in the box below to test your code with different arguments.

*/


function BitwiseTwo(strArr) { 
    return strArr[0].split('').map((item,idx)=> { if(item === '1' && strArr[1][idx] === '1'){
        return 1;
      }else{
        return 0;
      } }).join('');
}
BitwiseTwo(readline());
