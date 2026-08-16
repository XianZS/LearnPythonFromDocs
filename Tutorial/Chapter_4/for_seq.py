names = [
    "jom",
    "kom",
    "lom",
]

# --- 按照自然顺序迭代names
# L = len(names)
# for index in range(L):
#     print(names[index])
# print(type(names))
# for child in names:
#     print(child)

names_copy = names.copy()
index = -1
for child in names_copy:
    if child == "kom":
        index = names_copy.index(child)
        names[index] = "-1"
        break
print(names)
