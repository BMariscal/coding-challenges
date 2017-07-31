/*

Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number 
within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest 
double digit number. The input will always contain at least two positive digits. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function LargestPair(num) { 
    let numarr = num.toString().split('');
    let finalarr =  numarr.map((item,i)=> item +numarr[i+1]);
    finalarr.pop();
    return finalarr.sort((a,b)=> parseInt(b)-parseInt(a))[0];
}
LargestPair(readline());
