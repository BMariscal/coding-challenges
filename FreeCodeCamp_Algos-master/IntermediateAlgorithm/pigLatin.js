
/*Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word, 
moves it to the end of the word and suffixes an "ay".

If a word begins with a vowel you just add "way" to the end.

Input strings are guaranteed to be English words in all lowercase.

Remember to use Read-Search-Ask if you get stuck. Try to pair program. Write your own code.*/

//uses regex, with help from http://regexr.com/

function translatePigLatin(str) {
  
  var word = str;

var replaceConst = word.replace(/(^[b-df-hj-np-tv-z]{1,2})/g, '');
var startCons = word.match(/(^[b-df-hj-np-tv-z]{1,2})/g);
if (!startCons){
  return replaceConst + 'way' ;}
else{
  return replaceConst + startCons + 'ay';}
  
}

translatePigLatin("algorithm");



translatePigLatin("california")// should return "aliforniacay".
translatePigLatin("paragraphs")// should return "aragraphspay".
translatePigLatin("glove")//should return "oveglay".
translatePigLatin("algorithm")// should return "algorithmway".
translatePigLatin("eight")// should return "eightway".
