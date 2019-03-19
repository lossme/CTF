m1 = open("data/密文.txt", "rb").read()
m2 = open("data/明文.txt", "rb").read()

message = "".join(map(lambda item: chr(item[0] ^ item[1]), zip(m1, m2)))
print(message)
