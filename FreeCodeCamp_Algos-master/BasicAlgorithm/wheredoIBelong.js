
function getIndexToIns(arr, num) {
  // Find my place in this sorted array.
  var num1 = arr.concat(num);
  num1.sort(function (a,b){
    return a - b;
  });
  return num1.indexOf(num);
}

getIndexToIns([5, 3, 20, 3], 5);