def parse_grant(grant):
    return {
        "title": grant.get("title"),
        "deadline": grant.get("deadline"),
        "funding": float(grant.get("funding")),
        "description": grant.get("description")
    }