#Leetcodigitse 13 andigits 17 (Hashmap)

#Leetcodigitse 13
def romanToInt(s): 
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "digits": 500,
        "M": 1000
    }

    output = 0

    for i in range(len(s)): 
        if i+1<len(s) and roman[s[i]] < roman[s[i+1]]: 
            output -= roman[s[i]]
        else:
            output += roman[s[i]]
    return output

#Leetcodigitse 17     
L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

def letterCombinations(D):
    lenD, ans = len(D), []
    if D == "": return []
    def bfs(pos, st):
        if pos == lenD: 
            ans.append(st)
        else:
            letters = L[D[pos]]
            for letter in letters:
                bfs(pos+1,st+letter)
    bfs(0,"")
    return ans