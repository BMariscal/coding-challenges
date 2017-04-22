/*We’ve seen that % (the remainder operator) 
can be used to test whether a number is 
even or odd by using % 2 to check whether
it’s divisible by two. Here’s another way to 
define whether a positive whole number is even or odd:

 *Zero is even.

 *One is odd.

 *For any other number N, its evenness is the same as N - 2.

Define a recursive function isEven corresponding
to this description. The function should accept 
a number parameter and return a Boolean.*/





function isEven(x){
    if (count == 2){
      count = 0;
        return x
    }else
    {count +=2;
        return isEven(x -2) % 2 == 0}
};
var count = 0;
console.log(isEven(50));
//true
console.log(isEven(75));
//false




//Book solutions:


function isEven(n) {
  if (n == 0)
    return true;
  else if (n == 1)
    return false;
  else if (n < 0)
    return isEven(-n);
  else
    return isEven(n - 2);
}
