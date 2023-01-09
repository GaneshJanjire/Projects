def edit_distance(name, document_name):
    name_tokens = name.split()
    document_tokens = document_name.split()

    edit_distances = []

    for name_token in name_tokens:
        min_distance = float('inf')
        for document_token in document_tokens:
            distance = levenshtein(name_token, document_token)
            if distance < min_distance:
                min_distance = distance
        edit_distances.append(min_distance)

    return edit_distances


def levenshtein(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        levenshtein(s1[:-1], s2) + 1,
        levenshtein(s1, s2[:-1]) + 1,
        levenshtein(s1[:-1], s2[:-1]) + cost,
    )



name = "salman khan"
document_name = "salmann khan"
print(edit_distance(name, document_name))

name = "salman khan"
document_name = "khan salmann"
print(edit_distance(name, document_name))

name = "khan salman"
document_name = "salim khan"
print(edit_distance(name, document_name))