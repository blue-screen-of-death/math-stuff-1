function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

function randomizeVowels(text) {
    var res = "";
    const lvowels = "aeiou";
    const uvowels = "AEIOU";
    for (i = 0; i < text.length; i++) {
        if (text[i] == "a" || text[i] == "e" || text[i] == "i" || text[i] == "o" || text[i] == "u") {
            var r = getRandomInt(0, 5);
            res += lvowels[r];
        } else if (text[i] == "A" || text[i] == "E" || text[i] == "I" || text[i] == "O" || text[i] == "U") {
            var r = getRandomInt(0, 5);
            res += uvowels[r];
        } else {
            res += text[i];
        }
    }
    console.log(res);
    copy(res);
}
