from typing import List

from tester import Tester
from collections import deque

cases = [
    # ("hot", "dog", ["hot", "dog"], []),
    # ("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"],
    #  ["leet", "lest", "lost", "lose", "lode", "code"])

    ("cet", "ism",
     ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
      "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan",
      "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
      "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry", "led",
      "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
      "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
      "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
      "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag",
      "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
      "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
      "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod",
      "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
      "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and",
      "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
      "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
      "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum",
      "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw",
      "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
      "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex",
      "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
      "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
      "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye",
      "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug",
      "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
      "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
      "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc",
      "moe", "caw", "eel", "dix", "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
      "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
      "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con",
      "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
      "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah", "hie",
      "aim", "ike", "jed", "ego", "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal",
      "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac",
      "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid", "god", "duo", "lin", "aid",
      "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
      "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob", "mow", "jot",
      "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe", "amp", "ale",
      "bud", "gee", "pin", "dun", "pat", "ten", "mob"], None)

]


def is_word_similar(word1, word2):
    diff_letter_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_letter_count += 1
        if diff_letter_count >= 2:
            return False

    if diff_letter_count == 0:
        return False
    return True


def transform_dfs(source_word, target_word, word_list, visited, result):
    if source_word == target_word:
        return True

    for idx, word in enumerate(word_list):
        if visited[idx] is True or is_word_similar(source_word, word) is False:
            continue

        visited[idx] = True
        result.append(word)
        if transform_dfs(word, target_word, word_list, visited, result):
            return True
        else:
            result.pop(-1)
            visited[idx] = False

    return False


class Result:
    def __init__(self, word, base_set):
        self.word = word
        base_set.add(word)
        self.parent = None
        self.route = base_set


def has_res_list_duplicate(res: Result):
    duplicate_words = set()
    while res.parent is not None:
        if res.word in duplicate_words:
            return True
        duplicate_words.add(res.word)
        res = res.parent

    return False


def transform_bfs(source_word, target_word, word_list, result):
    word_set = set(word_list)
    base_res = Result(source_word, set())

    queue = deque([(source_word, base_res)])

    dead_routes = set()

    while len(queue) > 0:
        cur_word, base_res = queue.popleft()
        if cur_word in dead_routes:
            # 跳过被剪枝的死路
            continue

        if cur_word == target_word:
            result.append(cur_word)
            res = base_res
            while res.parent is not None:
                res = res.parent
                result.append(res.word)

            return True

        q_len = len(queue)
        for word in word_set:

            if is_word_similar(cur_word, word) is False:
                continue

            if word in base_res.route:
                continue
            res = Result(word, base_res.route)
            res.parent = base_res
            queue.append((word, res))

        if q_len == len(queue):
            # 证明这个word走不动了，且不可能到达终点，所以做剪枝
            dead_routes.add(cur_word)
            word_set.remove(cur_word)

    return False


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
    #     if endWord not in wordList:
    #         return []
    #
    #     result = [beginWord]
    #     if transform_dfs(beginWord, endWord, wordList, [False] * len(wordList), result):
    #         return result
    #     else:
    #         return []

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        if endWord not in wordList:
            return []

        result = list()
        if transform_bfs(beginWord, endWord, wordList, result):
            return result[::-1]
        else:
            return []


if __name__ == '__main__':
    Tester(cases, Solution, Solution.findLadders).run()
