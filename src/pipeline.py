from src.scraper import load_raw_data
from src.parser import parse_grant
from src.cleaner import clean_data
from src.scorer import score_grant
from src.llm_scorer import llm_score
from src.storage import save

def run_pipeline():
    raw = load_raw_data()
    parsed = [parse_grant(g) for g in raw]
    cleaned = clean_data(parsed)

    for g in cleaned:
        g["rule_score"] = score_grant(g)
        g["llm_score"] = llm_score(g)
        g["final_score"] = round((g["rule_score"] + g["llm_score"]) / 2, 2)

    save(cleaned)
    return cleaned