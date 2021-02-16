import py621
md5 = py621.public.genmd5("tests/md5test.jpg")
print("The calculated hash is: " + md5)
truemd5 = "55dff350e4d5f5a7602bc3dffc78e21a"
print("The actual value is: " + truemd5 + "\nAre they the same?")
if md5 == truemd5:
    print("Yes")
else: 
    print("No")