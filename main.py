"""
Given an array of string and a string as input, create an array where the occurrences of the input string have been removed.
Input-> ["Java","Master","Job","Ready","Java"], "Java"
Output-> ["Master","Job","Ready"]
"""

ls = ["Java","Master","Job","Ready","Java"]
st = "Java"
ln = len(ls)
arr = []
for i in range(0,ln):
  e = ls[i]
  if (e==st):
    pass
  else:
    arr += [e]
print(arr)
