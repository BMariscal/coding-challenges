/*
Spinal Tap Case
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.*/



function spinalCase(str) {

  var splitString= str.split(/\s|_|(?=[A-Z])/);
  return splitString.join('-').toLowerCase();
  //return str.replace(/([a-z])([A-Z])|[_|\s]+/g, '$1-$2').toLowerCase(); //one-liner
}

spinalCase('This Is Spinal Tap');


spinalCase("This Is Spinal Tap") //should return "this-is-spinal-tap".
spinalCase("thisIsSpinalTap") //should return "this-is-spinal-tap".
spinalCase("The_Andy_Griffith_Show") //should return "the-andy-griffith-show".
spinalCase("Teletubbies say Eh-oh") //should return "teletubbies-say-eh-oh".
spinalCase("AllThe-small Things") //should return "all-the-small-things".
