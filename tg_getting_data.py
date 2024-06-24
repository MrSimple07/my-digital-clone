import json
import os
import asyncio
from decouple import config
from loguru import logger
from telethon import TelegramClient
from telethon.tl.custom.dialog import Dialog
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.patched import Message
from pathlib import Path

#You have to get the TELEGRAM_APP_ID and TELEGRAM_APP_HASH from telegram org
PHONE_NUMBER = 'your number with country code'
TELEGRAM_APP_ID = ""
TELEGRAM_APP_HASH = ""

# This is the name of the session file that will be created and stored in the working directory. Session files are used to store the state of the client, so that it can be resumed later so you dont have to login everytime you run the code
session_name = "session_1"

def save_to_json(file_to_save: list[dict[str, str]], file_name: str) -> None:
    # Create the directory if it doesn't exist
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(file_to_save, f, ensure_ascii=False)

async def get_dialogs(client: TelegramClient, limit: int | None = 100) -> list[Dialog]:
    """Get all dialogs from the Telegram."""
    dialogs: list[Dialog] = await client.get_dialogs(limit=limit)
    dialogs = [
        dialog for dialog in dialogs if dialog.is_user
    ]  # remove groups or channels
    logger.info(f"Found {len(dialogs)} dialogs")
    return dialogs

async def parse_messages(client: TelegramClient, dialog: Dialog, limit: int = 1000) -> list[dict]:
    """Get all messages from the dialog."""
    all_messages_list = []
    offset_id = 0

    while True:
        messages: list[Message] = await client(
            GetHistoryRequest(
                peer=dialog,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )
        messages = messages.messages
        if not messages:
            break

        all_messages_list.extend(
            {
                "date": message.date.isoformat(),
                "message": message.message,
                "out": message.out,
            }
            for message in messages
            # Filter audio or video content
            if message.message and not message.via_bot
        )
        offset_id = messages[-1].id
    return all_messages_list

async def main():
    """Parse and save private chat messages."""
    data_dir = Path(__file__).parent / "data"
    async with TelegramClient(PHONE_NUMBER, TELEGRAM_APP_ID, TELEGRAM_APP_HASH) as client:
        await client.start()
        
        dialogs = await get_dialogs(client, limit=None)
        for dialog in dialogs:
            all_messages_list = await parse_messages(client, dialog)
            save_to_json(all_messages_list, data_dir / f"{dialog.id}.json")
            logger.success(f"Saved {len(all_messages_list)} messages for {dialog.name}")

            
if __name__ == "__main__":
    asyncio.run(main())