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
let tick = 0;
let numberOfRestingRocks = 0;
let state = new Set();
// add floor to state
for (let i = 0; i < 7; i++) {
    state.add(encode([i,0]));
}

while (numberOfRestingRocks < 2022) {
    let jet = 0;
    let rock = new Rock (tick % 5, 2, highestY);
    if (tick % 2 === 0) {
        let direction = puzzleData[jet % puzzleData.length];
        if (direction === '<' && rock.getLeftLimit() > 0) {
            rock.move(-1, 0);
        }
        if (direction === '>' && rock.getRightLimit() < 6) {
            rock.move(1, 0);
        }
        jet++;
    } else {
        let newPos = new Set();
        let oldPos = rock.getPositions();
        oldPos.forEach(pos => newPos.add([pos[0], pos[1] - 1]));
        let conflict = false;
        newPos.forEach((pos) => {
            if (state.has(encode(pos))) {
                conflict = true;
            }
        });
        if (!conflict) {
            rock.move(0, -1);
        } else {
            rock.land();
            rock.getPositions().forEach(pos => state.add(encode(pos)));
            numberOfRestingRocks++;
            highestY = Math.max(...state.map(pos => pos.split('.').map(t => Number(t))[1]));
        }
    }
    tick++;
}
