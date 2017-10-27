
'''

Author: Tangudu Avinash
Posted: Github
Topic: Data Structures through Python

'''

class Stack(object):
    def __init__(self):
        self.content = []

    def push(self, value):
        self.content.append(value)

    def pop(self):
        if self.content:
            return self.content.pop()
        else:
            return 'Empty List...! '

    def size(self):
        return len(self.content)

    def isEmpty(self):
        return not bool(self.content)

    def peek(self):
        if self.content:
            return self.content[-1]
        else:
            print('Stack is Empty.')



if __name__ == '__main__':
    q = Stack()

    for i in range(18):
        q.push(i)
    for i in range(19):
        print q.pop()