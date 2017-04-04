//Convert the given number into a roman numeral.



function convertToRoman(num) {
  var romans1s = {1:'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7:'VII', 8: 'VIII', 9: 'IX'};
  var romans10s = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60:'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'};
  var romans100s = {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'};

 var romans1000s = {1000: 'M', 2000: 'MM', 3000: 'MMM', 4000:'MMMM'};
  
  var newNum = num.toString();
        var ones= parseInt(newNum[newNum.length-1]);
      var tens = parseInt(newNum[newNum.length-2] + 0);
      var hundreds = parseInt(newNum[newNum.length-3] + 0 + 0);
      var thousands = parseInt(newNum[newNum.length-4] + 0 +0 +0);
  
  if (newNum.length === 1){
    return romans1s[num];
  }
  
  else if (newNum.length === 2){
    if (num in romans10s){
      return romans10s[num];
    }else{

      return romans10s[tens] + romans1s[ones];
    }
  }
  
  else if (newNum.length === 3){

    
    if(num in romans100s){
      return romans100s[num];
    }else if(tens < 10){
      //501
      return romans100s[hundreds] +romans1s[ones]; 
    }else if (tens === 10 && ones === 0){
      return romans100s[hundreds] +romans10s[tens];
    }
    else{
     //may have issues with 501
    return romans100s[hundreds] + romans10s[tens] + romans1s[ones];
    }
  }
  
  else if (newNum.length === 4){

    
    if(num in romans1000s){
      return romans1000s[num];
    }
    else if (tens === 10 && ones === 0){
      return romans1000s[thousands] +romans10s[tens];    
    }else if (hundreds === 0 && tens !== 0){
      return romans1000s[thousands] + romans10s[tens] + romans1s[ones];
    
    } else if (hundreds ===0 && tens === 0){
      return romans1000s[thousands] + romans1s[ones];
    }else{
      return romans1000s[thousands] + romans100s[hundreds] + romans10s[tens] + romans1s[ones];
    }
  }
  
}

//testcases

convertToRoman(2) //should return "II".
convertToRoman(3) //should return "III".
convertToRoman(4) //should return "IV".
convertToRoman(5) //should return "V".
convertToRoman(9) //should return "IX".
convertToRoman(12) //should return "XII".
convertToRoman(16) //should return "XVI".
convertToRoman(29) //should return "XXIX".
convertToRoman(44) //should return "XLIV".
convertToRoman(45) //should return "XLV"
convertToRoman(68) //should return "LXVIII"
convertToRoman(83) //should return "LXXXIII"
convertToRoman(97) //should return "XCVII"
convertToRoman(99) //should return "XCIX"
convertToRoman(500) //should return "D"
convertToRoman(501) //should return "DI"
convertToRoman(649) //should return "DCXLIX"
convertToRoman(798) //should return "DCCXCVIII"
convertToRoman(891) //should return "DCCCXCI"
convertToRoman(1000) //should return "M"
convertToRoman(1004) //should return "MIV"
convertToRoman(1006) //should return "MVI"
convertToRoman(1023) //should return "MXXIII"
convertToRoman(2014) //should return "MMXIV"
convertToRoman(3999) //should return "MMMCMXCIX"

