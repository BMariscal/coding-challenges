/*
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function TimeConvert(num) { 
    let answer = ''
    let final =''
    let lastnum = ''
    let disnum=  ''
    if ( num < 60){
        answer = num
        final = '0:'+answer
    }else{
     let newnum = (num/60).toString()
     if (newnum.length > 1){
         lastnum = (num.toString())
         disnum = num % 60
         final = newnum[0] +':'+disnum
     }else{
         final = newnum + ':'+ '0'}
    }
  // code goes here  
  return final; 
}
// keep this function call here 
TimeConvert(readline());
