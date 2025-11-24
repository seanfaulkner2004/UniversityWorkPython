import sys
import random
import time
from stack import Stack
from queue122 import Queue
from deque import Deque


print("Using time.perf_counter for timing.")
REZ = time.get_clock_info('perf_counter').resolution
print('Smallest unit of time is ' + str(REZ) + ' seconds')


def time_stack_push(initial_size, n_trials):
    """ Finds average time for pushing onto a stack of a given initial size"""
    s = Stack()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.push(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.push(0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Stack size = {:,d} -> avg. time/push for {:,d} pushes is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_stack_pop(initial_size, n_trials):
    """ Finds average time for popping a stack of a given initial size"""
    s = Stack()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.push(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.pop()
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Stack size = {:,d} -> avg. time/pop for {:,d} pops is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_queue_enqueue(initial_size, n_trials):
    """ Finds average time for enqueuing onto a queue of a given initial size"""
    s = Queue()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.enqueue(0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Queue size = {:,d} -> avg. time/enqueue for {:,d} enqueues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_queue_dequeue(initial_size, n_trials):
    """ Finds average time for dequeuing onto a queue of a given initial size"""
    s = Queue()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.dequeue()
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Queue size = {:,d} -> avg. time/dequeue for {:,d} dequeues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_deque_enqueue_front(initial_size, n_trials):
    """ Finds average time for enqueuing onto the front of a deque of a given initial size"""
    s = Deque()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue_rear(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.enqueue_front(0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Deque size = {:,d} -> avg. time/enqueue_front for {:,d} enqueues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_deque_enqueue_rear(initial_size, n_trials):
    """ Finds average time for enqueuing onto the back of a deque of a given initial size"""
    s = Deque()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue_rear(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.enqueue_rear(0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Deque size = {:,d} -> avg. time/enqueue_rear for {:,d} enqueues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_deque_dequeue_front(initial_size, n_trials):
    """ Finds average time for dequeuing onto the front of a deque of a given initial size"""
    s = Deque()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue_rear(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.dequeue_front()
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Deque size = {:,d} -> avg. time/dequeue_front for {:,d} dequeues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))

def time_deque_dequeue_rear(initial_size, n_trials):
    """ Finds average time for dequeuing onto the back of a deque of a given initial size"""
    s = Deque()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.enqueue_rear(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.dequeue_rear()
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Deque size = {:,d} -> avg. time/dequeue_rear for {:,d} dequeues is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))


def run_tests():
    """ Runs as many or as few tests as you call,
    initially just runs the test for stack pushes
    """
    print('\n' *3)
    initial_size = 10000000  # start with this many items in data structure
    n_trials = 100  # run this many trials and take the average time
    
    time_deque_enqueue_front(initial_size, n_trials)
    time_deque_enqueue_rear(initial_size, n_trials)
    time_deque_dequeue_front(initial_size, n_trials)
    time_deque_dequeue_rear(initial_size, n_trials)
    # call your shiny new test functions here


run_tests()
