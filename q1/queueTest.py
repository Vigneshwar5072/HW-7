import pytest
from queueMain import *


def test_happyPath():
    obj = Queue()
    assert(obj.enqueue(5)==5, "Returned value is not None but it should have some valid entries")
    assert(obj.enqueue(7)==7, "Returned value is not None but it should have some valid entries")
    assert obj.size() == 2, "Returned value should be 2  else wrong comparsion "
    assert(print(obj.dequeue()) == 5, "Returned value should be 5 not None but it should have some valid entries")
    assert obj.size() == 1, "Returned value is 1 not None but it should have some valid entries"



def test_edgecases():
    list=Queue()
    
    def edgeOne():
        list=Queue()
        try:
            list.dequeue()
        except IndexError as indexerror:
            return None
        
    def edgeTwo():
        list=Queue()
        try:
            list.enqueue(myname)
        except NameError as unknownstring:
            return None
        
    assert edgeOne()==None, "Unable to pop out the elements from the queue, as the queue is empty "
    assert edgeTwo()==None, "Unable to enqueue the undefined datatype"
    obj = Queue()
    assert print(obj.dequeue()) == None, "Returned value should be None"
    assert obj.size() == 0, "Returned value should be 0 else wrong comparsion "

    
test_happyPath()
test_edgecases()    
    