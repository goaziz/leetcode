import re
from typing import List


class Solution:
    IPV4 = 'IPv4'
    IPV6 = 'IPv6'

    def has_invalid_chars(self, s, ip_type):
        if ip_type == Solution.IPV4:
            return not s.isdigit()
        else:
            return bool(re.search(r'[^A-Fa-f0-9]', s))

    def validate_ipv4(self, ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return 'Neither'

        for part in parts:
            if not part or self.has_invalid_chars(part, Solution.IPV4):
                return 'Neither'
            if len(part) > 1 and part[0] == '0':
                return 'Neither'
            if not 0 <= int(part) <= 255:
                return 'Neither'

        return Solution.IPV4

    def validate_ipv6(self, ip):
        parts = ip.split(':')
        if len(parts) != 8:
            return 'Neither'

        for part in parts:
            if not part or self.has_invalid_chars(part, Solution.IPV6):
                return 'Neither'
            if len(part) > 4:
                return 'Neither'

        return Solution.IPV6

    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and ':' in queryIP:
            return 'Neither'
        elif '.' in queryIP:
            return self.validate_ipv4(queryIP)
        elif ':' in queryIP:
            return self.validate_ipv6(queryIP)
        else:
            return 'Neither'


obj = Solution()
queryIP = "1.0.1."
print(obj.validIPAddress(queryIP))
