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

/*
    Sensors, beacons and distances

    sensor: ["s_x.s_y", dist]
    beacon: ["b_x.b_y"]
*/
const dist = (x1, y1, x2, y2) => {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

const encode = (x, y) => {
    return `${x}.${y}`;
}

const decode = (coords) => {
    return coords.split('.').map(t => Number(t));
}

let sensors = [];
let beacons = [];

for (const line of puzzleData) {
    const [s_x, s_y, b_x, b_y] = parseLine(line);
    sensors.push([encode(s_x, s_y), dist(s_x, s_y, b_x, b_y)]);
    beacons.push(encode(b_x, b_y));
}

/*
    A point (with no known beacon) doesn't have a beacon, if there is a sensor closer to it
    than the sensor's distance to the closest beacon
*/
const possibleNewBeacon = (x,y) => {
    if (beacons.includes(encode(x, y))) {
        return false;
    }
    for (const sensor of sensors) {
        if (dist(x, y, ...sensor[0]) <= sensor[1]) {
            return false;
        }
    }
    return true;
}

let min_x = Number.POSITIVE_INFINITY;
let max_x = Number.NEGATIVE_INFINITY;
let min_y = Number.POSITIVE_INFINITY;
let max_y = Number.NEGATIVE_INFINITY;
for (const sensor of sensors) {
    let [s_x, s_y] = decode(sensor[0]);
    min_x = Math.min(min_x, s_x - sensor[1]);
    max_x = Math.max(max_x, s_x + sensor[1]);
    min_y = Math.min(min_y, s_y - sensor[1]);
    max_y = Math.max(max_y, s_y + sensor[1]);
}


console.log(min_x, max_x, min_y, max_y);

