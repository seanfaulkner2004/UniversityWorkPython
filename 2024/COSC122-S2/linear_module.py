""" Linear/sequential searching """
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name


def linear_result_finder(tested_list, quarantined):
    """ The tested list contains (nhi, Name, result) tuples
        and isn't guaranteed to be in any order
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the  quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
    """
    total_comparisons = 0
    results = []
    for name in quarantined:
        found = False
        i = 0
        while i < len(tested_list) and not found:
            total_comparisons+=1
            nhi, search_name, result = tested_list[i]
            if search_name == name:
                results.append((name, nhi, result))
                found = True
            else:
                i+=1 
        if not found:
            results.append((name, None, None))
    return results, total_comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # write your own simple tests here
    # eg
    tested = [(1, Name('Lee'), True), (2, Name('EE'), False)]
    quarantined = [Name('Bob'), Name('Lee')]
    print(linear_result_finder(tested, quarantined))
    
