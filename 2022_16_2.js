const fs = require('fs');

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

let DP = new Map();

const score = (position, valves, openValves, timeLeft) => {

    if (timeLeft === 0) {
        return 0;
    }

    let key = `p=${position}.${valves.join('v')}.${Array.from(openValves).join('o')}.${timeLeft}`;

    if (DP.has(key)) {
        return DP.get(key);
    }

    let ans = 0;
    let alreadyOpen = openValves.has(position);


    if (!alreadyOpen && flowingValves.includes(position)) {
        let newOpenValves = new Set([position]);
        openValves.forEach(x => newOpenValves.add(x));
        ans = Math.max(ans, indexedValves[position][1] * (timeLeft - 1) + score(position, valves, newOpenValves, timeLeft - 1));
    }
    
    for (const newPos of indexedValves[position][2].filter(x => valves.includes(x))) {
        ans = Math.max(ans, score(newPos, valves, openValves, timeLeft - 1));
    }

    DP.set(key, ans);
    
    return ans;
}

console.log(score(0, [...Array(indexedValves.length).keys()], new Set(), 30));

