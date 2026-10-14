class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # "shifting_id":["strings"]
        print()

        for string in strings:
            shifting_id = [0]
            if len(string) == 1:
                shifting_id.append(0)
            else:
                for i in range(1, len(string)):
                    shifting_id.append(chr((ord(f"{string[i]}") - ord(f"{string[i-1]}")) % 26 + ord('a')))
            hashMap[tuple(shifting_id)].append(string)
        
        return [seq for seq in hashMap.values()]