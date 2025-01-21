
const iterator = function (nestedArr) {
    this.arr = nestedArr
}

iterator.prototype.print = function(){
    console.log(this.arr)
}

const itr = new iterator([1, 3, 4, 5])
itr.print()