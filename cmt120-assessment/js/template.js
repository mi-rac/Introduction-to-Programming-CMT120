// Exercise 1
function reduceFraction(num, den) {
    const gcd = (a, b) => {return b ? gcd(b, a%b): a}
    const hcf = gcd(num, den);
    return [num/hcf, den/hcf];
}

// Exercise 2
function isMagicDate(day, month, year) {
    return (day * month) == (year % 100);
}

// Exercise 3
function sublist(l) {
    const res = [[]];
    for (let len_sublist = 1; len_sublist <= l.length; len_sublist++){
      for (let i = 0; i <= l.length - len_sublist; i++){
        res.push(l.slice(i, i + len_sublist));
      }
    }
    return res;
}

// Exercise 4
function pigLatin(word) {
    const isUpper = (word[0] == word[0].toUpperCase());
    word = word.toLowerCase();
    var i = word.length - 1;
    var char = word[i];
    while (!(/[a-zA-Z0-9]/.test(char))) {
      i--;
      char = word[i];
    }
}

// Exercise 5
function morseCode(message) {
    return undefined
}

// Exercise 6
function int2Text(num) {
    return undefined
}

// Exercise 7
function missingComment(filename) {
    return undefined
}

// Exercise 8
function consistentLineLength(filename, length) {
    return undefined
}

// Exercise 9
function knight(start, end, moves) {
    return undefined
}

// Exercise 10
function warOfSpecies(environment) {
    return undefined
}

module.exports = {
    reduceFraction: reduceFraction,
    isMagicDate: isMagicDate,
    sublist: sublist,
    pigLatin: pigLatin,
    morseCode: morseCode,
    int2Text: int2Text,
    missingComment: missingComment,
    consistentLineLength: consistentLineLength,
    knight: knight,
    warOfSpecies: warOfSpecies
}

console.log(pigLatin('Alelujah'))
