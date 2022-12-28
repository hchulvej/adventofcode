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

//console.log(rawValves);

let vi = {};
for (const valve of rawValves) {
    vi[valve[0]] = rawValves.indexOf(valve);
}

//console.log(vi);

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
    Trying to follow Jonathan Paulsen's method
*/
const setToKey = (S) => {
    if (S.size === 0) {
        return 0;
    }
    let num = 0;
    S.forEach(x => num += 2 ** x);
    return num;
}
let DP = new Array();

const score = (position, openValves, timeLeft, otherPlayers) => {

    if (timeLeft === 0) {
        if (otherPlayers === 1) {
            //console.log('here');
            return score(0, openValves, 26, 0);
        } else {
            return 0;
        }
    }

    let key = setToKey(openValves).toString() +  (valvesWithFlow.length * 100000 + position * 10000000 + timeLeft * 1000000000 + otherPlayers).toString();
    
    if (DP[key] > 0) {
        return DP[key];
    }

    let ans = 0;
    let alreadyOpen = openValves.has(position);

    if (!alreadyOpen && valvesWithFlow.includes(position)) {
        let newOpenValves = new Set([position]);
        openValves.forEach(x => newOpenValves.add(x));
        ans = Math.max(ans, rawValves[position][1] * (timeLeft - 1) + score(position, newOpenValves, timeLeft - 1, otherPlayers));
    }
    for (const v of rawValves[position][2].map(t => vi[t])) {
        ans = Math.max(ans, score(v, openValves, timeLeft - 1, otherPlayers));
    }

    DP[key] = ans;

    
    return ans;
}

console.log(score(0, new Set(), 30, 0));
console.log(score(0, new Set(), 26, 1));