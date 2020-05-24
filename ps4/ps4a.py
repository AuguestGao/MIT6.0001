# Problem Set 4A
# Name: AG
# Collaborators:n/a
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #pass #delete this line and replace with your code here
    new_list=[]
    if len(sequence)==1:
        new_list.append(sequence)
        return new_list 
    else:
        smaller_problem_result=get_permutations(sequence[1:])
        for case in smaller_problem_result:
            for idx in range(0,len(case)+1):
                lst_case=list(case)
                lst_case.insert(idx, sequence[0])
                new_list.append(''.join(lst_case))
        return new_list
            

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('New example:', get_permutations('aeiou'))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #pass #delete this line and replace with your code here
    
