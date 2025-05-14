// // ACCESS O(1) PUSH O(1) INSERT O(n) DELETE O(n)

const strings = ["a", "b", "c", "d"];
strings.push("e"); // O(1)
strings.pop("e"); // O(1)
strings.unshift("x"); // O(n)
strings.splice(2, 0, "mid in 2"); // O(n/2) ==> O(n)

// ====== interview question: =======
// // 1. Reverse A String
const reverse = (str) => {
  if (!str || str.length == 1) {
    return str;
  }
  const reversedArr = [];
  for (let i = str.length - 1; i >= 0; i--) reversedArr.push(str[i]);

  return reversedArr.join("");
};
console.log(reverse("123"));

// // 2. Reverse A String using js methods
const reverse2 = (str) => {
  // return str.split("").reverse().join("");
  return [...str].reverse().join("");
};
console.log(reverse2("456"));

// // 3. merge 2 array
const merge = (arr1, arr2) => {
  return [...arr1, ...arr2];
};
console.log(merge([1, 2, 3], [4, 5, 6]));
