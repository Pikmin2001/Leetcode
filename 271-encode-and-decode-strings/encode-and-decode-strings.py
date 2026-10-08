class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        if strs == [""]:
            return strs
        
        ans = ""
        for word in strs:
            ans += (str(len(word)) + "#" + word)

        print(ans)
        return ans 


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == [""]:
            return [""]

        if not s:
            return [""]
        ans = []
        i = 0
        j = i
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1 #start at # letter
            ans.append(s[i:j + length+1])
            i = j+length+1
        return ans
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))