/*

Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a
portion of str1 characters can be rearranged to match str2, otherwise return the string false. For example: if str1 is 
"rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will not be entered with the parameters. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function StringScramble(str1,str2) { 
    let dict1 ={};
    let dict2 ={};
    str1.split('').forEach((item,index)=> dict1[item] = dict1[item] ? dict1[item]+1:1);
    str2.split('').forEach(item=> dict2[item] = dict2[item] ? dict2[item]+1:1);
    let orderDict1 = Object.keys(dict1).sort();
    let orderDict2 = Object.keys(dict2).sort();
    let or =  orderDict2.filter(item=> orderDict1.includes(item));
    return  or.every(item=> orderDict2[item] === orderDict1[item]) && orderDict2.join('') === or.join('');
    
}
StringScramble(readline());
