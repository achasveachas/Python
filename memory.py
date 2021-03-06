import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
tup_comp = sys.getsizeof(tuple(x * 10 for x in range(1000)))
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Tuple Comprehension: {tup_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

