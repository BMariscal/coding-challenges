/*

Have the function Superincreasing(arr) take the array of numbers stored in arr and determine if the array forms a superincreasing sequence where each element in the array is greater than the sum of all previous elements. The array will only consist of positive integers. For example: if arr is [1, 3, 6, 13, 54] then your program should return the string "true" because it forms a superincreasing sequence. If a superincreasing sequence isn't formed, then your program should return the string "false" 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/





function Superincreasing(arr) { 
    let newsum = arr[0]+ arr[1];
    let final;
    return arr.slice(2).every(item=> {
        final = item > newsum;
        newsum+= item;
        return final;
    });
}
Superincreasing(readline());
