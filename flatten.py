
# Time-stamp: <2016-10-17 20:39:55 daniel>   -*- mode: python; -*-

#
# flatten.py: Defines a recursive function to flatten
# an array of arbitraritly nested arrays.
#

#
# Written by Daniel Mendyke [archadious@gmail.com]
#


# Flatten an array of nested arrays of INT
# Example:
#   flab = [ 1, [ 2, [ 3, 4 ], [ 5, 6, [ 7 ] ] ] ]
#   flate = FlattenIntVector( flab )
#------------------------------------------------------------------------------
class FlattenedIntVector( list ) :

  ## Class constructor
  ## Parameter: the integer vector - defaults to empty list
  def __init__( self, vector = [] ) :
    super().__init__( self._main( vector ) )

  ## Performs actual flattening of the array
  ## Note! Uses recursion
  def _main( self, vector ) :
    result = []
    if type( vector ) is int : result.extend( [ vector ] )
    else :
      for element in vector :
        result.extend( self._main( element ) )
    return result
