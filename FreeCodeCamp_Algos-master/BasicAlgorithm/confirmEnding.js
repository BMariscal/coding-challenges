
function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  var targetLen = target.length;
   var answer = (str.slice(-targetLen) === target);
  
  // -- Falcor
  return answer;
}

confirmEnding("Bastian", "n");