class Solution(object):
    
    def gen_dict(self, word):
        if len(word) == 0:
            return dict()
        result = dict()
        for i in range(26):
            result[i] = 0
        for c in word:
            idx = ord(c) - 97
            result[idx] += 1
        return result
    
    def is_equal(self, dict_1, dict_2):
        if len(dict_1) == 0 or len(dict_2) == 0:
            return False
        for i in range(26):
            if dict_1[i] == dict_2[i]:
                continue
            else:
                return False
        return True
    
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = []
        empty_s_flag = False
        for s in strs:
            dict_s = self.gen_dict(s)
            if len(dict_s) == 0:
                if not empty_s_flag:
                    groups.append([''])
                    empty_s_flag = True
                else:
                    for g in groups:
                        g_rep = g[0]
                        if g_rep == '':
                            g.append('')
                continue
            if len(groups) == 0:
                groups.append([s])
            else:
                found = False
                for g in groups:
                    g_rep = g[0]
                    rep_dict = self.gen_dict(g_rep)
                    if self.is_equal(rep_dict, dict_s):
                        g.append(s)
                        found = True
                if not found:
                    groups.append([s])
              
        return groups
                
            
            
            