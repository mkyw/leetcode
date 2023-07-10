class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_chars = list()
        t_chars = list()
        for i in s:
            s_chars.append(i)
        for j in t:
            t_chars.append(j)

        print(s_chars)
        print(t_chars)

        for x in s:
            if x in t_chars:
                s_chars.remove(x)
                t_chars.remove(x)

                print(x)
                print(s_chars)
                print(t_chars)
            else:
                return False

        if len(t_chars) == 0:
            return True
        else:
            return False

    print(isAnagram("anagram", "nagaram"))
