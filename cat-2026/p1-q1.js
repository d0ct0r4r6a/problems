const readline = require('node:readline')

readInput()


function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let N, S, T;

  rl.on('line', function (line) {
    if (!N)
        N = Number(line);
    else if (!S)
        S = line;
    else if (!T)
        T = line;
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem({ N, S, T })
    process.exit()
  })
}

function solveProblem({ N, S, T}) {
    let result = 'YA';
    let diff = null;
    function countDiff (num1, num2) {
        if (num2 >= num1) {
            return num2 - num1
        } else {
            return (10 - num1) + num2
        }
    }
    for (let i = 0; i < N; i++) {
        const currentDiff = countDiff(Number(S[i]), Number(T[i]));
        if (diff === null) {
            diff = currentDiff
            continue;
        }
        if (currentDiff != diff) {
            result = 'TIDAK';
            break;
        }
    }
    console.log(result);
}