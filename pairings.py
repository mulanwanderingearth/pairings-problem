def find_pairs(num_string):
  # Write your solution here!
  #convert the string to a list of number
  #initiate an empty set
  #loop through the list of number , the outer loop will loop from index 0 to the last but one element
  #nested loop will iterate through the index 1 to the last element
  # we will add those two numbers to a tuple and sort it and add it to an emtpy set
  #when the loop is done, return this set

  nums= num_string.split()
  result = set()
  for i in range(len(nums)-1): 
    for j in range(i+1,len(nums)):
      ordered = sorted((int(nums[i]),int(nums[j])))
      result.add(tuple(ordered))
  return result
# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")