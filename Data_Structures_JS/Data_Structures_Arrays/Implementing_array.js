// implementation array using class

class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }
  get(index) {
    return this.data[index];
  }
}

const array = new MyArray();

console.log(array.get[0]);
