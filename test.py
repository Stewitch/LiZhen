d = {'a':{'b':{'c':{'d':{'e':["f",'g']}}}}}

key = "a.b.c.d"
keys = key.split(".")
value = ["d","f"]

# exp = "d"
# for i in range(len(keys)):
#     exp = exp + "[" + f"'{keys[i]}'" + "]"
#     if i == len(keys)-1:
#         exp = exp + "=" + value
#         exec(exp)

current = d
keys = key.split(".")
        
for k in keys[:-1]:
    if k not in current:
        raise KeyError(f"Key not found: {k}")
    current = current[k]
            
        # 设置最后一个键的值
if keys[-1] not in current:
    raise KeyError(f"Key not found: {keys[-1]}")
current[keys[-1]] = value
    
print(d)

