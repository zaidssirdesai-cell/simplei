import sys

def simInt(principal, intrest, time):
    return (principal*intrest*time)/100

if __name__ == "__main__":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple intrest: ", simInt(p,i,t))
    print(sys.argv[0])