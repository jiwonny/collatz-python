# Collatz

	
### collatz_eval(i, j)
i the beginning of the range, inclusive
j the end       of the range, inclusive
if i is bigger than j, swap them to make the for loop run normally.
 
max_val is initialized to zero. max_val is the max cycle length in the range
using the global array 'memory'.
 
iterator is the value being checked.
if iterator has been calculated before, the element in the memory array with the index of iterator won't be zero.
if iterator has not been calculated before, keep computing.
after computing, check the memory array if the computed value has been calculated for the cycle length before.
 
compare the current maximum value with cycle length of the iterator.
 
return the current maximum value after computing all the values in the range through for loop.

<br>

### collatz_print(w, i, j, v)
print three ints
w a writer
i the beginning of the range, inclusive
j the end       of the range, inclusive
v the max cycle length

<br>

### collatz_read(s)
read two ints
s a string
return a list of two ints, representing the beginning and end of a range, [i, j]

<br>
### collatz_solve(r, w)
r a reader
w a writer
