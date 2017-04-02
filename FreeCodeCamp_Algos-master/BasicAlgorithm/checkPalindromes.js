
function palindrome(str) {
  var lowerCase = str.toLowerCase();
  var a = lowerCase.replace(/[^a-z0-9]/g,"");
  var splitting = a.split('');
  var reversed = splitting.reverse();
  var joined = reversed.join('');
  if ( a === joined){
    return true;
  } else{
    return false;
  
  }
}



palindrome("eye");