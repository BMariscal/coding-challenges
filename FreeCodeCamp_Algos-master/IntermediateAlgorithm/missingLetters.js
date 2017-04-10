/*Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined.*/



function fearNotLetter(str) {
  for (var i in str){
    let currentLetter = str.charCodeAt(parseInt(i));
    let nextLetter = str.charCodeAt(parseInt(i)+1);  
    if (currentLetter + 1 === nextLetter){

    }else{
      if(!nextLetter) {
        return undefined;
        }return String.fromCharCode(parseInt(nextLetter-1));}
    }
  }



fearNotLetter("bcd");

fearNotLetter("abce") //should return "d".
fearNotLetter("abcdefghjklmno") //should return "i".
fearNotLetter("bcd") //should return undefined.
fearNotLetter("yz") //should return undefined.
