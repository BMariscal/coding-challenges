function mutation(arr) {
  var final ="";
  var arr0 = arr[0].toLowerCase();
  var arr1= arr[1].toLowerCase().split('');
  for (var i=0; i < arr1.length; i++){
    if (arr0.indexOf(arr1[i]) >= 0){
      final += arr1[i];
      }
    }return (final.length == arr1.length);
}

mutation(["floor", "for"]);