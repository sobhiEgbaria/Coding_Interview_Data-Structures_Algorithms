// implementation array using class

class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }
  get(index) {
    return this.data[index];
  }
  push(value) {
    this.data[this.length] = value;
    this.length++;
    return this.length;
  }
  pop() {
    delete this.data[this.length - 1];
    this.length--;
    return this.length;
  }
  delete(index) {
    this.shiftItems(index);
    return this.data[index];
  }

  shiftItems(index) {
    // [0, 1, 2, 3, 4, 5, 6, 7];
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }
}

const array = new MyArray();
array.push("you");
array.push("are");
array.push("!");
array.push("nice");
console.log(array);
array.delete(2);
console.log(array);
