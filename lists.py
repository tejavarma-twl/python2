sample_list         = [1,2,3,4,5]
sample_tuple        = (1,2,3,4,5)
sample_set          = {1,2,3,4,5}
sample_set2         = {1,2,4,6,7}
sample_dictionary   = {'soups':'soup info','starters':'Starter info'}

# print(sample_set | sample_set2)
# print(sample_set & sample_set2)
# print(sample_set - sample_set2)
# print(sample_set ^ sample_set2)
print(sample_set.union(sample_set2))
print(sample_set.intersection(sample_set2))
print(sample_set.difference(sample_set2))
print(sample_set.symmetric_difference(sample_set2))
print(sample_set2.symmetric_difference_update(sample_set))
print(sample_set)
print(sample_set2)

# print(type(sample_list))
# print(sample_list)
# print(type(sample_tuple))
# print(sample_tuple)
# print(type(sample_set))
# print(sample_set)
# print(type(sample_dictionary))
# print(sample_dictionary)

# i = 0
# while i<2:
#     print("ok")
#     i += 1
#     if(i==1):
#         break
# else:
#     print("Not ok")