const fs = require('fs');
const hash = require('object-hash');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_16.txt');

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

const flowingValves = indexedValves.filter(v => v[1] > 0).map(v => v[0]);

let DP = {};

const score = (position, valves, openValves, timeLeft) => {

    if (timeLeft === 0) {
        return 0;
    }

    let key = `p${position}.v${hash(valves)}.o${openValves}.t${timeLeft}`;

    if (key in DP) {
        return DP[key];
    }

    let ans = 0;
    let alreadyOpen = openValves & (1 << position);


    if (!alreadyOpen) {
        if (valves[position][1] > 0) {
            let newOpenValves = openValves | (1 << position);
            ans = Math.max(ans, valves[position][1] * (timeLeft - 1) + score(position, valves, newOpenValves, timeLeft - 1));
        }
    }
    
    for (const newPos of valves[position][2]) {
        ans = Math.max(ans, score(newPos, valves, openValves, timeLeft - 1));
    }

    DP[key] = ans;
    
    return ans;
}

console.log(score(0, indexedValves, 0, 30));

