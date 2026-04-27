import pandas as pd
from pathlib import Path


def export_list_to_csv(usernames, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame({"username": usernames})
    df.to_csv(output_path, index=False)