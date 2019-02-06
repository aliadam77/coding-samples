def jump(numjumps,cur,c):
    if cur == (len(c)-1):
        return numjumps
    if (cur+2 < len(c)):
         if (c[cur+2] != 1):
            numjumps +=1
            numjumps = jump(numjumps,cur+2,c)
         else:
            numjumps+=1
            numjumps = jump(numjumps,cur+1,c)
    return numjumps
def jumpingOnClouds(c):
    numjumps =0
    result = jump(numjumps,0,c)
    return result
def main():
    c = [0,0,1,0,0,1,0]
    result = jumpingOnClouds(c)
main()
