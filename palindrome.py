from collections import deque
import re


def is_palindrome(phr: str) -> bool:
    dq = deque(re.sub(r"[^A-z]", "", phr).lower())
    while len(dq) >= 2:
        if dq.popleft() != dq.pop():
            return False
    return True


phrases = [
    "sIr, i DeManD, I aM a MaID NaMeD IrIs.",
    "this is not a palindrome",
    "yO, BanAnA bOY!",
    "this is also not a palindrome",
    "this is definitely not a palindrome",
    "eVa, cAn i SeE bEeS In A cAvE?",
    "mAdAm, iN EdEn, I’m aDaM.",
    "a man, a plan, a canal, Panama!",
    "Never a foot too far, even.",
    "tHiS iS cErTaInLy NoT a PaLiNdRoMe,",
]

for phrase in phrases:
    print(f"{phrase}: {is_palindrome(phrase)}")
