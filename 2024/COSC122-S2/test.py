def word_counter(input_str):
    '''Return a dictionary mapping from the words in the given input_str 
       to their occurrence counts.'''
    word_list = input_str.lower().split()
    word_counts = dict()
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

word_count_dict = word_counter("THIS is a sentence this is")
print(word_count_dict)