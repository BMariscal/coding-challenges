/*

Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the 
output should be 4547-9-3. Don't count zero as an odd number. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
*/


function DashInsert(str) { 
  let newitem = '';
  let newstr = str.split('');
  for (let i=0 ;i < newstr.length; i++){
      if ((newstr[i] % 2 !== 0) && (newstr[i+1]%2 !== 0) && newstr.indexOf(newstr[i]) !== newstr.length-1){
          newitem += newstr[i] +'-';
      }else{
          newitem+= newstr[i];
      }
  }
  return newitem[newitem.length-1] == '-'? newitem.slice(0,newitem.length-1) : newitem;
}
DashInsert(readline());
