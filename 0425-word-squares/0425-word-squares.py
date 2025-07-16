class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        res = []

        prefix_map = defaultdict(set)
        for word in words:
            for i in range(1, n):
                prefix = word[:i]
                prefix_map[prefix].add(word)

        def backtrack(i, word_sqrs):
            if i == n:
                res.append(word_sqrs)
                return

            prefix = ''
            for word in word_sqrs:
                prefix += word[i]

            for word2 in prefix_map[prefix]:
                backtrack(i + 1, word_sqrs + [word2])

        for word in words:
            backtrack(1, [word]) # start

        return res