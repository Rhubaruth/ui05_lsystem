def lsystem(axiom: str, rules: dict, limit: int = 10):
    for _ in range(limit):
        new_ax = ''
        for c in axiom:
            if c in rules.keys():
                new_ax += rules[c]
            else:
                new_ax += c
        axiom = new_ax
    return axiom
