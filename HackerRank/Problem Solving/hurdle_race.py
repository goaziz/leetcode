def hurdleRace(k, height):
    max_h = max(height)
    if max_h > k:
        return max_h - k
    return 0
