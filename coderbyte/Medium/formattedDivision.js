/*
Have the function FormattedDivision(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas and 4 significant digits after the decimal place. For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789". The output must contain a number in the one's place even if it is a zero. 

Use the Parameter Testing feature in the box below to test your code with different arguments.




*/


function FormattedDivision(num1,num2) { 
    const result = (num1/num2).toFixed(4);
    const numStr = result.toString().match(/(.*?)\./)[1].split('');
    const numAfter = result.toString().match(/\..+/);
    let newNumArr = [];
    for (let i = numStr.length-1; i >= 0 ; i--){
        if (newNumArr.length === 3 || newNumArr.length === 7 ){
           
           newNumArr.push(',');
           newNumArr.push(numStr[i]);
        }else{
            newNumArr.push(numStr[i]);
        }
        
    }
    
  return  newNumArr.reverse().join('').concat(numAfter);  
         
}
FormattedDivision(readline());
