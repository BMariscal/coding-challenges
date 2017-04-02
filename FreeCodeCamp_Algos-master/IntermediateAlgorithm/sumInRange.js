function sumAll(arr) {
  var minimum = Math.min(arr[0], arr[1]);
  var maximum = Math.max(arr[0],arr[1]);
  //var arr1 = [minimum, maximum];
  var array = [];
  for (var i = minimum; i <= maximum; i++) {
    array.push(i);
}
var sum = array.reduce(
  function(total, num){ 
    return total + num;
    }, 0);  
return sum;
}

sumAll([1, 4]);  