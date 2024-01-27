from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            d = email.split('@')
            plus_idx = d[0].find('+')
            if plus_idx != -1:
                clean_email = d[0][:plus_idx].replace('.', '') + '@' + d[1]
            else:
                clean_email = d[0].replace('.', '') + '@' + d[1]
            seen.add(clean_email)

        return len(seen)

    def numUniqueEmails2(self, emails: List[str]) -> int:
        # Hash set to store all the unique emails.
        uniqueEmails = set()

        for email in emails:
            # Split into two parts: local and domain.
            name, domain = email.split('@')

            # Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.', '')

            # Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)

        return len(uniqueEmails)


obj = Solution()
emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
print(obj.numUniqueEmails(emails))
