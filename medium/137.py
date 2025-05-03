# 2019.04.18

class Solution(object):
    def singleNumber(self, nums):
        resultDic = {}
        for i in nums:
            if i in resultDic.keys():
                if resultDic[i] == 2:
                    del resultDic[i]
                else:
                    resultDic[i] = resultDic[i] + 1
            else:
                resultDic[i] = 1
        return list(resultDic.keys())[0]