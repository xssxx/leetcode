// 2023.12.02

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
  const val1 = await promise1;
  const val2 = await promise2;
  // console.log(val1, val2)
  return new Promise((resolve) => setTimeout(() => resolve(val1 + val2), 1));
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
