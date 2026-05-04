const readline = require('node:readline')

readInput()


function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let params
  let N, L;
  let dayCounts = [];
  let holidays = [];

  rl.on('line', function (line) {
    if (!N || !L) {
        [N, L] = line.split(' ').map(Number);       
    } else if (dayCounts.length === 0) {
        dayCounts.push(...line.split(' ').map(Number));
    } else {
        holidays.push(line.split(' ').map(Number))
    }
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem({ N, L, dayCounts, holidays})
    process.exit()
  })
}

function solveProblem({N, L, dayCounts, holidays}) {
    // console.log({ N, L, dayCounts, holidays})
    let result = 'TIDAK';
    for (let i = 1; i <= holidays.length - 1; i++) {
        const index = i - 1;
        const [firstD, firstM] = holidays[index];
        const [follD, follM] = holidays[index + 1];

        // same month case
        if (firstM === follM) {
            if (follD - firstD === 2) {
                result  = 'YA'
                break;
            }
        } else {
            const firstDayCount = dayCounts[firstM - 1];
            if (
                firstD === firstDayCount && follD === 2 ||
                follD === 1 && firstD === firstDayCount - 1
            ) {
                result = 'YA'
                break;
            }
        }
    }
    console.log(result);
}