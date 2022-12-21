const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_14.txt');

console.log(puzzleData);