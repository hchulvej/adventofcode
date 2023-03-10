const fs = require('fs');
const { PassThrough } = require('stream');

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

const nextPos = (x, y) => {
    if (
      !allTiles.has(encode(x, y + 1, "rock")) &&
      !allTiles.has(encode(x, y + 1, "sand"))
    ) {
      return [x, y + 1];
    }
    if (
      !allTiles.has(encode(x - 1, y + 1, "rock")) &&
      !allTiles.has(encode(x - 1, y + 1, "sand"))
    ) {
      return [x - 1, y + 1];
    }
    if (
      !allTiles.has(encode(x + 1, y + 1, "rock")) &&
      !allTiles.has(encode(x + 1, y + 1, "sand"))
    ) {
      return [x + 1, y + 1];
    }
    return false;
  };

const partOne = false;

if (partOne) {
  let unitsDropped = 0;
  let stop = false;

  const dropUnitOfSand = () => {
    let posX = 500;
    let posY = 0;
    let rests = false;

    if (fallsToAbyssFrom(posX, posY)) {
      unitsDropped++;
      return true;
    }

    while (nextPos(posX, posY) && !fallsToAbyssFrom(posX, posY)) {
      [posX, posY] = nextPos(posX, posY);
    }

    if (fallsToAbyssFrom(posX, posY)) {
      unitsDropped++;
      return true;
    } else {
      unitsDropped++;
      allTiles.add(encode(posX, posY, "sand"));
      return false;
    }
  };

  console.log(allTiles.size, unitsDropped);
  while (!dropUnitOfSand()) {
    continue;
  }
  console.log(allTiles.size, unitsDropped);
}

/*
    Part Two
*/
const partTwo = true;

if (partTwo) {

    // Create the floor
    let leftEdge = 500;
    let rightEdge = 500;
    let depth = 0;
    allTiles.forEach((tile) => {
        const rockTile = decode(tile).slice(0,2);
        leftEdge = Math.min(leftEdge, rockTile[0]);
        rightEdge = Math.max(rightEdge, rockTile[0]);
        depth = Math.max(depth, rockTile[1]);
    });

    leftEdge = leftEdge - 1 * depth;
    rightEdge = rightEdge + 1 * depth;
    depth = depth + 2;

    for (let x = leftEdge; x <= rightEdge; x++) {
        allTiles.add(encode(x, depth, 'rock'));
    }

    let unitsDropped = 0;

    // Start pouring
    const dropUnitOfSand = () => {
        let posX = 500;
        let posY = 0;
        

        while (nextPos(posX, posY)) {
            [posX, posY] = nextPos(posX, posY);
        }

        unitsDropped++;
        allTiles.add(encode(posX, posY, 'sand'));

        if (posX === 500 && posY === 0) {
            return true;
        } else {
            return false;
        }
    }

    const draw = () => {
        for (let y = 0; y <= depth; y++) {
          let hor = "";
          for (let x = leftEdge; x <= rightEdge; x++) {
            if (allTiles.has(encode(x, y, "rock"))) {
              hor += "#";
            } else if (allTiles.has(encode(x, y, "sand"))) {
              hor += "O";
            } else {
              hor += ".";
            }
          }
          console.log(hor);
        }
      };

    console.log(allTiles.size, unitsDropped);
   
    while (!dropUnitOfSand()) {
        continue;
    }
    console.log(allTiles.size, unitsDropped);
    
}

