import os

files = os.listdir("/")


for file in files:
    print(file)

print(files.__len__())