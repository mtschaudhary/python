import json
a = '{"name": "mitesh", "age":20}'

res = json.loads(a)

print(res)
print(type(res))

print(json.dumps(res), type(json.dumps(res)))
print(eval(a), type(eval(a)))

b = '[1,2,3]'

print(eval(b))
print(type(eval(b)))    
