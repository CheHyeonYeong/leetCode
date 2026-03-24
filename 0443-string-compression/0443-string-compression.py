class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        left = 0

        for right in range(len(chars) + 1):
            if right == len(chars) or chars[right] != chars[left]:
                chars[write] = chars[left]
                write += 1

                count = right - left
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                left = right

        return write