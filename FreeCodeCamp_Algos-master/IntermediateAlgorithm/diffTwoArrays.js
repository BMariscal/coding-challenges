function diffArray(arr1, arr2) {
  var arr3 = arr1.concat(arr2);
  var newArr = [];
  var final= [];
  var countedNames = arr3.reduce(function(allNames, name) { 
  if (name in allNames) {
    allNames[name]++;
  }
  else {
    allNames[name] = 1;
  }
  return allNames;
}, {}); 
  // Same, same; but different.
newArr = countedNames;

var key = Object.keys(newArr).filter(function(key) {return newArr[key] === 1;});
var arrayOfNumbers = [];
for(var i=0; i<key.length;i++){
  if (key[i] === '1' || key[i] === '2' || key[i] === '3'|| key[i] === '4' || key[i] === '5' || key[i] === '6' || key[i] === '7'){
    arrayOfNumbers.push(Number(key[i]));

  }else{
    arrayOfNumbers.push(key[i]);
    }
  }
return arrayOfNumbers;
}
diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
