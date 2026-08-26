from dotenv import load_dotenv
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from model_request.tutor import Tutor
import os
import requests

load_dotenv()

class NotionWriter:
    def __init__(self, block_id):
        self.notion_token = os.getenv("NOTION_TOKEN")
        self.block_id = block_id
        self.base_url = f"https://api.notion.com/v1/pages/{self.block_id}/markdown"
        self.headers = {
            "Authorization": f"Bearer {self.notion_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2026-03-11"
        }

    def get_definition(self):
        tutor = Tutor()
        definition = tutor.get_definition()
        return definition

    def write_to_notion(self):
        content = self.get_definition()

        data = {
        "type": "insert_content",
        "insert_content": {
            "content": content,
            "position": {
            "type": "end"
            }
        }
    }

        response = requests.patch(self.base_url, headers=self.headers, json=data)
        if response.status_code == 200:
            print("Content written to Notion successfully.")
        else:
            print(f"Failed to write to Notion: {response.status_code}, {response.text}")

notion_writer = NotionWriter(block_id="2fe159311885804686c2d026bb17c02e")
notion_writer.write_to_notion()