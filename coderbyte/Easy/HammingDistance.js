/*Have the function HammingDistance(strArr) take the array of strings stored in strArr, which will only contain two strings
of equal length and return the Hamming distance between them. The Hamming distance is the number of positions where the 
corresponding characters are different. For example: if strArr is ["coder", "codec"] then your program should return 1. 
The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/



function HammingDistance(strArr) { 
    let diffcounter  =0;
    strArr[0].split('').forEach((item,index)=> {if(item !== strArr[1][index]){
                                        diffcounter++;
    }} );
    return diffcounter;
}
HammingDistance(readline());
