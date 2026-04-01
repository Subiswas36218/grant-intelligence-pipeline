def score_grant(grant):
    score = 0

    if grant["funding"] > 50000:
        score += 0.5

    if "AI" in grant["description"]:
        score += 0.3

    return score