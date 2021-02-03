import json
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter

from bot.training.train import start_training
from bot.chat.chat import start_chatting

router = APIRouter()


@router.get('/train')
def train_model(epochs: Optional[int] = None):
    with open('intents.json', 'r') as json_file:
        intent = json.load(json_file)
    if not epochs:
        epochs = 2000
    res = start_training(intent, epochs)
    return {'model': res}


@router.get('/chat/{msg}')
async def chat(msg):
    with open('intents.json', 'r') as file:
        intent = json.load(file)
    bot_response = start_chatting(msg, intent)
    return {'bot': f'{bot_response}'}
