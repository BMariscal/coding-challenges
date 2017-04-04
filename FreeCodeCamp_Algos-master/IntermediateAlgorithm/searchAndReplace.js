//Perform a search and replace on the sentence using the arguments provided and return the new sentence.

//First argument is the sentence to perform the search and replace on.

//Second argument is the word that you will be replacing (before).

//Third argument is what you will be replacing the second argument with (after).



function myReplace(str, before, after) {
  if (before[0].toUpperCase() === before[0]){
    after = after[0].toUpperCase() + after.slice(1);
  }
  
  var newStr= str.replace(before, after);
  return newStr;
}
myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");


//test cases:


myReplace("Let us go to the store", "store", "mall") //should return "Let us go to the mall".
myReplace("He is Sleeping on the couch", "Sleeping", "sitting") //should return "He is Sitting on the couch".
myReplace("This has a spellngi error", "spellngi", "spelling") //should return "This has a spelling error".
myReplace("His name is Tom", "Tom", "john") //should return "His name is John".
myReplace("Let us get back to more Coding", "Coding", "algorithms") //should return "Let us get back to more Algorithms".
