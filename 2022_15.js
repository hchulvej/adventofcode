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
    A point doesn't have a beacon, if there is a sensor closer to it
    than the sensor's distance to the closest beacon

    When counting, remember to subtract known beacons
*/
const possibleNewBeacon = (x,y) => {
    for (const sensor of sensors) {
        if (dist(x, y, ...decode(sensor[0])) <= sensor[1]) {
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

// console.log(min_x, max_x);

const noBeacons = (y) => {
    let countS = 0;
    let countB = 0;
    for (let x = min_x; x <= max_x; x++) {
        if (!possibleNewBeacon(x, y)) {
            countS++;
        }
        if (beacons.includes(encode(x, y))) {
            countB++;
        }
    }
    return countS - countB;
}

const partOne = false;
if (partOne) {
    console.log(noBeacons(2000000));
}


/*
    Part Two:

    Main idea:

    Only check borders around no-beacon areas of sensors

    i.e. where the distance is 1 + distance to nearest beacon

    The unique point must be on an intersection of two borders
*/
const check = (x, y) => {
    if (x < 0 || y < 0 || x > 4000000 || y > 4000000) {
        return false;
    }
    return possibleNewBeacon(x, y) && !beacons.includes(encode(x,y));
}

const discretePath = (s_x, s_y, dist) => {
    return (t) => {
        if (t >= 4 * dist) {
            t = t % (4 * dist); 
        }
        if (t >= 0 && t < dist) {
            return [s_x + dist - t, s_y + t];
        }
        if (t >= dist && t < 2 * dist) {
            return [s_x + dist - t, s_y + 2 * dist - t];
        }
        if (t >= 2 * dist && t < 3 * dist) {
            return [s_x - 3 * dist + t, s_y + 2 * dist - t];
        }
        if (t >= 3 * dist && t < 4 * dist) {
            return [s_x - 3 * dist + t, s_y - 4 * dist + t];
        }
    }
} 

const intersection = (sensor1, sensor2) => {
    if (dist(...decode(sensor1[0]), ...decode(sensor2[0])) > sensor1[1] + sensor2[1] + 2) {
        return new Set();
    }
    let res = new Set();
    if (sensor1[1] > sensor2[1]) {
        return intersection(sensor2, sensor1);
    }
    let p = discretePath(...decode(sensor1[0]), sensor1[1] + 1);
    for (let t = 0; t < 4 * sensor1[1]; t++) {
        if (dist(...p(t), ...decode(sensor2[0])) === sensor2[1] + 1) {
            res.add(encode(...p(t)));
        }
    }
    return res;
}

let possibilities = new Set();

for (let i = 0; i < sensors.length - 1; i++) {
    for (let k = 1; k + i < sensors.length; k++) {
        let intSec = intersection(sensors[i], sensors[i + k]);
        if (intSec.size > 0) {
            intSec.forEach(element => {
                possibilities.add(element);
            });
        }
    }
}

for (const p of Array.from(possibilities)) {
    if (check(...decode(p))) {
        let [p_x, p_y] = decode(p);
        console.log(p_x * 4000000 + p_y);
        break;
    }
}

