from tester import Tester

cases = [
    # ("abab", "redblueredblue", True),
    # ("aaaa", "asdasdasdasd", True),
    # ("aabb", "xyzabcxzyabc", False),
    # ("d", "e", True),
    # ("d", "ef", True)
    # ("ab", "cd", True),
    # ("ab", "aa", False),
    ("sucks", "teezmmmmteez", False)
]


def digest(pattern: str, word: str, string: str, mapping_dict: dict):
    if len(pattern) == 0:
        if len(string) == 0:
            return True
        else:
            return False

    cur = pattern[0]
    if cur == pattern[0]:
        if string.startswith(word):
            next_pattern = pattern[1:]
            next_string = string[len(word):]
            next_word = word
            if len(pattern) == 1:
                return digest(next_pattern, next_word, next_string, mapping_dict)
            else:
                next_ = pattern[1]
                if next_ == cur:
                    return digest(next_pattern, next_word, next_string, mapping_dict)
                else:
                    for i in range(1, len(next_string) + 1):
                        generate = False
                        if next_pattern[0] not in mapping_dict:
                            next_word = next_string[:i]
                            if next_word in mapping_dict.values():
                                continue
                            generate = True
                            mapping_dict[next_pattern[0]] = next_word
                        else:
                            next_word = mapping_dict.get(next_pattern[0])
                        ret = digest(next_pattern, next_word, next_string, mapping_dict)
                        if ret is True:
                            return True
                        else:
                            if next_pattern[0] in mapping_dict and generate:
                                del mapping_dict[next_pattern[0]]
                    return False

        else:
            return False


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        next_string = s
        next_pattern = pattern
        for i in range(1, len(next_string) + 1):
            next_word = next_string[:i]
            ret = digest(next_pattern, next_word, next_string, {next_pattern[0]: next_word})
            if ret is True:
                return True
        if len(pattern) == len(s) == 1:
            return True
        return False


if __name__ == '__main__':
    Tester(cases, Solution, Solution.wordPatternMatch).run()
