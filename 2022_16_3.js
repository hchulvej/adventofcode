const fs = require('fs');
const hash = require('object-hash');

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



rawValves.sort((v1, v2) => {
    if (v1[0] === 'AA' || v2[0] === 'AA') {
        return Number.POSITIVE_INFINITY;
    }
    return v2[1] - v1[1];
});

// console.log(rawValves[8])

let translate = {};
for (const v of rawValves) {
    translate[v[0]] = rawValves.indexOf(v);
}

// Translate to indices
for (const v of rawValves) {
    v[0] = translate[v[0]];
    v[2] = v[2].map(t => translate[t]);
}

// Flowing valves
const flowingValves = rawValves.filter(valve => valve[1] > 0);
const nonFlowingValves = rawValves.filter(valve => valve[1] === 0 && valve[0] > 0);


const valveIndices = rawValves.map(valve => valve[0]);
const flowingIndices = flowingValves.map(valve => valve[0]);
const nonFlowingIndices = nonFlowingValves.map(valve => valve[0]);

// Creating distances from every node to every other node
let dist = new Map();

for (const ind of valveIndices) {

    dist.set(ind, new Map());
    dist.get(ind).set(ind, 0).set(0, 0);

    let visited = new Set();
    visited.add(ind);

    let queue = [[0, ind]];

    while (queue.length > 0) {
        let [distance, position] = queue.shift();
        for (const neighbor of rawValves[position][2]) {
            if (visited.has(neighbor)) {
                continue;
            } else {
                visited.add(neighbor);
                dist.get(ind).set(neighbor, distance + 1);
                queue.push([distance + 1, neighbor]);
            }
        }
    }

    dist.get(ind).delete(ind);
    if (ind > 0) {
        dist.get(ind).delete(0);
    }
}

// Clean up the non-flowing valves
for (const ind of valveIndices) {
    for (const nf of nonFlowingIndices) {
        if (dist.get(ind).has(nf)) {
            dist.get(ind).delete(nf);
        }
    }
}

console.log(dist.get(0));

/*
    Part One
*/
let cache = {};

const solve = (timeLeft, position, openvalves) => {

    let key = `${timeLeft}s.${position}p.${openvalves}v`;

    if (key in cache) {
        return cache[key];
    }

    let maxval = 0;

    let toValves = Array.from(dist.get(position).keys());
    
    for (const v of toValves) {
        openbit = 1 << v;
        if (openvalves & openbit) {
            continue;
            // already open
        }
        remTime = timeLeft - 1 - dist.get(position).get(v);
        if (remTime <= 0) {
             continue;
        } 
        maxval = Math.max(maxval, solve(remTime, v, openvalves | openbit) + remTime * rawValves[v][1]);
         }

    

    cache[key] = maxval;
    return maxval;
}

console.log(solve(30, 0, 0));

