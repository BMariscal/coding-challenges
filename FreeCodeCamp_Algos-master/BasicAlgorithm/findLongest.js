function findLongestWord(str) {
  var splitting = str.split(' ');
  var currentLongest = splitting[0];
  for (var i =1; i < splitting.length; i++){
    if (splitting[i].length > currentLongest.length){
      currentLongest = splitting[i];
      }
  
  }
  return (currentLongest.length);
}
findLongestWord("May the force be with you");