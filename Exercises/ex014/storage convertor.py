def megabytes(GB):
    return 1024 * GB
def kilobytes(MB):
    return 1024 * MB
def bytes(KB):
    return 1024 * KB

gb = int(input("Input gigabytes: "))

print(f"Gigabytes {gb} GB")
print(f"to megabytes  {megabytes(gb)} MB")
print(f"to kilobytes  {kilobytes(megabytes(gb))} KB")
print(f"to bytes  {bytes(kilobytes(megabytes(gb)))} KB")