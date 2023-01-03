const fs = require('fs');


const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_17.txt');

/*
    Setting up the cave

    7 units wide (x = 0..6)

    floor is at y-level 0
*/
const encode = (arr) => {
    return arr.join('.');
}

const getY = (str) => {
    return Number(str.split('.')[1]);
}


class Rock {
    constructor(type, topLeftX, highestY) {
        this.type = type;
        // Type: ####
        if (type === 0) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 3];
            this.yvals = [highestY + 4, highestY + 4, highestY + 4, highestY + 4];
        }
        // Type: .#.
        //       ###
        //       .#.
        if (type === 1) {
            this.xvals = [topLeftX + 1, topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 1];
            this.yvals = [highestY + 6, highestY + 5, highestY + 5, highestY + 5, highestY + 4];
        }
        // Type: ..#
        //       ..#
        //       ###
        if (type === 2) {
            this.xvals = [topLeftX + 2, topLeftX + 2, topLeftX, topLeftX + 1, topLeftX + 2];
            this.yvals = [highestY + 6, highestY + 5, highestY + 4, highestY + 4, highestY + 4];
        }
        // Type: #
        //       #
        //       #
        //       #
        if (type === 3) {
            this.xvals = [topLeftX, topLeftX, topLeftX, topLeftX];
            this.yvals = [highestY + 7, highestY + 6, highestY + 5, highestY + 4];
        }
        // Type: ##
        //       ##
        if (type === 4) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX, topLeftX + 1];
            this.yvals = [highestY + 5, highestY + 5, highestY + 4, highestY + 4];
        }
    }

    getPositions() {
        let pos = new Set();
        for (let i = 0; i < this.xvals.length; i++) {
            pos.add([this.xvals[i], this.yvals[i]]);
        }
        return pos;
    }

    move(v_x, v_y) {
        this.xvals = this.xvals.map(x => x + v_x);
        this.yvals = this.yvals.map(y => y + v_y);
    }

    getRightLimit() {
        return Math.max(...this.xvals);
    }

    getLeftLimit() {
        return Math.min(...this.xvals);
    }

    getType() {
        return this.type;
    }
}

let highestY = 0;
let deltaHeight = [];
let state = new Set();
// add floor to state
for (let i = 0; i < 7; i++) {
    state.add(encode([i,0]));
}

const signature = (state) => {
    let highs = [];
    for (let i = 0; i < 7; i++) {
        highs.push(Math.max(...[...state].filter(x => x[0] === i.toString()).map(y => Number(y.split('.')[1]))));
    }
    let himin = Math.min(...highs);
    highs = highs.map(x => x - himin);
    return highs.join('.');
}

let seen_signatures = new Set();

const dropRocks = (noOfRocks) => {
    let rocks = [0, 1, 2, 3, 4];
    let jets = puzzleData[0].split('').map(x => {
        if (x === '<') {
            return -1;
        }
        if (x === '>') {
            return 1;
        }
    });

    let count = 0;
    let rockIndex = 0;
    let rock = new Rock(rocks[rockIndex], 2, highestY);

    while (count < noOfRocks) {

        for (const jet in jets) {
            rock.move(jets[jet], 0);
            if (rock.getLeftLimit() < 0 || rock.getRightLimit() > 6 || [...rock.getPositions()].map(encode).some(x => state.has(x))) {
                rock.move(-jets[jet], 0);
            }
            rock.move(0, -1);
            if ([...rock.getPositions()].map(encode).some(x => state.has(x))) {
                rock.move(0, 1);
                [...rock.getPositions()].map(encode).forEach(x => state.add(x));
                
                highestY = Math.max(...[...state].map(getY));
                
                let sig = signature(state) + '.' + JSON.stringify(count % 5) + '.' + JSON.stringify(jet);

                if (seen_signatures.has(sig)) {
                    //console.log(sig);
                } else {
                    seen_signatures.add(sig);
                }

                

                count++;

                if (sig === '19.19.21.15.15.14.0.4."6552"') {
                    console.log(count, highestY);
                }

                if (count === 1105 + 495) {
                    console.log(highestY);
                }

                rockIndex++
                rock = new Rock(rocks[rockIndex % 5], 2, highestY);
                if (count >= noOfRocks) {
                    break;
                }
            }
        }

    }
}    
    
    



const drawState = () => {
    for (let y = highestY; y >= 0; y--) {
        let line = '';
        for (let x = 0; x < 7; x++) {
            if (state.has(encode([x,y]))) {
                line += '#';
            } else {
                line += '.';
            }
        }
        console.log(line);
    }
}

dropRocks(4000);


/*
    (1105, 1710), (1105 + k*1725, 1710 + k*2728)

    1105 + k*1725 <= 1000000000000 => k <= 579710144

    1000000000000 = 1105 + 579710144 * 1725 + 495

    count = 1105 + 495 => highestY = 2487

    guess = 1710 + 579710144 * 2728 + (2487 - 1710) = 1581449275319

*/
