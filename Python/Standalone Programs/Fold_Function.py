def main():
    foldlist = ["cat", "dog", "owl", "snake"]
    x = len(foldlist)
    y = int(x/2)
    a = [foldlist[0:y]]
    b = [foldlist[y:x]]
    print(a)
    print(b)
main()
