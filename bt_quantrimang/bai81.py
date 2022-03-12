import zlib

s = "hello world!hello world!hello world!hello world!"
t = zlib.compress(s.encode("utf-8"))  # Nen la ntn day

print(t)
print(zlib.decompress(t))  #  giai nen ntn day
