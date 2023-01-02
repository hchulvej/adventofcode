const fs = require('fs');


const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_17_small.txt');


/*
    Setting up the cave

    7 units wide (x = 0..6)

    floor is at y-level 0
*/