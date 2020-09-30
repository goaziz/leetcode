def countSegments(s: str) -> int:
    t = " ".join(s.split())
    if not t:
        return 0
    else:
        t = t.split(' ')
        print(t)
        return len(t)

    # another solution
    # segment_count = 0
    #
    # for i in range(len(s)):
    #     if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
    #         segment_count += 1
    #
    # return segment_count