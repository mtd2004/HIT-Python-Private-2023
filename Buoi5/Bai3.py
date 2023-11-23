def most_words(str):
    unique_words = set(str.lower().split())
    word_counts = {}
    for word in unique_words:
        word_counts[word] = str.lower().split().count(word)
    max_count = max(word_counts.values())
    most_common = [(word, count) for word, count in word_counts.items() if count == max_count]
    return most_common

van_ban = input()
ket_qua = most_words(van_ban)
print(ket_qua)
