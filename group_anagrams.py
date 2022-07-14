# fix this not completed
class Solution(object):
    
    def gen_dict(self, str):
        result = dict()
        for s in str:
            if s in result.keys():
                result[s] += 1
            else:
                result[s] = 1
        return result
        # result = set()
        # for s in str:
        #     result.add(s)
        # return result

    def is_anagram(self, str1, str2):
        dict_1 = self.gen_dict(str1)
        dict_2 = self.gen_dict(str2)

        if dict_1 == dict_2:
            return True
        # if dict_1 == dict_2:
        #     return True
        else:
            return False
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()

        for s in strs:
            if not bool(anagrams):
                anagrams[s] = [s]
            else:
                is_in = False
                for k in anagrams.keys():
                    if self.is_anagram(k, s):
                        anagrams[k].append(s)
                        is_in = True
                if not is_in:
                    anagrams[s] = [s]
                
        
        # make list of anagrams
        result = []
        for v in anagrams.values():
            result.append(v)
        return result
            
        