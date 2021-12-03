import pytest
from remove_dups_linked_list_MainFile import *


def test_happyPath():
    first_node = Node()
    assert print(first_node.set_data(11)) == None, "Returned value should be None"
    linked_list = LinkedList(first_node)
    assert linked_list.print_list() == None, "Returned value should be None"
    assert print(linked_list.insert(3)) is None, "Returned value should be None for 3"
    assert print(linked_list.insert(6)) is None, "This is check for insert() function execution"    
    assert linked_list.size() is not None, "Returned value should not be None for size " 
    assert print(linked_list.insert(3)) is None, "Returned value should be None for 3 insertion"
    assert linked_list.size() == 4, "Returned value should not be None for size as inserted elements" 
    assert print(linked_list.remove_dups()) is None, "This is check for remove_dups() function execution"
    assert linked_list.size() == 3, "Returned value should not be None, as we have elements inserted" 
    assert linked_list.print_list() == None, "There should be None elements in the list"



def test_edgecases():
    first_node = Node()
    linked_list = LinkedList()
    
    def valueErrorPrintList():

        with pytest.raises(ValueError):
            linked_list.print_list()
    valueErrorPrintList()
    first_node = Node()
    linked_list = LinkedList(first_node)
    assert linked_list.print_list() is None, "Returned value should be None, as list contains None element "
    assert linked_list.size() is not None, "Returned value should be 0 as list has no elements"
    assert linked_list.remove_dups 
    assert linked_list.print_list() is None, "Returned value should be None, as list contains None elements to remove duplicates"
    def edgeCaseFour():
        first_node = Node()
        first_node.set_data(11)
        linked_list = LinkedList(first_node)        
        try:
            print(linked_list.insert(you))
        except NameError as unknownstring:
            return None
    def edgeCaseFive():
        first_node = Node()
        first_node.set_data(11)
        linked_list = LinkedList(first_node)        
        try:
            print(linked_list.remove_dups(6))
        except TypeError as takesOnePositionalArgument:
            return None
    def edgeCaseSix():
        first_node = Node()
        first_node.set_data(11)
        linked_list = LinkedList(first_node)        
        try:
            print(linked_list.size(9))
        except TypeError as takesNoArgument:
            return None

    assert edgeCaseFour()==None, "Unable to insert Unknown datatype, hence returned None "
    assert edgeCaseFive()==None, "Cannot pass two positional arguments to remove_dups() function "
    assert edgeCaseSix()==None, "Cannot insert any argument to the size() function "



    
test_happyPath()
test_edgecases()    
    