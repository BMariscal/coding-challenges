
/*The DNA strand is missing the pairing element. Take each character, get its pair, and return the results as a 2d array.

Base pairs are a pair of AT and CG. Match the missing element to the provided character.

Return the provided character as the first element in each array.

For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]

The character and its pair are paired up in an array, and all the arrays are grouped into one encapsulating array.*/



//with switch
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

//with object and map() 
function pairElement(str) {
  const bases = str.split("");
  const map = {T:'A', A:'T', G:'C', C:'G'};
  const basepairs = bases.map(bases => {
    return [bases, map[bases]];
  });
  return basepairs;
}

pairElement("GCG");






pairElement("GCG");


 pairElement("ATCGA")// should return [["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]].
pairElement("TTGAG") //should return [["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]].
pairElement("CTCTA") //should return [["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]]. 
