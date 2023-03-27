# Bubbling

def is_possible(item, avails) -> bool:
    if len(avails) == 0:
        return False

    if len(item) == 0:
        return True

    for a in avails:
        loc = item.find(a)
        if loc > -1:
            first = item[:loc]
            second = item[loc + len(a):]
            if is_possible(first, avails) and is_possible(second, avails):
                return True


def solution(babbling):
    answer = 0
    avails = ['aya', 'ye', 'woo', 'ma']

    for item in babbling:
        if is_possible(item, avails):
            answer = answer + 1

    return answer


assert solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1
assert solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
