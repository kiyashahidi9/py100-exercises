scores = [96, 47, 113, 89, 100, 102]

def score_counter(scores):
    counter = 0
    for num in scores:
        if num >= 100:
            counter += 1
    return counter
    
print(score_counter(scores))