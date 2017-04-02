function bouncer(arr) {
  // Don't show a false ID to this bouncer.
  var filtArray= arr.filter(Boolean);
  return filtArray;
}
//Since the Boolean constructor is also a function, it returns either true for ‘truthy’ argument or false for ‘falsy’ argument. If the value is omitted or is 0, -0, null, false, NaN, undefined, or the empty string (""), the object has the value of false. All other values, including any object or the string "false", create an object with an initial value of true.


bouncer([7, "ate", "", false, 9]);