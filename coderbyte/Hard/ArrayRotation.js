/*
Have the function ArrayRotation(arr) take the arr parameter being passed which will be an array of non-negative integers
and circularly rotate the array starting from the Nth element where N is equal to the first integer in the array. 
For example: if arr is [2, 3, 4, 1, 6, 10] then your program should rotate the array starting from the 2nd position 
because the first element in the array is 2. The final array will therefore be [4, 1, 6, 10, 2, 3], and your program 
should return the new array as a string, so for this example your program would return 4161023. The first element in the
array will always be an integer greater than or equal to 0 and less than the size of the array. 

Hard challenges are worth 15 points and you are not timed for them. Use the Parameter Testing feature in the box 
below to test your code with different arguments.
*/


function ArrayRotation(arr) { 
    let targetIndex = arr[0];
    let rotate = arr.slice(targetIndex);
    let notRotate = arr.slice(0,arr[0]);
    return rotate.concat(notRotate).toString().replace(/,/g,'');
         
}
ArrayRotation(readline());
