/*


Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic 
characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee" then your 
program should return k. The string will always contain at least one character and there will always be at least one 
non-repeating character. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/

function NonrepeatingCharacter(str) { 
    let newstr = str.split('');
    let dict ={};
    newstr.forEach(item=> 
        dict[item] = dict[item] ? dict[item]+1: 1);
    return Object.keys(dict).sort((a,b)=> dict[a]-dict[b])[0];
}
NonrepeatingCharacter(readline());
