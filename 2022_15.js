const fs = require('fs');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_15.txt');

const parseLine = (line) => {
    const arr = line.split(' ');
    const clean = (str) => {
        let res = str.replace('x=', '')
            .replace('y=', '')
            .replace(':', '')
            .replace(',', '');
        return res;
    }
    return [2, 3, 8, 9].map(x => arr[x]).map(clean).map(x => Number(x));
}

class Sensor {
    constructor(coordinates) {
        this.x = coordinates[0];
        this.y = coordinates[1];
        this.bx = coordinates[2];
        this.by = coordinates[3];
        this.distanceToBeacon = this.dist(this.bx, this.by);
    }

    dist(x, y) {
        return Math.abs(x - this.x) + Math.abs(y - this.y);
    }

    closer(x, y) {
        return this.dist(x, y) <= this.distanceToBeacon;
    }

    limits(y) {
        return [this.x - this.distanceToBeacon, this.x + this.distanceToBeacon];
    }

    beaconPos() {
        return `${this.bx}.${this.by}`;
    }
}

let sensors = [];
for (const line of puzzleData) {
    sensors.push(new Sensor(parseLine(line)))
}

const noBeacons = (y) => {
    let leftLimit = Number.POSITIVE_INFINITY;
    let rightLimit = Number.NEGATIVE_INFINITY;
    let beacons = new Set();
    let notHere = 0;

    for (const sensor of sensors) {
        leftLimit = Math.min(leftLimit, sensor.limits(y)[0]);
        rightLimit = Math.max(rightLimit, sensor.limits(y)[1]);
        beacons.add(sensor.beaconPos());
    }

    for (let x = leftLimit; x <= rightLimit; x++) {
        let here = true;
        for (const sensor of sensors) {
            if (sensor.closer(x, y)) {
                here = false;
            }
        }
        if (!here && !beacons.has(`${x}.${y}`)) {
            notHere++;
        }
    }
    return notHere;
}

console.log(noBeacons(2000000));