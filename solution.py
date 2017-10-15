import sys

def sortline(line):
    ints = []
    strs = []
    mask = []   # helper list for further zipping, 0 - str, 1 - int
    words = line.split()
    
    # decompose
    for w in words:
        if w.isdigit() or (len(w) > 1 and w[0] == '-' and w[1:].isdigit()):
            ints.append(int(w))
            mask.append(1)
        else:
            strs.append(w)
            mask.append(0)

    ints.sort(reverse=True)
    strs.sort(reverse=True)

    # combine
    masked = map(lambda x: str(ints.pop()) if x else strs.pop(), mask)
    return " ".join(masked)

if __name__ == '__main__':
    line = sys.stdin.readline()
    print(sortline(line))
