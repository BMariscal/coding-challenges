function destroyer(arr) {
   var vala = [arguments[1],arguments[2],arguments[3]];
   return arr.filter(function(element) {
   return vala.indexOf(element) === -1;
});
}

destroyer([3, 5, 1, 2, 2], 2, 3);
