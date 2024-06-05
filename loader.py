from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.database.request import Request

rq = Request()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()