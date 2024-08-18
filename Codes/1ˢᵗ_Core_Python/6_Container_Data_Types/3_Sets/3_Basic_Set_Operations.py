# Basic Set Operations

# Like lists Sets are mutable too. Their contents can be changed.

s = {'gate', 'fate', 'late'}
s.add('rate') # adds one more element to set s

# If we want an immutable set, we should use a frozenset.

s = frozenset({'gate', 'fate', 'late'})
s.add('rate') # error


# Concatenation - doesn't work
# Merging - doesn't work

# While converting a set using set( ), repetitions are eliminated.
lst = [10, 20, 10, 30, 40, 50, 30]
s = set(lst) # will create set containing 10, 20, 30, 40, 50