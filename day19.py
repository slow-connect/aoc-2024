import aoc

data = aoc.get_str(19)[:-1]
patterns, builds = data.split('\n\n')
patterns = patterns.split(', ')
patterns.sort(key=lambda x: len(x), reverse=True)
builds = builds.split('\n')


def p1(patterns, builds):
    def composable(S, W):
        memo = {}
        for w in W:
            memo[w] = True
        return composable_aux(S, W, memo)


    def composable_aux(S, W, memo):
        if S == "":
            return True
        if S in memo:
            return memo[S]
        for w in W:
            if S.startswith(w):
                if composable_aux(S[len(w):], W, memo):
                    memo[S] = True
                    return True
        memo[S] = False
        return False

    cnt = 0
    for b in builds:
        if composable(b, patterns):
            cnt += 1
    print(cnt)

p1(patterns, builds)


def p2(patterns, builds):
    def composable(S, W):
        return composable_aux(S, W, dict())


    def composable_aux(S, W, memo):
        if S == "":
            return 1
        if S in memo:
            return memo[S]
        count = 0
        for w in W:
            if S.startswith(w):
                if composable_aux(S[len(w):], W, memo):
                    count += composable_aux(S[len(w):], W, memo)

        memo[S] = count
        return count
    cnt = 0
    for b in builds:
        cnt += composable(b, patterns)
    print(cnt)

p2(patterns, builds)
