const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_18.txt');

const coordinates = puzzleData.map(s => s.split(',').map(t => Number(t)));

// x in [0;18], y in [1;18], z in [0;19]

/*
    Different strategy: model the six faces as the midpoints of the cube

    The 1-1-1 cube has faces
        px: [1, 1/2, 1/2]
        nx: [0, 1/2, 1/2]
        py: [1/2, 1, 1/2]
        ny: [1/2, 0, 1/2]
        pz: [1/2, 1/2, 1]
        nz: [1/2, 1/2, 0]

    All other faces are vector translations of these faces
*/
const encode = (coords) => {
    return `(${coords[0]}, ${coords[1]}, ${coords[2]})`;
}

const decode = (str) => {
    str = str.slice(1, str.length - 1);
    return str.split(',').map(t => Number(t));
}

const baseCube = new Set();
for (let c = 0; c < 2; c++) {
    baseCube.add(encode([c, 0.5, 0.5]));
    baseCube.add(encode([0.5, c, 0.5]));
    baseCube.add(encode([0.5, 0.5, c]));
}

const createCube = (coords) => {
    let base = Array.from(baseCube).map(decode);
    let [x, y, z] = [...coords];
    return new Set(base.map(c => [c[0] + x - 1, c[1] + y - 1, c[2] + z - 1]).map(encode));
}

let cubes = [];
let faces = new Set();
for (const coords of coordinates) {
    let cube = createCube(coords);
    cubes.push(cube);
    cube.forEach(f => faces.add(f));
}

/*
    A face is covered if another cube shares the face
*/
let uncovered = cubes.length * 6; // No faces covered
for (let i = 0; i < cubes.length; i++) {
    for (let j = i + 1; j < cubes.length; j++) {
        if (Array.from(cubes[i]).filter(x => cubes[j].has(x)).length > 0) {
            uncovered -= 2;
        }
    }
}

console.log(uncovered);
console.log(faces.size * 2 - 6 * cubes.length);

/*
    We want to find the trapped air pockets.
*/

// Boundaries
// minX, maxX, minY, maxY, minZ, maxZ
let boundaries = [Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY];
faces.forEach(f => {
    let [x, y, z] = decode(f);
    boundaries[0] = Math.min(boundaries[0], x);
    boundaries[1] = Math.max(boundaries[1], x);
    boundaries[2] = Math.min(boundaries[2], y);
    boundaries[3] = Math.max(boundaries[3], y);
    boundaries[4] = Math.min(boundaries[4], z);
    boundaries[5] = Math.max(boundaries[5], z);
    return
});

const outOfBounds = (face) => {
    let [x, y, z] = decode(face);
    if (boundaries[0] > x
        || boundaries[1] < x
        || boundaries[2] > y
        || boundaries[3] < y
        || boundaries[4] > z
        || boundaries[5] < z) {
            return true;
        }
    return false;
}

let connectedFaces = (face) => {
    let connected = new Set();
    cubes.forEach(c => {
        if (c.has(face)) {
            c.forEach(f => connected.add(f));
        }
    })
}