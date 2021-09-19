#https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    l = len(string)
    k = len(sub_string)
    count = 0
    if sub_string in string == True:
        count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



