def longestCommonPrefix(strs: list[str]) -> str:

        res = ""

        word_length = min([len(x) for x in strs])

        if word_length == 0:
            return res

        for i in range(word_length):
            # print("Debug: " + str(i))
            all_ch = [word[i] for word in strs]
            if len(set(all_ch)) > 1:
                break
            if len(set(all_ch)) == 1:
                res = res + all_ch[0]
                
        return res

# Test -> OK    
# test = longestCommonPrefix(["a"])    
