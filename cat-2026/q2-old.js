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
    // console.log({ N, T, durations, waits})
    function recurse(remainingTime, lastPlayedGameI, gameCount) {
        // end
        if (remainingTime <= 0) {
            return gameCount;
        }
        // start
        if (lastPlayedGameI === null) {
            let options = [];
            for (let i = 0; i < N; i++) {
                const timeAfterDuration = remainingTime - durations[i];
                if (timeAfterDuration >= 0) {
                    options.push(recurse(timeAfterDuration, i, gameCount + 1))
                }
            }
            if (options.length === 0) return 0;
            // console.log({ options })
            const max = Math.max(...options);
            return max;
        }

        const lastPlayedGameDuration = durations[lastPlayedGameI];
        const lastPlayedGameWait = waits[lastPlayedGameI];
        // if we choose to wait and then play current game
        let firstOption = gameCount;
        // console.log({ lastPlayedGameI, firstOption, remainingTime, gameCount })
        if (remainingTime - lastPlayedGameWait - lastPlayedGameDuration >= 0) {
            firstOption = recurse(remainingTime - lastPlayedGameWait - lastPlayedGameDuration, lastPlayedGameI, gameCount + 1);
        }
        // else we choose to play other games
        let options = [];
        for (let i = 0; i < N; i++) {
            if (i === lastPlayedGameI) continue;
            const timeAfterDuration = remainingTime - durations[i];
            if (timeAfterDuration >= 0) {
                // console.log({ timeAfterDuration })
                options.push(recurse(remainingTime - durations[i], i, gameCount + 1))
            }
        }
        // console.log({ firstOption, options })
        const maxCountFromOptions = Math.max(...options);
        // console.log({firstOption, options})
        if (firstOption >= maxCountFromOptions) {
            return firstOption;
        } else {
            return maxCountFromOptions;
        }
    }
    result = recurse(T, null, 0);

    console.log(result);
}