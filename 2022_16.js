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
const encode = (arr) => {
    return arr.join('.');
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
            dist[encode([i, j])] = 0;
            next[encode([i, j])] = i;
        }
        if (rawValves[i][2].includes(rawValves[j][0])) {
            dist[encode([i, j])] = 1;
            next[encode([i, j])] = j;
        } else if (i !== j) {
            dist[encode([i, j])] = Number.POSITIVE_INFINITY;
            next[encode([i, j])] = null;
        }
    }
}

for (let k = 0; k < numV; k++) {
    for (let i = 0; i < numV; i++) {
        for (let j = 0; j < numV; j++) {
            if (dist[encode([i, j])] > dist[encode([i, k])] + dist[encode([k, j])]) {
                dist[encode([i, j])] = dist[encode([i, k])] + dist[encode([k, j])];
                next[encode([i, j])] = next[encode([i, k])];
            }
        }
    }
}

/*
    All possible ways through (ignoring 0-valves)
*/
let possiblePaths = new Combinatorics.Permutation(valvesWithFlow);

const startTime = 30;
let memoScore = {'0': [0, startTime]};


// Set up the first valve
// Assumes that a possitive valve will always be opened (possibly wrong?)
for (let i = 1; i < rawValves.length; i++) {
    let timeSpent = dist['0.' + i.toString()] + rawValves[i][1] > 0 ? 1 : 0;
    memoScore['0.' + i.toString()] = [rawValves[i][1] * (startTime - timeSpent), startTime - timeSpent];
}

const processPath = (path) => {
    let existingPath = '0.' + path.shift().toString();
    while (existingPath in memoScore) {
        existingPath += path.shift().toString();
    }
    if (path.length === 0) {
        return memoScore[existingPath];
    }
    while (path.length > 0) {
        let currentScore = memoScore[existingPath][0];
        let timeRemaining = memoScore[existingPath][1];
        let nextDestination = path.shift().toString();
        let timeNeeded = dist[existingPath.slice(-1) + '.' + nextDestination];
        if (rawValves[Number(nextDestination)][1]> 0) {
            timeNeeded++;
        }
        if (timeRemaining < timeNeeded) {
            memoScore[encode(path)] = [currentScore, 0];
        } else {
            currentScore += rawValves[Number(nextDestination)][1] * (timeRemaining - timeNeeded);
            memoScore[existingPath + nextDestination] = [currentScore, timeRemaining - timeNeeded];
        }  
    }
    return memoScore[path];
}


let maxScore = 0;



console.log(processPath([2,4,5,6]));
