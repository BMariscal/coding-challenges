var final = 0;
function reverseString(str) {
  final = str.split('').reverse().join('');
  return final;
}

reverseString("hello");