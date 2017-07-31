/*
Have the function DistinctCharacters(str) take the str parameter being passed and determine if it contains at least 10 distinct characters, if so, then your program should return the string true, otherwise it should return the string false. For example: if str is "abc123kkmmmm?" then your program should return the string false because this string contains only 9 distinct characters: a, b, c, 1, 2, 3, k, m, ? adds up to 9. 

Use the Parameter Testing feature in the box below to test your code with different arguments.


*/


function DistinctCharacters(str) { 
    let newstr = str.split('');
    let dict = {};
    newstr.forEach(item=> dict[item] = dict[item]? dict[item]+1: 1 );
    return Object.keys(dict).length >= 10;
}
DistinctCharacters(readline());
