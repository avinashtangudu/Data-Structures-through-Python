
'''

Author: Tangudu Avinash
Posted: Github
Topic: Data Structures through Python

'''


def Bubble_Sort(Seq):
    """
    Implementation of bubble sort.
    O(n2) and thus highly ineffective.
    """
   Size = len(Seq) -1
    for num in range(size, 0, -1):
        for i in range(num):
            if Seq[i] > Seq[i+1]:
                Temp = Seq[i]
                Seq[i] = Seq[i+1]
                Seq[i+1] = Temp
    return Seq


def Bubble_Sort_Test(Module_Name='Current Module'):
    Seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(Bubble_Sort(Seq) == Sorted(Seq))


if __name__ == '__main__':
    Bubble_Sort_Test()

