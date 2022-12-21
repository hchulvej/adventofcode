const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_14.txt');

const encode = (x, y, type) => {
    return `${x}.${y}.${type}`;
}

const decode = (str) => {
    let arr = str.split('.');
    return [Number(arr[0]), Number(arr[1]), arr[2]];
}

const pathToTiles = (path) => {
    let tiles = new Set();
    const instructions = path.split('->').map(x => x.trim()).map(y => y.split(',').map(z => Number(z)));

    for (let i = 0; i < instructions.length - 1; i++) {
        const endPoint1 = instructions[i];
        const endPoint2 = instructions[i + 1];
        
        if (endPoint1[0] === endPoint2[0]) {
            for (let j = Math.min(endPoint1[1], endPoint2[1]); j <= Math.max(endPoint1[1], endPoint2[1]); j++) {
                tiles.add(encode(endPoint1[0], j, 'rock'));
            }
        }
        if (endPoint1[1] === endPoint2[1]) {
            for (let j = Math.min(endPoint1[0], endPoint2[0]); j <= Math.max(endPoint1[0], endPoint2[0]); j++) {
                tiles.add(encode(j, endPoint1[1], 'rock'));
            }
        }
    }
    return tiles;
}

let allTiles = new Set();
for (const path of puzzleData) {
    pathToTiles(path).forEach(x => allTiles.add(x));
}

/*
    Sand flows from (500,0)
*/
let lowestRockLevel = new Map();
allTiles.forEach(tile => {
    const rockTile = decode(tile).slice(0,2);
    if (!lowestRockLevel.has(rockTile[0]) || lowestRockLevel.get(rockTile[0]) < rockTile[1]) {
        lowestRockLevel.set(rockTile[0], rockTile[1]);
    }
})

const fallsToAbyssFrom = (x, y) => {
    if (!lowestRockLevel.has(x) || lowestRockLevel.get(x) < y) {
        return true;
    }
    return false;
}

let unitsDropped = 0;
let stop = false;

const dropUnitOfSand = () => {
    let posX = 500;
    let posY = 0;
    let rests = false;

    while (!rests && !fallsToAbyssFrom(posX, posY)) {
        
    }
}
