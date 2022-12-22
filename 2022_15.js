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

    sensorPos() {
        return [this.x, this.y];
    }

    getDistanceToBeacon() {
        return this.distanceToBeacon;
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

// console.log(noBeacons(2000000));

/*
    Part Two: grid 0-4000000 x2
*/
const perimeter = (sensor) => {
    const [sx, sy] = sensor.sensorPos();
    const radius = sensor.getDistanceToBeacon() + 1;
    // Top, Right, Bottom, Left
    const corners = [[sx, sy + radius], [sx + radius, sy], [sx, sy - radius], [sx - radius, sy]];
    // Line from (x1,y1) and (x2,y2)
    // Top->Right: slope = -1
    // y + x = sx + sy + radius
    // Right->Bottom: slope = 1
    // y - x = sy - sx - radius
    // Bottom->Left: slope = -1
    // y + x = sx + sy - radius
    // Left->Top: slope = 1
    // y - x = sy - sx + radius
    return [[-1, sx + sy + radius], [1, sy - sx - radius], [-1, sx + sy - radius], [1, sy - sx + radius]];
}

console.log(perimeter(sensors[0]));