import re


def is_correct(exp: str) -> bool:
    pairs = re.sub(r"[^()[]{}]", "", exp)
    while pairs:
        prev_len = len(pairs)
        pairs = pairs.replace("()", "").replace("[]", "").replace("{}", "")
        if len(pairs) == prev_len:
            return False
    return True


expressions = [
    "({})[]",
    "[({})]",
    "{[)}]",
    "({}[{}])",
    "[({)}]",
    "{{[]]}",
    "{[()]}",
    "[{()}]",
    "({]})[{}",
    "({})[]{}",
]

for expression in expressions:
    print(f"{expression}: {is_correct(expression)}")
