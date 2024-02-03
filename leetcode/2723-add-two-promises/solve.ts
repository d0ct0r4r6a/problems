type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    return (await Promise.all([promise1, promise2])).reduce((prev, curr) => prev + curr, 0)
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */