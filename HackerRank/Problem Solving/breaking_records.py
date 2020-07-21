def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    count_min = 0
    count_max = 0

    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            count_max += 1
        if scores[i] < min_score:
            min_score = scores[i]
            count_min += 1
    return [count_max, count_min]
