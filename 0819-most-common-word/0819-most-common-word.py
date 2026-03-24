class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        counts: dict[str, int] = {}
        answer = ""
        best_count = 0

        for word in re.findall(r"[a-z]+", paragraph.lower()):
            if word in banned_set:
                continue

            counts[word] = counts.get(word, 0) + 1
            if counts[word] > best_count:
                best_count = counts[word]
                answer = word

        return answer


        