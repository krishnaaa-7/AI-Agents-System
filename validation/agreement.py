def agreement_score(answer1, answer2):
    a1 = (answer1 or "").strip().lower()
    a2 = (answer2 or "").strip().lower()

    if not a1 or not a2:
        return 0.5

    if a1 == a2:
        return 1.0

    if a1 in a2 or a2 in a1:
        return 0.8

    return 0.6
