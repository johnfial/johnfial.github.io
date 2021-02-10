# Book:
    # p98 describe how you could use a single array to implement three stacks!
    # hints 2, 12, 38, 58
    # hint: divide them well... can we make three lists in a list?

# Functions I need for the stack:
    # pop() remove the top (last, most recent) item
    # push(item) add an item to the top
    # peek() return the top of the stack
    # isEmpty() returns true only if the stack is empty

# Functions I need for the queue:
    # add(item) add to the stack
    # remove() remove the FIRST item in the stack
    # peek() returns the top (last) item
    # isEmpty() returns true only if the queue is empty...

# https://www.w3schools.com/python/python_ref_list.asp
class MyFirstStack():    
    # array1 = []
    # array2 = []
    # array3 = []
    # main_array = [array1, array2, array3]
    main_array = []
    def __init__(self, k:int):
        print(f'created new stack')
        self.main_array.append(k)
        return

    def pop(self):
        print(f'pop(self)')
        self.main_array.pop(len(self.main_array))
        return 

    def push(self, k):
        self.main_array.append(k)
        return

    def peek(self):
        return self.main_array[-1]

    def isEmpty(self):
        if len(self.main_array) == 0:
            return True

    def return_zero(self):
        print(f'return_zero(self)')
        return 0

    def sort_into_three(self):
        pass

    def __len__(self):
        print('len() function')
        return len(self.main_array)

new_stack = MyFirstStack(55)
new_stack.push(3)
new_stack.push(8)
print(new_stack.main_array)
# print(new_stack.len())
print(new_stack.main_array)
new_stack.push(27)
print(new_stack.main_array)
print(new_stack.peek)
