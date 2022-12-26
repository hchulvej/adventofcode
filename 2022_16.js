const fs = require('fs');
const Combinatorics = require('js-combinatorics')


const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_16_small.txt');

const parseLine = (line) => {
    let name = line.split(' ')[1];
    let flowrate = Number(line.split('=')[1].split(';')[0]);
    let valves;
    if (line.includes('valves')) {
        valves = line.split('valves')[1].trim().split(', ');
    } else {
        valves = [line.split(' ').pop()];
    }
    return [name, flowrate, valves];
}

let rawValves = [];
puzzleData.forEach(line => rawValves.push(parseLine(line)));

// console.log(rawValves);

/*
    Shortest path between all vertices: Floyd–Warshall

    https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
*/
const encode = (x,y) => {
    return `${x}.${y}`;
}
const decode = (str) => {
    return str.split('.').map(t => Number(t));
}

let numV = rawValves.length;
let dist = {};
let next = {};
let valvesWithFlow = [];

for (let i = 0; i < numV; i++) {
    if (rawValves[i][1] > 0) {
        valvesWithFlow.push(i);
    }
    for (let j = 0; j < numV; j++) {
        if (i === j) {
            dist[encode(i, j)] = 0;
            next[encode(i, j)] = i;
        }
        if (rawValves[i][2].includes(rawValves[j][0])) {
            dist[encode(i, j)] = 1;
            next[encode(i, j)] = j;
        } else if (i !== j) {
            dist[encode(i, j)] = Number.POSITIVE_INFINITY;
            next[encode(i, j)] = null;
        }
    }
}

for (let k = 0; k < numV; k++) {
    for (let i = 0; i < numV; i++) {
        for (let j = 0; j < numV; j++) {
            if (dist[encode(i, j)] > dist[encode(i, k)] + dist[encode(k, j)]) {
                dist[encode(i, j)] = dist[encode(i, k)] + dist[encode(k, j)];
                next[encode(i, j)] = next[encode(i, k)];
            }
        }
    }
}

/*
    All possible ways through (ignoring 0-valves)
*/
let possiblePaths = new Combinatorics.Permutation(valvesWithFlow);

console.log(possiblePaths);
