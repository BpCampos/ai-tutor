from dotenv import load_dotenv
from model_request.tutor import Tutor
import os
import requests

load_dotenv()

class NotionWriter:
    def __init__(self, block_id):
        self.notion_token = os.getenv("NOTION_TOKEN")
        self.block_id = block_id
        self.base_url = f"https://api.notion.com/v1/blocks/{self.block_id}/children"
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
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ]
                    }
                }
            ],
            "position": {
            "type": "end"
            }
        }

        response = requests.patch(self.base_url, headers=self.headers, json=data)
        if response.status_code == 200:
            print("Content written to Notion successfully.")
        else:
            print(f"Failed to write to Notion: {response.status_code}, {response.text}")

notion_writer = NotionWriter(block_id="2fe159311885804686c2d026bb17c02e")
notion_writer.write_to_notion()