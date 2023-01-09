import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.txt':
                    print(full_filename)
    except PermissionError:
        pass


# search("c:/")
na=3
Na=4
a=[]
a.append(na)
a.append(Na)
print(a)