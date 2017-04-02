function chunkArrayInGroups(arr, size) {
  var increments = 0;
  var list= [];
  var removeExtra = arr.slice(arr.length-(arr.length % size));
  arr = arr.slice(0,arr.length-(arr.length % size));
  for (var i=size ; i < arr.length+1; i+=size){
    var sliced = arr.slice(increments,i);
    list.push(sliced);
    increments +=size;
  }
  if (removeExtra.length > 0){
    list.push(removeExtra);
  }
  // Break it up.
  return( list);
}
chunkArrayInGroups(["a", "b", "c", "d"], 2);
