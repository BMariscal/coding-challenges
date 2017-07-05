
/*Return a new array that transforms the element's average altitude into their orbital periods.

The array will contain objects in the format {name: 'name', avgAlt: avgAlt}.

You can read about orbital periods on wikipedia.

The values should be rounded to the nearest whole number. The body being orbited is Earth.

The radius of the earth is 6367.4447 kilometers, and the GM value of earth is 398600.4418 km3s-2*/


function orbitalPeriod(arr) {
  var GM = 398600.4418;
  var earthRadius = 6367.4447;
  for (let i=0; i < arr.length; i++){
    let avgAlt =  arr[i].avgAlt;
    let orbitalPeriod = ((2* Math.PI)*(Math.sqrt(Math.pow((avgAlt+earthRadius),3)/GM))).toFixed();
    delete arr[i].avgAlt;
    arr[i].orbitalPeriod = parseInt(orbitalPeriod, 10);
  }
  return arr;
}

orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}]);
