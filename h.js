
  var counter = 1
function multiplicationFunc(num, maxCounter) {
  while (counter <= maxCounter) {
       var res =  num * counter;
      var template =  `${num} * ${counter} =  ${res}`;
      console.log(template)
      counter = counter + 1;
  }
  
}
// multiplicationFunc(2, 24)


function RandomCharacter(n){
  var maxNumber = 6;
  var str =  "Sharashell"
  if ( (n > 0) && (n <= maxNumber) ) {
    var res = str.split('')
    var d = Math.floor(Math.random() * parseInt(n)) + 1;
      console.log(res)
      console.log(res[d])

  } else {
    console.log('Number must be btw 1 & 6');
  }
}

RandomCharacter(5)


