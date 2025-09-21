class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = []
        max_len = 0
        #split_s = list(s)
        for char in s:
            # char = split_s[index]
            # print(current_chars,char,max_len)
            if char in current_chars:
                # current_len = len(current_chars)
                max_len = max(len(current_chars),max_len)
                current_chars = current_chars[current_chars.index(char)+1:]
            current_chars.append(char)
            #print(current_chars,char,max_len)
        return max(len(current_chars),max_len)