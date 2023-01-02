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
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    getCoordinates() {
        return [this.x, this.y];
    }

    move(v_x, v_y) {
        this.x += v_x;
        this.y += v_y;
    }
}
class Rock {
    constructor(type, topLeftX, topLeftY) {
        this.resting = false;
        // Type: ####
        if (type === 0) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 3];
            this.yvals = [topLeftY, topLeftY, topLeftY, topLeftY];
        }
        // Type: .#.
        //       ###
        //       .#.
        if (type === 1) {
            this.xvals = [topLeftX + 1, topLeftX, topLeftX + 1, topLeftX + 2, topLeftX + 1];
            this.yvals = [topLeftY, topLeftY - 1, topLeftY - 1, topLeftY - 1, topLeftY - 2];
        }
        // Type: ..#
        //       ..#
        //       ###
        if (type === 2) {
            this.xvals = [topLeftX + 2, topLeftX + 2, topLeftX, topLeftX + 1, topLeftX + 2];
            this.yvals = [topLeftY, topLeftY - 1, topLeftY - 2, topLeftY - 2, topLeftY - 2];
        }
        // Type: #
        //       #
        //       #
        //       #
        if (type === 3) {
            this.xvals = [topLeftX, topLeftX, topLeftX, topLeftX];
            this.yvals = [topLeftY, topLeftY - 1, topLeftY - 2, topLeftY - 3];
        }
        // Type: ##
        //       ##
        if (type === 4) {
            this.xvals = [topLeftX, topLeftX + 1, topLeftX, topLeftX + 1];
            this.yvals = [topLeftY, topLeftY, topLeftY - 1, topLeftY - 1];
        }
    }

    getPositions() {

    }
}