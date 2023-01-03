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

    visibleArea() {
        return 6 - this.neighbors.size;
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