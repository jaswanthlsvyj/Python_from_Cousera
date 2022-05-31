a = "ast"
try:
    b = int(a)
except:
    a = -1
    print("An traceback error: ", a)

a = "123"
try:
    b = int(a)
except:
    a = -1
print(a)
