from typing import Any, List

import pandas as pd  # type: ignore
from pandas import DataFrame  # type: ignore


def save(grants: List[Any]) -> None:
    df = pd.DataFrame(grants)
    df.to_csv("output/structured_grants.csv", index=False)