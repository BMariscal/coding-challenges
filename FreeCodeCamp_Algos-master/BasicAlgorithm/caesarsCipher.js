function rot13(str) {
  var finalArray =[];

  for( var i=0; i < str.length; i++){
    var charAtt = str.charCodeAt(i);
    if (charAtt < 65 || charAtt > 90){
        finalArray.push(charAtt);
    }else{
       if(charAtt >= 78){
            finalArray.push(charAtt - 13 );
       }else{
            finalArray.push(charAtt + 13);
          }
        }
  }
 
  
  return String.fromCharCode.apply(null, finalArray);
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");