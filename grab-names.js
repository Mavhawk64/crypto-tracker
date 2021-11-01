const fs = require("fs");
var details = [];
var names = details.map(obj=>
obj.name);
console.log(names);
fs.writeFile("names.txt", names.join("\n"),function (err) {
  if (err) return console.log(err);
  // console.log('Hello World > helloworld.txt');
});

var symbol = details.map(obj=>
obj.symbol);
console.log(symbol);
fs.writeFile("symbols.txt", symbol.join("\n"),function (err) {
  if (err) return console.log(err);
  // console.log('Hello World > helloworld.txt');
});