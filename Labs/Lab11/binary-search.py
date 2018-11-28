# CS 5001
# Lab 11: Binary Search
# Evan Douglass

## Signature
# b_search_iterative :: (Object, Object[]) => Boolean
def b_search_iterative(item, array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (end+start) // 2
        if array[mid] == item:
            return True
        elif array[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return False

## Signature
# b_search_recursive :: (Object, Object[]) => Boolean
def b_search_recursive(item, array):
    mid = len(array) // 2
    if len(array) == 0:
        return False
    elif item == array[mid]:
        return True
    elif item < array[mid]:
        return b_search_recursive(item, array[:mid])
    else:
        return b_search_recursive(item, array[mid+1:])

## Signature
# find_lowest :: Object[] => Object
def find_lowest_recursive(arr:list):
    # Array is sorted but shifted.
    # It increases until a sudden decrease

    end = len(arr) - 1
    mid = len(arr) // 2

    # base cases
    if len(arr) == 0:
        return None
    elif arr[0] < arr[end]:
        return arr[0]
    elif len(arr) == 1:
        return arr[0]

    # Recursive
    elif arr[0] < arr[mid]:
        return find_lowest_recursive(arr[mid+1:])
    elif arr[0] > arr[mid]:
        return find_lowest_recursive(arr[1:mid+1])

## Signature
# find_lowest_iterative :: Object[] => Object
def find_lowest_iterative(arr:object):
    start = 0
    end = len(arr) - 1

    # Edge cases
    if len(arr) == 0:
        return None
    elif arr[start] < arr[end]:
        return arr[start]
    
    # Main loop
    while start <= end:
        mid = (start+end) // 2
        if arr[start] < arr[mid]:
            start = mid
        elif arr[start] > arr[mid]:
            end = mid
        else:
            start += 1

    return arr[mid]



##### Tests #####
def test_binary_exists_iterative():
  assert(b_search_iterative(1, [1]) == True)
  assert(b_search_iterative(1, [1, 2]) == True)
  assert(b_search_iterative(2, [1, 2]) == True)
  assert(b_search_iterative('a', ['a']) == True)

  lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
  assert(b_search_iterative('a', lst) == True)
  assert(b_search_iterative('b', lst) == True)
  assert(b_search_iterative('c', lst) == True)
  assert(b_search_iterative('d', lst) == True)
  assert(b_search_iterative('e', lst) == True)
  assert(b_search_iterative('f', lst) == True)
  assert(b_search_iterative('g', lst) == True)
  assert(b_search_iterative('h', lst) == True)
  assert(b_search_iterative('i', lst) == True)

def test_binary_no_exist_iterative():
  assert(b_search_iterative(-1, [1]) == False)
  assert(b_search_iterative(3, [1, 2]) == False)
  assert(b_search_iterative(-1, [1, 2]) == False)
  assert(b_search_iterative('b', ['a']) == False)

  lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
  assert(b_search_iterative('j', lst) == False)
  assert(b_search_iterative('', lst) == False)
  assert(b_search_iterative('klm', lst) == False)
  assert(b_search_iterative('n', lst) == False)
  assert(b_search_iterative(1, []) == False)


def test_binary_exists_recursive():
  assert(b_search_recursive(1, [1]) == True)
  assert(b_search_recursive(1, [1, 2]) == True)
  assert(b_search_recursive(2, [1, 2]) == True)
  assert(b_search_recursive('a', ['a']) == True)

  lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
  assert(b_search_recursive('a', lst) == True)
  assert(b_search_recursive('b', lst) == True)
  assert(b_search_recursive('c', lst) == True)
  assert(b_search_recursive('d', lst) == True)
  assert(b_search_recursive('e', lst) == True)
  assert(b_search_recursive('f', lst) == True)
  assert(b_search_recursive('g', lst) == True)
  assert(b_search_recursive('h', lst) == True)
  assert(b_search_recursive('i', lst) == True)

def test_binary_no_exist_recursive():
  assert(b_search_recursive(-1, [1]) == False)
  assert(b_search_recursive(3, [1, 2]) == False)
  assert(b_search_recursive(-1, [1, 2]) == False)
  assert(b_search_recursive('b', ['a']) == False)

  lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
  assert(b_search_recursive('j', lst) == False)
  assert(b_search_recursive('', lst) == False)
  assert(b_search_recursive('klm', lst) == False)
  assert(b_search_recursive('n', lst) == False)
  assert(b_search_recursive(1, []) == False)

def test_find_lowest_iterative():
    assert find_lowest_iterative([18, 25, 38, 1, 12, 13]) == 1
    assert find_lowest_iterative([25, 38, 40, 12, 13]) == 12
    assert find_lowest_iterative([12, 13, 25, 38]) == 12
    assert find_lowest_iterative([1]) == 1
    assert find_lowest_iterative([2, 1]) == 1
    assert find_lowest_iterative([]) == None

def test_find_lowest_recursive():
    assert find_lowest_recursive([18, 25, 38, 1, 12, 13]) == 1
    assert find_lowest_recursive([25, 38, 40, 12, 13]) == 12
    assert find_lowest_recursive([12, 13, 25, 38]) == 12
    assert find_lowest_recursive([1]) == 1
    assert find_lowest_recursive([2, 1]) == 1
    assert find_lowest_recursive([]) == None