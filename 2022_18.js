const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_18.txt');

const coordinates = puzzleData.map(s => s.split(',').map(t => Number(t)));

/*
    Cubes
*/
class Cube {
    constructor(coords) {
        this.x = coords[0];
        this.y = coords[1];
        this.z = coords[2];
        this.neighbors = new Set();
    }

    getx() {
        return this.x;
    }

    gety() {
        return this.y;
    }

    getz() {
        return this.z;
    }

    isNeighbor(other) {
        return (Math.abs(this.x - other.getx()) === 1 && this.y === other.gety() && this.z === other.getz())
            || (Math.abs(this.y - other.gety()) === 1 && this.x === other.getx() && this.z === other.getz())
            || (Math.abs(this.z - other.getz()) === 1 && this.y === other.gety() && this.x === other.getx())
    }

    addNeighbor(other) {
        this.neighbors.add(other);
    }

    getNeighbors() {
        return this.neighbors;
    }

    visibleArea() {
        return 6 - this.neighbors.size;
    }

    equals(other) {
        return this.x === other.getx() && this.y === other.gety() && this.z === other.getz();
    }
}



let cubes = [];
coordinates.forEach(c => cubes.push(new Cube(c)));

for (let i = 0; i < cubes.length; i++) {
    for (let j = i; j < cubes.length; j++) {
        if (cubes[i].isNeighbor(cubes[j])) {
            cubes[i].addNeighbor(cubes[j]);
            cubes[j].addNeighbor(cubes[i]);
        }
    }
}

let area = 0;
cubes.forEach(c => area += c.visibleArea());

console.log(area);

// Setting the boundaries
// minX, maxX, minY, maxY, minZ, maxZ
let boundaries = [Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY];
for (const cube of cubes) {
    boundaries[0] = Math.min(boundaries[0], cube.getx());
    boundaries[1] = Math.max(boundaries[1], cube.getx());
    boundaries[2] = Math.min(boundaries[2], cube.gety());
    boundaries[3] = Math.max(boundaries[3], cube.gety());
    boundaries[4] = Math.min(boundaries[4], cube.getz());
    boundaries[5] = Math.max(boundaries[5], cube.getz());
}

const outOfBounds = (cube) => {
    if (cube.getx() < boundaries[0]) {
        return true;
    }
    if (cube.getx() > boundaries[1]) {
        return true;
    }
    if (cube.gety() < boundaries[2]) {
        return true;
    }
    if (cube.gety() > boundaries[3]) {
        return true;
    }
    if (cube.getz() < boundaries[4]) {
        return true;
    }
    if (cube.getz() > boundaries[5]) {
        return true;
    }
    return false;
}

const newCube = (coords) => {
    let cube = new Cube(coords);
    let [x, y, z] = [cube.getx(), cube.gety(), cube.getz()];
    for (let d = -1; d < 2; d+= 2) {
        cube.addNeighbor(new Cube([x + d, y, z]));
        cube.addNeighbor(new Cube([x, y + d, z]));
        cube.addNeighbor(new Cube([x, y, z + d]));
    }
    return cube;
}

