const fs = require('fs');
const jsc = require('js-combinatorics');


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
}

let cubes = [];
coordinates.forEach(c => cubes.push(new Cube(c)));

let actualArea = 6 * cubes.length;

for (const pair of new jsc.Combination(cubes, 2)) {
    if (pair[0].isNeighbor(pair[1])) {
        actualArea -= 2;
    }
}

console.log(actualArea);