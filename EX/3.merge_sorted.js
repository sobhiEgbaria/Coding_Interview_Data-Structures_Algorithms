const mergeSorted = (arr1, arr2) => {
  let mergeSortedArr = [];
  let arr1counter = 0;
  let arr2counter = 0;

  if (arr1.length == 0) {
    return arr2;
  } else if (arr2.length == 0) {
    return arr1;
  }

  while (arr1.length > arr1counter || arr2.length > arr2counter) {
    if (arr1[arr1counter] < arr2[arr2counter]) {
      mergeSortedArr.push(arr1[arr1counter]);
      arr1counter++;
    } else {
      mergeSortedArr.push(arr2[arr2counter]);
      arr2counter++;
    }

    if (!arr1[arr1counter]) {
      return [...mergeSortedArr, ...arr2.splice(arr2counter)];
    } else if (!arr2[arr2counter]) {
      return [...mergeSortedArr, ...arr1.splice(arr1counter)];
    }
  }

  return mergeSortedArr;
};
console.log(mergeSorted([0, 3, 4, 31], [4, 6, 30]));
