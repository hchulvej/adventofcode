const fs = require('fs');

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

let translate = {};
for (const v of rawValves) {
    translate[v[0]] = rawValves.indexOf(v);
}

let indexedValves = [];
for (const v of rawValves) {
    v[0] = translate[v[0]];
    v[2] = v[2].map(t => translate[t]);
    indexedValves.push(v);
}

const flowingValves = indexedValves.filter(v => v[1] > 0);

let state = '0'.repeat(flowingValves.length);

console.log(state, flowingValves);
