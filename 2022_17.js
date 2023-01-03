const fs = require('fs');


const openFile = (filename) => {
    let data = fs.readFileSync(filename, {encoding: 'utf-8'});

    return data.split('\r\n');
}

const puzzleData = openFile('2022_17_small.txt');

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
}

let highestY = 0;
let state = new Set();
// add floor to state
for (let i = 0; i < 7; i++) {
    state.add(encode([i,0]));
}

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
   
    for (let i = 0; i < noOfRocks; i++) {
        let rock = new Rock(rocks[i % 5], 2, highestY);
        let landed = 0;
        for (const push of jets) {
            if (landed < 2) {
                rock.move(push, 0);
                if (rock.getLeftLimit() < 0 || rock.getRightLimit() > 6 || [...rock.getPositions()].map(encode).some(x => state.has(x))) {
                    rock.move(-push, 0);
                }    
            }
            
            rock.move(0, -1);
            if ([...rock.getPositions()].map(encode).some(x => state.has(x))) {
                rock.move(0, 1);
                landed++;
            }
        }
        [...rock.getPositions()].map(encode).forEach(x => state.add(x));
        highestY = Math.max(...[...state].map(getY));
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

dropRocks(3);

drawState();

console.log(highestY);