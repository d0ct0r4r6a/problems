const readline = require('readline')

function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let problem = {
    T: 0,
    testCases: []
  }

  let nTower = null;

  rl.on('line', function (line) {
    // TODO: Process input
    if (problem.T === 0) {
      // Get number of test cases from first line
      problem.T = Number(line)
    } else if (nTower === null) {
      nTower = Number(line);
    } else {
      towerBlocks = line.split(' ');

      problem.testCases.push({
        nTower,
        towerBlocks,
      });
      nTower = null;
    }
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem(problem)
    process.exit()
  })
}

function solveProblem(problem) {
  problem.testCases.forEach((input, tcIndex) => {
    solveTestCase(input, tcIndex)
  })
}

function solveTestCase(input, tcIndex) {
  const { nTower, towerBlocks } = input
  let outputStatement = `Case #${tcIndex + 1}: `;
  let outcome = '';
  
  if (
  // Corner case 1 Output: Always IMPOSSIBLE
  // When the same letters appear in a word and not contiguous
    !hasContiguousWord(towerBlocks)
  // Corner case 2 Output: Always IMPOSSIBLE
  // When there are same letters but not in the edges
    // || hasSeparatedSameLetters(towerBlocks)
  ) {
    outcome = 'IMPOSSIBLE';
  } else {
    const combinations = generateCombinations(towerBlocks);
    const validCombination = combinations.find((combination) => {
      return checkContiguous(combination);
    });
    outcome = validCombination || 'IMPOSSIBLE'
  }
  console.log(outputStatement + outcome);
}

function checkContiguous(letters) {
  const appearedLetters = {};
  for (let i = 0; i <= letters.length - 1; i++) {
    if (letters[i] in appearedLetters) {
      const letterAppearanceIndices = appearedLetters[letters[i]];
      if (letterAppearanceIndices.includes(i - 1)) {
        appearedLetters[letters[i]].push(i);
        continue;
      } else {
        return false;
      }
    } else {
      appearedLetters[letters[i]] = [i]
    }
  }
  return true;
}

function hasContiguousWord(towerBlocks) {
  for (letters of towerBlocks) {
    if (!checkContiguous(letters)) {
      return false;
    }
  }
  return true;
}

// function hasSeparatedSameLetters(towerBlocks) {
//   let lettersInMiddle = [];
//   for (letters of towerBlocks) {
//     if (letters.slice(1, letters.length - 1).split('').some((letter) => lettersInMiddle.includes(letter))) {
//       return true;
//     } else {
//       lettersInMiddle.push(...letters.slice(1, letters.length - 1))
//     }
//   }
//   return false;
// }

function generateCombinations(towerBlocks) {
  if (towerBlocks.length === 1) {
    return [towerBlocks[0]];
  } else {
    let combinations = [];
    for (let i = 0; i <= towerBlocks.length - 1; i++) {
      const remainingTowerBlocks = towerBlocks.filter((tb, tbi) => tbi !== i);
      for (remainingTBCombination of generateCombinations(remainingTowerBlocks)) {
        combinations.push(towerBlocks[i] + remainingTBCombination)
      }
    }
    return combinations;
  }
}

readInput()