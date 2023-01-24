d={2:4,1:2,5:5}
print('original directory',d)
sorted_d=sorted(d.items())
print('ASCENDING directory',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('DESCENDING directory',sorted_d)