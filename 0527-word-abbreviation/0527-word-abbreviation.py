class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node.setdefault(w, {})
                rest = len(cands) - i - 1
                node[rest] = node.get(rest, 0) + 1

        ans = []
        for word in words:
            if len(word) <= 3: 
                ans.append(word)
                continue
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node[w]
                rest = len(cands) - i - 1
                if rest > 1 and node[rest] < 2:
                    ans.append(word[:i+1]+str(rest)+word[-1])
                    break
                elif rest <= 1:
                    ans.append(word)
                    break
        
        
        return ans