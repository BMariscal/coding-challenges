/*

Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if 
they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). The array 
will not be empty, will only contain positive integers, and will not contain more than one mode. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function MeanMode(arr) { 
    let mean = arr.reduce((acc,item)=> acc+item)/arr.length;
    let dict = {};
    for (let i=0; i <arr.length; i++){
        dict[arr[i]] = dict[arr[i]]? dict[arr[i]]+1:1;
    }
    let mode = Object.keys(dict).sort((a,b)=> dict[b]-dict[a])[0];  
    if (parseInt(mode,10) === mean){
        return 1;
    }else{
        return 0;
    }
}
MeanMode(readline());
