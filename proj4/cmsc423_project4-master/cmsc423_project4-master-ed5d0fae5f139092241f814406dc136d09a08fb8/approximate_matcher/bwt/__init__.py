from preprocess_bwt import _get_first_occurence_fn, _get_count_fn
from bwt import burrows_wheeler_transform
from suffix_array import get_suffix_array

# THIS IS A STUB, YOU NEED TO IMPLEMENT THIS
#
# Construct the Burrows-Wheeler transform for given text
# also compute the suffix array
#
# Input:
#   text: a string (character `$` assumed to be last character)
#
# Output:
#   a tuple (bwt, suffix_array):
#       bwt: string containing the Burrows-Wheeler transform of text
#       suffix_array: the suffix array of text
def _construct(text):
    # done
    return burrows_wheeler_transform(text), get_suffix_array(text)

# wrapper for the processing functions used to compute
# auxiliary data structures for efficient BWT matching
# see file `preprocess_bwt.py`
def _preprocess_bwt(bwt):
    first_occurence = _get_first_occurence_fn(bwt)
    count = _get_count_fn(bwt)
    return first_occurence, count

# class encapsulating exact matching with Burrows-Wheeler transform
#
# Fields:
#   _text: string, the target string
#   _bwt: string, the burrows-wheeler transform of target string
#   _suffix_array: [int], suffix array of target string
#   first_occurence: function returning first occurence of each symbol in
#                     first column of sorted rotation table for bwt, see below
#   count: function returning number of occurences of each symbol up to
#           a given position, see below
#
# Notes:
#   After initializing: `bwt = BWT(target)`:
#
#   `bwt.first_occurence(symbol)` returns the row in which symbol occurs first
#       in the first column of the sorted rotation table corresponding to the BWT
#       of target string
#
#   `bwt.count(symbol, position)` returns the number of occurrences of symbol
#       up to given position in BWT of target string
class BWT:
    def __init__(self, target):
        self._text = target
        self._bwt, self._suffix_array = _construct(self._text)
        self.first_occurence, self.count = _preprocess_bwt(self._bwt)
        self._l2f = BWT.last_to_first(self._bwt)

    # THIS IS A STUB, YOU NEED TO IMPLEMENT THIS
    #
    # return indices for positions in target string that match
    # query exactly
    #
    # Input:
    #   pattern: string, query string
    #
    # Output:
    #   [int], array of indices of exact matches of query in target
    #          array is empty if no exact matches found
    def get_matches(self, pattern):
        top, bottom = self._get_matching_rows(pattern)

        if top == -1:
            return []

        matches = []
        for i in xrange(bottom - top + 1):
            # col = self.get_bwt_col(top + i)
            # matches.append(len(self._text) - col.find("$") + 1)
            matches.append(self._suffix_array[top + i])
        return matches

    @staticmethod
    def last_to_first(last_column):
        first_column = sorted(last_column)
        mapped_indexes = []

        for ch in last_column:
            i = first_column.index(ch)
            mapped_indexes.append(i)
            first_column[i] = "\0"

        return mapped_indexes

    # THIS IS A STUB, YOU NEED TO IMPLEMENT THIS
    #
    # return top, bottom pointers for rows of sorted rotations table
    # that start with query
    #
    # Input:
    #   pattern: string, query string
    #
    # Output:
    #   tuple (top, bottom): top and bottom pointers for consecutive rows in
    #       sorted rotations table that start with exact matches to query string
    #       returns (-1, -1) if no matches are found
    def _get_matching_rows(self, pattern):
        top = 0
        bottom = len(self._bwt) - 1

        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern[-1:]
                pattern = pattern[:-1]

                substr = self._bwt[top: bottom + 1]
                if symbol in substr:
                    top_index = substr.index(symbol) + top
                    bottom_index = len(substr) - substr[::-1].index(symbol) + top - 1
                    top = self._l2f[top_index]
                    bottom = self._l2f[bottom_index]
                else:
                    return -1, -1
            else:
                return top, bottom

