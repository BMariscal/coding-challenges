/*
Have the function SwapII(str) take the str parameter and swap the case of each character. Then, if a letter is between two numbers (without separation), switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3. 

Use the Parameter Testing feature in the box below to test your code with different arguments.


*/

function SwapII(str) { 
    if (str.match(/[0-9]*/g)[0].length > 1 ){
        return str.split('').map(item => item.split('').map(i=> i === i.toUpperCase()? i.toLowerCase(): i.toUpperCase())).join('');
    }
    let splitter = str.match(/[^A-Za-z1-9]/g) ? withSplitter(str.match(/[^A-Za-z1-9]/g)[1],str):withNOSplitter(str) ;
    return splitter
}
function withNOSplitter(str){
    let arr = str.split('').map(i=> i === i.toUpperCase()? i.toLowerCase(): i.toUpperCase());
    let finalArr = [arr.join('')].map(item=> {if (item.match(/[0-9].+[0-9]/g) ){
      
        let nums = item.match(/[0-9]/g);
        let newStr = '';
        for (let i =0; i < item.length; i++){
            if (item[i] === nums[0].toString()){
                newStr+= nums[1].toString();
            }else if(item[i] === nums[1].toString()){
                newStr+= nums[0].toString();
            }else{
                newStr+= item[i];
            }
        }
        return newStr;
        
    }else{
        return item;
    }});
    return finalArr[0];
  
}

function withSplitter(splitter, str){
    let newarr = str.split(splitter);
    let arr = newarr.map(item => item.split('').map(i=> i === i.toUpperCase()? i.toLowerCase(): i.toUpperCase()));
    let finalArr = arr.map(item=> item.join('')).map(item=> {if (item.match(/[0-9].+[0-9]/g)){ 
        
        let nums = item.match(/[0-9]/g);
        console.log(nums)
        let newStr = '';
        for (let i =0; i < item.length; i++){
            if (item[i] === nums[0].toString()){
                newStr+= nums[1].toString();
            }else if(item[i] === nums[1].toString()){
                newStr+= nums[0].toString();
            }else{
                newStr+= item[i];
            }
        }
        return newStr;
        
    }else{
        return item;
    }});
    return finalArr.join(splitter);
  
  
}


SwapII(readline());
