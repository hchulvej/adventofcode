const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_18.txt');

const coordinates = puzzleData.map(s => s.split(',').map(t => Number(t)));

// x in [0;18], y in [1;18], z in [0;19]

let outerArea = 0;

// XY
for (let x = 0; x < 19; x++) {
    for (let y = 1; y < 19; y++) {
        if (coordinates.filter(c => c[0] === x && c[1] === y).length > 0) {
            outerArea += 2;
        }
    }
}

// XZ
for (let x = 0; x < 19; x++) {
    for (let z = 0; z < 20; z++) {
        if (coordinates.filter(c => c[0] === x && c[2] === z).length > 0) {
            outerArea += 2;
        }
    }
}

// YZ
for (let y = 1; y < 19; y++) {
    for (let z = 0; z < 20; z++) {
        if (coordinates.filter(c => c[1] === y && c[2] === z).length > 0) {
            outerArea += 2;
        }
    }
}

console.log(outerArea);