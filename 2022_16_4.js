const fs = require('fs');
const jsc = require('js-combinatorics');

const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_16.txt');

let valves = [];
let flowrates = {};
let neighbours = {};

const parseLine = (line) => {
    let name = line.split(' ')[1];
    valves.push(name);
    flowrates[name] = Number.parseInt(line.split(' ')[4].split('=')[1].replace(';', ''));
    let temp = line.replaceAll('valves', 'valve').split(' ').slice(1);
    neighbours[name] = temp.slice(temp.indexOf('valve') + 1).map(x => x.replace(',',  ''));
}

puzzleData.forEach(parseLine);

// Parsing done

/*
    Calculating the distance from one node to the rest

    Shortest path between all vertices: Floyd–Warshall

    https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
*/
let dist = {};
for (let i = 0; i < valves.length; i++) {
    dist[valves[i]] = {};
    for (let j = 0; j < valves.length; j++) {
        if (i === j) {
            // Same node
            dist[valves[i]][valves[j]] = 0;
        } else {
            if (neighbours[valves[i]].includes(valves[j])) {
                // Neighbour node
                dist[valves[i]][valves[j]] = 1;
            } else {
                // Not discovered yet
                dist[valves[i]][valves[j]] = Number.POSITIVE_INFINITY;
            }
        }
    }
}

for (let k = 0; k < valves.length; k++) {
    for (let i = 0; i < valves.length; i++) {
        for (let j = 0; j < valves.length; j++){
            if (dist[valves[i]][valves[j]] > dist[valves[i]][valves[k]] + dist[valves[k]][valves[j]]) {
                dist[valves[i]][valves[j]] = dist[valves[i]][valves[k]] + dist[valves[k]][valves[j]];
            }
        }
    }
}


/*
    Part One: depth first search
*/
let valvesWithFlow = valves.filter(v => flowrates[v] > 0);

const dfs = (allValves, valve, remainingTime, openedValves, canOpen, cache = {}) => {
    const key = `${allValves.join(',')}.${valve}.${remainingTime}.${openedValves.join(',')}.${canOpen.join('.')}`;

    if (key in cache) {
        return cache[key];
    }

    let openedFlow = openedValves.reduce((p, c) => p + flowrates[c], 0);

    let maxVal = openedFlow * remainingTime; // i.e. do nothing

    for (let [v, d] of Object.entries(dist[valve]).filter(([v, d]) => d > 0 && canOpen.includes(v))) {
        if (d < remainingTime) {
            if  (!openedValves.includes(v)) {
                // we go to the neighbour and open the valve if its flowrate is positive
                if (flowrates[v] > 0) {
                    maxVal = Math.max(maxVal, openedFlow * (d + 1) + dfs(allValves, v, remainingTime - d - 1, [...openedValves, v], canOpen, cache));
                }
            }
        }
    }

    cache[key] = maxVal;

    return maxVal;
};

console.log(dfs(valves, 'AA', 30, [], valvesWithFlow));


/*
    Part Two
*/
let P = new jsc.PowerSet(valvesWithFlow);

const complementary = (arr) => {
    return valvesWithFlow.filter(x => !arr.includes(x));
}

let newMax = 0;
for (let s of P) {
    newMax = Math.max(newMax, dfs(valves, 'AA', 26, [], s) + dfs(valves, 'AA', 26, [], complementary(s)));
}

console.log(newMax);
