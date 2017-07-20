/*

Have the function ExOh(str) take the str parameter being passed and return the string true if there is 
an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in 
the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false 
because there are 6 x's and 5 o's. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/

function ExOh(str) { 
    let exes = 0;
    let os = 0;
    str.split('').forEach(item=> { if (item === "x"){exes++}else{os++}
    });
    return (exes === os ? true: false);
         
}
   
ExOh(readline());
