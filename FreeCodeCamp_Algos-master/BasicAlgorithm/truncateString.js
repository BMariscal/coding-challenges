unction truncateString(str, num) {
  // Clear out that junk in your trunk
  if(num >= str.length){
    return str;
  }else if(num < 3){
    return str.slice(0,num) + "...";
  }else{
      var answer =(str.slice(0,num));
      var a=answer.split(' ');
      a.pop();
      var z = a.join(' ');
      return(z + "...");
  }
}

truncateString("A-tisket a-tasket A green and yellow basket", 11);
