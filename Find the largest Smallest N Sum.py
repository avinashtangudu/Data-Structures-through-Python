
'''
Author: Tangudu Avinash
Posted: Github
Topic: Data Structures through Python

'''

import heapq

def N_largest(seq, N):
    ''' find the N largest items in a sequence '''
    return heapq.nlargest(N,seq)

def N_smallest(seq, N):
    ''' find the N smallest items in a sequence '''
    return heapq.nsmallest(N, seq)

def N_heap(seq):
    ''' find the smallest items in a sequence using heapify first'''
    ''' heap[0] is always the smallest item '''
    ''' pops the smallest item, O(logN) '''
    heapq.heapify(seq)
    return heapq.heappop(seq)

def N_smallest_seq(seq):
    '''  if it is only one item, min() is faster '''
    return min(seq)

def N_smallest_sorted(seq, N):
    '''  N ~ len(seq), better sort instead'''
    return sorted(seq)[:N]

def N_largest_sorted(seq, N):
    '''  N ~ len(seq), better sort instead'''
    return sorted(seq)[len(seq)-N:]


def N_find_largest(module_name='this module'):
    seq = [1, 3, 2, 8, 6, 10, 9]
    N = 3
    assert(N_largest(seq, N) == [10, 9, 8])
    assert(N_largest_sorted(seq, N) == [8, 9, 10])
    assert(N_smallest(seq, N) == [1,2,3])
    assert(N_smallest_sorted(seq, N) == [1,2,3])
    assert(N_smallest_seq(seq) == 1)
    assert(N_heap(seq) == 1)

    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    N_find_largest()

