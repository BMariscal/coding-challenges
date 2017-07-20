/*

Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the 
result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas 
(ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346". 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function DivisionStringified(num1,num2) { 
    let newnum = Math.round(num1/num2).toString();
    let newstr ='';
    let count =0;
    if (newnum.length <= 3){
        return newnum;
    }else{
        for (let i=newnum.length-1; i >= 0; i--){
            count++;
            newstr+= newnum[i];
            if (count % 3 === 0){
                newstr+=',';
            }
             
        }
    }
   return newstr.split('').reverse().join('');      
}
DivisionStringified(readline());
