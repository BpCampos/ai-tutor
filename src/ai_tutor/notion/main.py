from ai_tutor.notion.notion_write import NotionWriter

def main():
    notion_writer = NotionWriter(block_id="2fe159311885804686c2d026bb17c02e")
    notion_writer.write_to_notion()

if __name__ == "__main__":
    main()