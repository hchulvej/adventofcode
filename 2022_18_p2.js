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
    We want to find the surface air pockets by slicing
*/
const faceArray = Array.from(faces).map(f => decode(f));

let surfaceAir = [];

// XY-plane (Z var)
for (x = -1; x < 21; x++) {
    for (y = -1; y < 21; y++) {
        let minZ = Number.POSITIVE_INFINITY;
        let maxZ = Number.NEGATIVE_INFINITY;
        const slice = faceArray.filter(arr => arr[0] === x && arr[1] === y);
        if (slice.length === 0) {
            continue;
        } else {
            minZ = Math.min(minZ, ...slice.map(arr => arr[2]));
            maxZ = Math.max(maxZ, ...slice.map(arr => arr[2]));
            surfaceAir.push(encode([x, y, minZ]));
            surfaceAir.push(encode([x, y, maxZ]));
        }
    }
}

// XZ-plane (Y var)
for (x = -1; x < 21; x++) {
    for (z = -1; z < 21; z++) {
        let minY = Number.POSITIVE_INFINITY;
        let maxY = Number.NEGATIVE_INFINITY;
        const slice = faceArray.filter(arr => arr[0] === x && arr[2] === z);
        if (slice.length === 0) {
            continue;
        } else {
            minY = Math.min(minY, ...slice.map(arr => arr[1]));
            maxY = Math.max(maxY, ...slice.map(arr => arr[1]));
            surfaceAir.push(encode([x, minY, z]));
            surfaceAir.push(encode([x, maxY, z]));
        }
    }
}

// YZ-plane (X var)
for (y = -1; y < 21; y++) {
    for (z = -1; z < 21; z++) {
        let minX = Number.POSITIVE_INFINITY;
        let maxX = Number.NEGATIVE_INFINITY;
        const slice = faceArray.filter(arr => arr[1] === y && arr[2] === z);
        if (slice.length === 0) {
            continue;
        } else {
            minY = Math.min(minX, ...slice.map(arr => arr[0]));
            maxY = Math.max(maxX, ...slice.map(arr => arr[0]));
            surfaceAir.push(encode([minX, y, z]));
            surfaceAir.push(encode([maxX, y, z]));
        }
    }
}

console.log(faceArray);