/*
Have the function CamelCase(str) take the str parameter being passed and return it in proper camel case format where the first letter of each word is capitalized (excluding the first letter). The string will only contain letters and some combination of delimiter punctuation characters separating each word. 

For example: if str is "BOB loves-coding" then your program should return the string bobLovesCoding. 

Use the Parameter Testing feature in the box below to test your code with different arguments.

*/

function CamelCase(str) { 
    let newstr = str.replace(/[^A-Z]/gi, ' ').split(' ');
    let newarr = newstr.slice(1).map(item=> 
            item[0].toUpperCase() + item.slice(1).toLowerCase()
);
    return newstr[0].toLowerCase() + newarr.join('');
}
CamelCase(readline());
