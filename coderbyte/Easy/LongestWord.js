/*


Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. 

Use the Parameter Testing feature in the box below to test your code with different arguments.*/


function LongestWord(sen) { 
 let arr, newarr;
 let longest =[];
if(sen[1].match(/[0-9]/i) && sen[sen.length-1].match(/[0-9]/i)){
  newarr = sen;
   arr = newarr.split(" ") 
 
}else{
   newarr = sen.replace(/[^A-Za-z\s]/g, "")
   arr = newarr.split(" ")
}
 if( arr.length === 1 ){
        longest = arr[0]
        return longest        
    }
 for (let i=0; i <arr.length; i++){  
   for (let j=i+1; j <arr.length; j++){    
     if (arr[i].length === arr[j].length  && arr[i].length > longest.length){
       longest = arr[i]

      }
      else if (arr[i].length > arr[j].length && arr[i].length > longest.length){
       longest = arr[i]   
       }else if ( arr[i].length  < arr[j].length && arr[j].length > longest.length){
          longest = arr[j]
         }  
     }
   }
 return longest         
}
// keep this function call here 
LongestWord(readline());
