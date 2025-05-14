// // // ACCESS O(1) PUSH O(1) INSERT O(n) DELETE O(n)

// const strings = ["a", "b", "c", "d"];
// strings.push("e"); // O(1)
// strings.pop("e"); // O(1)
// strings.unshift("x"); // O(n)
// strings.splice(2, 0, "mid in 2"); // O(n/2) ==> O(n)

// // // ====== interview question: =======
// // // 1. Reverse A String
// const reverse = (str) => {
//   if (!str || str.length == 1) {
//     return str;
//   }
//   const reversedArr = [];
//   for (let i = str.length - 1; i >= 0; i--) reversedArr.push(str[i]);

//   return reversedArr.join("");
// };
// console.log(reverse("123"));

// // // 2. Reverse A String using js methods
// const reverse2 = (str) => {
//   // return str.split("").reverse().join("");
//   return [...str].reverse().join("");
// };
// console.log(reverse2("456"));

// // // 3. merge 2 array
// const merge = (arr1, arr2) => {
//   return [...arr1, ...arr2];
// };
// console.log(merge([1, 2, 3], [4, 5, 6]));

// // 4. merge sorted array
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
