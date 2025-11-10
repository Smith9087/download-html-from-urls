thonimport json
import os

def export_json(contents: List[dict], output_dir="data/output"):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "scraped_data.json")
    with open(output_file, "w") as f:
        json.dump(contents, f)