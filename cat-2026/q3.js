const readline = require('node:readline')

readInput()


function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let params

  rl.on('line', function (line) {
    // if (!N)
    //     N = Number(line);
    // else if (!S)
    //     S = line;
    // else if (!T)
    //     T = line;
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem(params)
    process.exit()
  })
}

function solveProblem(params) {
    let result = null;
    console.log(result);
}