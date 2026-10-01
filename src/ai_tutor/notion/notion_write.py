from dotenv import load_dotenv
from ai_tutor.model_request.tutor import Tutor
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
        data = {
                "type": "insert_content",
                "insert_content": {
                    "content": f"""{definition}
---
                                """,
                    "position": {
                    "type": "end"
                    }
                }
            }

        return data

    def write_to_notion(self):

        data = self.get_definition()

        to_write = input("Write the definition to Notion? (y/n): ")

        if to_write.lower() != 'y':
            print("Aborted writing to Notion.")
            return

        response = requests.patch(self.base_url, headers=self.headers, json=data)
        if response.status_code == 200:
            print("Content written to Notion successfully.")
        else:
            print(f"Failed to write to Notion: {response.status_code}, {response.text}")