import codecs

string = "70"
binary_str = codecs.decode(string, "hex")
print(str(binary_str,'utf-8'))
