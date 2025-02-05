from collections import defaultdict

#fictional 5-dimensional values for testing
word_to_vector = defaultdict(lambda: "Not Present")
word_to_vector["tree"] = [0.45321, 0.12342, -0.65432, 0.23987, 0.33456]
word_to_vector["car"] = [0.75412, -0.23145, -0.19875, 0.87654, 0.12434]
word_to_vector["jump"] = [-0.31245, 0.89123, 0.10123, -0.09876, 0.65312]
word_to_vector["wood"] = [0.54312, 0.12211, -0.84321, 0.23124, 0.98455]
word_to_vector["house"] = [0.98712, 0.45121, -0.13421, -0.45311, 0.76234]
word_to_vector["bird"] = [0.39845, 0.67123, -0.21312, 0.98734, -0.33221]

def cosine_similarity(vec_a, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (sum([vec_a[i] ** 2 for i in range(len(vec_a))]) ** 0.5 * sum([vec_b[i] ** 2 for i in range(len(vec_b))]) ** 0.5)
    return numerator / denominator

def similar_words(word, top_k):
    return sorted(
        word_to_vector.keys(), 
        key=lambda x: -cosine_similarity(word_to_vector[x], word_to_vector[word])
    )[:top_k]

result = similar_words("tree", top_k=3)
print(result)