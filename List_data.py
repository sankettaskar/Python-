print("Demonstration of List")

batches = ["PPA","LB","Angular","Python"]
print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

# We can store Heterogenious data

data1 = [11,"Shri Swami Samarth",3.14]
print(data1)
data2 = [23,"Om Shiv Shankara",22.48]
print(data2)

# We can create list of list

combined = [data1,data2]
print(combined)

# There are multiple methods that we can used to manipulate list

batches.append("MEAN")
print(batches)

batches.insert(2,"LSP")
print(batches)

batches.remove("LSP")
print(batches)

batches.pop()
print(batches)

batches.pop(2)
print(batches)

del batches[1:]
print(batches)

batches.extend(["LB","PYTHON","ANGULAR","MEAN"])
print(batches)

batches.sort()
print(batches)








































