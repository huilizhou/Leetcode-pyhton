class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 我的想法，但是集合不太熟悉
        keyset = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for keys in keyset:
            for word in words:
                line = set(word.lower())
                if line.issubset(set(keys)):
                    res.append(word)
        return res

        # 人家的解法
        # Line1 = "QWERTYUIOPqwertyuiop"
        # Line2 = "ASDFGHJKLasdfghjkl"
        # Line3 = "ZXCVBNMzxcvbnm"
        # Output = []
        # for word in words:
        #     result = []
        #     for letter in word:
        #         if letter in Line1:
        #             result.append(1)
        #         if letter in Line2:
        #             result.append(2)
        #         if letter in Line3:
        #             result.append(3)
        #     new_result = []
        #     for item in result:
        #         if item not in new_result:
        #             new_result.append(item)
        #     if len(new_result) == 1:
        #         Output.append(word)
        # return Output

        # 人家的解法，用hashmap
        # keysets={"q":1,"w":1,"e":1,"r":1,"t":1,"y":1,"u":1,"i":1,"o":1,"p":1,"a":2,"s":2,"d":2,"f":2,"g":2,"h":2,"j":2,"k":2,"l":2,"z":3,"x":3,"c":3,"v":3,"b":3,"n":3,"m":3}
        # return[word for word in words if len(set([keysets[i] for i in word.lower()]))==1]


print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
