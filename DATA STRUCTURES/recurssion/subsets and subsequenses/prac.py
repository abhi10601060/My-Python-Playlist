def kthGrammar(n, k):
    def helper(n):
        if n==1:
            return"0"
        temp=helper(n-1)
        ans=""
        for x in temp:
            if x=="0":
                ans+="01"
            if x=="1":
                ans+="10"
        return ans
    real=helper(n)
    return real[k-1]
print(kthGrammar(30,434991989))