# Parallel
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

# 기울기
def m(line):
    return (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])


def solution(dots):
    answer = 0

    for idx1 in range(len(dots)):
        for idx2 in range(len(dots)):
            if idx1 == idx2:
                continue
            else:
                line1 = [dots[idx1], dots[idx2]]
                line2 = []
                for idx in range(len(dots)):
                    if idx != idx1 and idx != idx2:
                        line2.append(dots[idx])

                m1 = abs(m(line1))
                m2 = abs(m(line2))
                if m1 == m2:
                    answer = 1
                    break

        if answer == 1:
            break

    return answer