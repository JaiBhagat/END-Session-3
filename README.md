# Assignment Session 3 

This assignment we are taught about the map,filter,zip ,list comprehensions, reduce functionality and partial functions , operator module.

## map()

A map function is a higher order function which take a function and an iterator . It iterates the function over the iterator.

```python
map(func, *iterators)
```

map is lazy operator that is when you initialize a map it will not give direct answer to function but will make a map object only when called it will iterate over and give results. it is also exhaustive i.e. once the iterator is iterated over the map function ends. 



## filter()

A map function is a higher order function which take a function and an iterator. It iterates the function over the iterator and returns Truthy value.

```python
filter(func, iterator)
```

Only one single iterator is accepted. If function is None  , it simply returns the elements of Iterable that are truthy.

  

## zip()

zip is not a higher order function but it zips the elements of multiple iterables .

```
zip(*iterables)
```

```
zip([1,2,3],[5,6,7])

gives

(1,5),(2,6),(3,7)
```



## list comprehensions

list comprehension are one liner codes that returns a list.

for writing compact code we can instead of writing a whole function can replace with list comprehensions. 

list comprehension can be used to replace map functions as they are more understandable.



## lambda function

lambda function is used to write one liner function. Usually passed as a function where the input has to change in ever iteration .

```
lambda x:x+1
```

here x is passed as an input which is written in the left hand side of the : and right hand side we write the function which is to be performed.



## reduce function 

function like max(), min(), avg() are reduce functions. Reduce functions are the once which iterate a function over the input which is given. Like it iterator over a iterator and given the addition of the element within that iterator.

python has it own reduce function in the functools module . However we can also define our own reduce function :

```
def _reduce(fn,l):
	result = l[0]
	for x in l[1:]:
		result = fn(result,x)
	return result
```

Although our reduce function is index dependent the python provide reduce is not and can work for set and dictionaries



## Partial Function

To reduce the total number of required arguments when calling a fucntion. In the below example partial function such that 1000/9999 are hardcoded.

veh_number = partial(numberplate_v1,r1=1000,r2=9999)

## Test Cases

[![test.png](https://i.postimg.cc/zG38xmC8/test.png)](https://postimg.cc/v4RJmN2N)
