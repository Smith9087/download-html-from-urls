thonimport os

def export_html(contents: List[dict], output_dir="data/output"):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "scraped_data.html")
    with open(output_file, "w") as f:
        for item in contents:
            f.write(f"<p>URL: {item['url']}</p>")
            f.write(f"<div>{item['html']}</div>")