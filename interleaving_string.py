def isInterleave(s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1_idx = 0
        s2_idx = 0
        s3_idx = 0
        last_s1_idx = 0
        last_s2_idx = 0
        current_sub = ''
        result = None
        while True:
            if is_done(s1_idx, s1) and is_done(s2_idx, s2) and is_done(s3_idx, s3):
                result = True
                print('in True result if')
                
            if s3[s3_idx] == s1[s1_idx] and s3[s3_idx] == s2[s2_idx]:
                last_s1_idx = s1_idx
                last_s2_idx = s2_idx
                while True:
                    if s3[s3_idx] == s1[s1_idx] and s3[s3_idx] == s2[s2_idx]:
                        s1_idx += 1
                        s2_isx += 1
                    else:
                        if s3[s3_idx] == s1[s1_idx]:
                            s1_idx += 1
                            s2_idx = last_s2_idx
                            break
                        elif s3[s3_idx] == s2[s2_idx]:
                            s2_idx += 1
                            s1_idx = last_s1_idx
                            break
                        else:
                            s1_idx += 1
                            s2_idx = last_s2_idx       #giving priority to s1 when having two identical same substrings from both s1 and s2
                            break
                            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
            elif s3[s3_idx] == s1[s1_idx] and s1_idx != -1:
                print('in s1')
                s1_idx += 1
                s3_idx += 1
                if is_done(s1_idx, s1):
                    s1_idx = -1
            elif s3[s3_idx] == s2[s2_idx] and s2_idx != -1:
                print('in s2')
                s2_idx += 1
                s3_idx += 1
                if is_done(s2_idx, s2):
                    s2_idx = -1
            else:
                print('not found')
                result = False
                break
        
        return result