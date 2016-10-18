#!/usr/bin/env python3
# Time-stamp: <2016-10-17 20:47:55 daniel>   -*- mode: python; -*-

#
# flatten_test.py: Test code for the flatten array module
#

#
# Written by D Mendyke [archadious@gmail.com]
#

# Required modules
#------------------------------------------------------------------------------
from flatten import FlattenedIntVector  # the class to flatten int arrays


def run_test( ) :

  one = [ 1, 2, [ 3, [ 4, 5 ], [ 6, [ 7 ] ] ] ]
  two = [ 1, [ 2, 3, 4 ], 5, 6, [ 7 ] ]
  three = [ 1, 2, 3, 4, 5, 6, 7 ]

  print( "\nThe following three lines should be the same." )
  print( FlattenedIntVector( one ) )
  print( FlattenedIntVector( two ) )
  print( FlattenedIntVector( three ) )
  print()


# Entry into the script
#------------------------------------------------------------------------------
if __name__ == '__main__' : run_test()
