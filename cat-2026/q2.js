const readline = require('node:readline')

readInput()


function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let params
  let N, T;
  let durations = [];
  let waits = [];

  rl.on('line', function (line) {
    if (!N || !T) {
        [N, T] = line.split(' ').map(Number);
    } else {
        const [duration, wait] = line.split(' ').map(Number);
        durations.push(duration)
        waits.push(wait)
    }
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem({ N, T, durations, waits})
    process.exit()
  })
}

function solveProblem({ N, T, durations, waits}) {
    let result = null;
    console.log({ N, T, durations, waits})
    function play(timeLeft, gameCount) {
      if (timeLeft === 0) {
        return gameCount
      }
    }
    

    console.log(result);
}