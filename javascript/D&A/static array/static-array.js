class StaticArray {
  // Insert n into arr at the next open position.
  // Length: is the number of 'real' values in arr
  // capacity: is the size of the array.
  insertEnd(arr, n, length, capacity) {
    if (length < capacity) {
      arr[length] = n
    }
  }

  // Remove from the last position in the array
  // if the array is not empty (i.e. length is non-zero).
  removeEnd(arr, length) {
    if (length > 0) {
      arr[length - 1] = 0
      length--
    }
    return length
  }

  // Insert n into index i after shifting elements to the right.
  // Assuming i is a valid index and arr is not full.
  insertMiddle(arr, index, n, length) {
    for (let i = length - 1; i >= index; i--) {
      arr[i + 1] = arr[i]
    }
    arr[index] = n
    length++
    return length
  }

  // Remove value at index i before shifting elements to the left.
  // Assuming i is a valid index.
  removeMiddle(arr, index, length) {
    for (let i = index + 1; i < length; i++) {
      arr[i - 1] = arr[i]
    }
    length--
    return length
  }

  printArr(arr, length) {
    let s = ""
    for (let i = 0; i < length; i++) {
      s += arr[i] + " "
    }
    console.log(s)
  }
}
