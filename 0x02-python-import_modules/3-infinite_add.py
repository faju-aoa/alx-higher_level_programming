#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_num = 0
    for i in range(len(sys.argv)-1):
        total_num += int(sys.argv[i + 1])
    print("{}".format(total_num))
