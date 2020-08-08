def designerPdfViewer(h, word):
    word = [h[ord(c) - ord('a')] for c in word]
    return max(word) * len(word)