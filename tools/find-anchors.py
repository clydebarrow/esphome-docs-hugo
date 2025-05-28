#!/usr/bin/env python3

import os
import json
from bs4 import BeautifulSoup

# Config
PUBLIC_DIR = "public"
OUTPUT_JSON = "data/anchors.json"

# Descending priority of page paths
page_order = ["/components", "/cookbook", "/changelog"]

def page_priority(page_path):
    """Return a priority index based on the page_order list. Lower index = higher priority."""
    for idx, prefix in enumerate(page_order):
        if page_path.startswith(prefix):
            return idx
    return len(page_order)  # lowest priority

anchors_dict = {}

# Walk through all HTML files
for root, _, files in os.walk(PUBLIC_DIR):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)

            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                page_path = os.path.relpath(str(filepath), PUBLIC_DIR).replace("index.html", "").rstrip("/") + "/"

                # 1️⃣ Headings
                for level in range(1, 7):
                    for heading in soup.find_all(f"h{level}"):
                        if heading.has_attr("id"):
                            anchor_id = heading["id"]
                            entry = {
                                "page": page_path,
                                "title": heading.get_text(strip=True),
                                "level": level,
                                "type": "heading"
                            }
                            anchors_dict.setdefault(anchor_id, []).append(entry)

                # 2️⃣ <a> tags with id
                for a_tag in soup.find_all("a"):
                    if a_tag.has_attr("id"):
                        anchor_id = a_tag["id"]
                        entry = {
                            "page": page_path,
                            "title": a_tag.get_text(strip=True),
                            "level": None,
                            "type": "anchor"
                        }
                        anchors_dict.setdefault(anchor_id, []).append(entry)

# 3️⃣ Sort each anchor’s page list by page_order priority
for anchor_id in anchors_dict:
    anchors_dict[anchor_id].sort(key=lambda e: page_priority(e["page"]))

# 4️⃣ Sort anchor IDs for stable output
sorted_anchors = dict(sorted(anchors_dict.items()))

# Write the JSON output
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(sorted_anchors, f, indent=2)

print(f"✅ Collated & sorted anchors written to {OUTPUT_JSON}")
