function titleCase(str) {
  var reformatting = str.toLowerCase().split(' ');
  var whatever =[];

  for (var i=0; i < reformatting.length; i++){
     whatever.push(reformatting[i][0].toUpperCase(), reformatting[i].slice(1));

     
  }
  var final = whatever.join('');
  var s = final.replace(/([A-Z])/g, ' $1').trim();
  return(s);
}


titleCase("I'm a little tea pot");