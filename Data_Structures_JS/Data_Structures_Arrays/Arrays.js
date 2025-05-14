// ACCESS O(1) PUSH O(1) INSERT O(n) DELETE O(n)

const strings = ["a", "b", "c", "d"];
strings.push("e"); // O(1)
strings.pop("e"); // O(1)

strings.unshift("x"); // O(n)
strings.splice(2, 0, "mid in 2"); // O(n/2) ==> O(n)

console.log(strings);
