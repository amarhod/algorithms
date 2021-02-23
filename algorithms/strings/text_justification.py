"""
Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""


def text_justification(words, max_width):
    '''
    :type words: list
    :type max_width: int
    :rtype: list
    '''
    branch_coverage = {i: False for i in range(0,18)}
    ret = []  # return value
    row_len = 0  # current length of strs in a row
    row_words = []  # current words in a row
    index = 0  # the index of current word in words
    is_first_word = True  # is current word the first in a row
    branch_coverage[0] = True
    while index < len(words):
        branch_coverage[1] = True
        while row_len <= max_width and index < len(words):
            branch_coverage[2] = True
            if len(words[index]) > max_width:
                branch_coverage[3] = True
                print("\nFunction call")
                for key in branch_coverage:
                    if branch_coverage[key] is False:
                        print(f"Branch point {key} not cover")
                print('\n\n')
                raise ValueError("there exists word whose length is larger than max_width")
            tmp = row_len
            row_words.append(words[index])
            tmp += len(words[index])
            if not is_first_word:
                branch_coverage[4] = True
                tmp += 1  # except for the first word, each word should have at least a ' ' before it.
            if tmp > max_width:
                branch_coverage[5] = True
                row_words.pop()
                break
            row_len = tmp
            index += 1
            is_first_word = False
            branch_coverage[6] = True
        # here we have already got a row of str , then we should supplement enough ' ' to make sure the length is max_width.
        row = ""
        branch_coverage[7] = True
        # if the row is the last
        if index == len(words):
            for word in row_words:
                branch_coverage[8] = True
                row += (word + ' ')
            branch_coverage[9] = True
            row = row[:-1]
            row += ' ' * (max_width - len(row))
        # not the last row and more than one word
        elif len(row_words) != 1:
            branch_coverage[10] = True
            space_num = max_width - row_len
            space_num_of_each_interval = space_num // (len(row_words) - 1)
            space_num_rest = space_num - space_num_of_each_interval * (len(row_words) - 1)
            for j in range(len(row_words)):
                branch_coverage[11] = True
                row += row_words[j]
                if j != len(row_words) - 1:
                    branch_coverage[12] = True
                    row += ' ' * (1 + space_num_of_each_interval)
                branch_coverage[13] = True
                if space_num_rest > 0:
                    branch_coverage[14] = True
                    row += ' '
                    space_num_rest -= 1
            branch_coverage[15] = True
        # row with only one word
        else:
            branch_coverage[16] = True
            row += row_words[0]
            row += ' ' * (max_width - len(row))
        branch_coverage[17] = True
        ret.append(row)
        # after a row , reset those value
        row_len = 0
        row_words = []
        is_first_word = True
    print("\nFunction call")
    for key in branch_coverage:
        if branch_coverage[key] is False:
            print(f"Branch point {key} not cover")
    print('\n\n')
    return ret
