class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            i, tmp = 0, ""
            while e[i] != "@" and e[i] != "+":
                if e[i] != ".":
                    tmp += e[i]
                i += 1
            while e[i] != "@":
                i += 1
            domain = e[i+1:]
            unique.add((tmp, domain))
        return len(unique)