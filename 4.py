# sum(probs) == 1
# probs[i] > 0
# random.random() ~ U(0, 1)
import random


def main(size, probs):
    new_probs = [0]
    for i in range(len(probs)):
        new_probs.append(new_probs[i] + probs[i])
    res = []
    for _ in range(size):
        rand = random.random()
        left, right = 0, len(new_probs)
        while left < right:
            m = (left + right + 1) // 2
            if rand > new_probs[m]:
                left = m
            else:
                right = m - 1
        print(round(rand, 2), left)


lst = [0.1, 0.4, 0.2, 0.3]
main(10, lst)
