# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    out = []
    if len(sequence) <= 1:
        return sequence   
    for i in range(len(sequence)):
        first = sequence[i]
        for perm in get_permutations(sequence[:i] + sequence[i+1:]):
            out += [first + perm]
    return out
    




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations("abc"))

