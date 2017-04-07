
/*The DNA strand is missing the pairing element. Take each character, get its pair, and return the results as a 2d array.

Base pairs are a pair of AT and CG. Match the missing element to the provided character.

Return the provided character as the first element in each array.

For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]

The character and its pair are paired up in an array, and all the arrays are grouped into one encapsulating array.*/




function pairElement(str) {
  var outerArr=[];
  for (var element in str){
    var subArr=[];
    var firstbase=str[element];
      subArr.push(firstbase);
    
    switch(firstbase){
      case "G":
        subArr.push("C");
        break;
      case "C":
        subArr.push("G");
        break;
      case "A":
        subArr.push("T");
        break;
      case "T":
        subArr.push("A");
        break;
                
    }
    
    outerArr.push(subArr);
    
  }
  
  
  return outerArr;
}


pairElement("GCG");
