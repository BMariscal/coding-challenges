function countBs(stringy){
    var myLetters ={};

    for (var i=0; i < stringy.length; i++){
        var current = stringy[i]
        myLetters[current] = (myLetters[current] || 0) + 1 //creating object, creating frequency count of letters by adding up occurences 
    }
    var arr =[];
    for (var key in myLetters){ //getting the values in the object, adding them to array, checking array for maximum value
        arr.push(myLetters[key])}
    return Math.max(...arr);
};


function countChar(stringy, letter){
    var count =0;
    for (var i=0; i < stringy.length; i++){
        if (stringy.charAt(i) === letter){
            count++;

        }

    }
    return count
};
console.log(countBs("BBC"));
// → 2
console.log(countChar("kakkerlak", "k"));
// → 4
