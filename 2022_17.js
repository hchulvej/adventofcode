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
class Rock {
    constructor(type, topLeftX, highestY) {
        this.resting = false;
        // Type: ####
        if (type === 0) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 3];
            this.yvals = [highestY + 3, highestY + 3, highestY + 3, highestY + 3];
        }
        // Type: .#.
        //       ###
        //       .#.
        if (type === 1) {
            this.xvals = [topLeftX + 1, topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 1];
            this.yvals = [highestY + 5, highestY + 4, highestY + 4, highestY + 4, highestY + 3];
        }
        // Type: ..#
        //       ..#
        //       ###
        if (type === 2) {
            this.xvals = [topLeftX + 2, topLeftX + 2, topLeftX, topLeftX + 1, topLeftX + 2];
            this.yvals = [highestY + 5, highestY + 4, highestY + 3, highestY + 3, highestY + 3];
        }
        // Type: #
        //       #
        //       #
        //       #
        if (type === 3) {
            this.xvals = [topLeftX, topLeftX, topLeftX, topLeftX];
            this.yvals = [highestY + 6, highestY + 5, highestY + 4, highestY + 3];
        }
        // Type: ##
        //       ##
        if (type === 4) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX, topLeftX + 1];
            this.yvals = [highestY + 4, highestY + 4, highestY + 3, highestY + 3];
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

    isResting() {
        return this.resting;
    }

    land() {
        this.resting = true;
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

let jet = 0;

const dropRock = (type) => {
    let rock = new Rock(type, 2, highestY);
    let falling = true;

    while (falling) {
        // Jet
        if (puzzleData[jet] = '<') {
            if (rock.getLeftLimit() > 0) {
                rock.move(-1, 0);
            }
            if ([...rock.getPositions()].map(encode).some(e => state.has(x))) {
                rock.move(1, 0);
            }
        }
        if (puzzleData[jet] = '>') {
            if (rock.getLeftLimit() < 6) {
                rock.move(1, 0);
            }
            if ([...rock.getPositions()].map(encode).some(e => state.has(x))) {
                rock.move(-1, 0);
            }
        }
        // Fall
        rock.move(0, -1);
        if ([...rock.getPositions()].map(encode).some(e => state.has(x))) {
            rock.move(0, 1);
            falling = false;
        }

    }
    [...rock.getPositions()].map(encode).forEach(e => state.add(e));
}
