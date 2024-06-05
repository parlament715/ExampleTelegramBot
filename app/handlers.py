from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from aiogram import F,Router
from aiogram.fsm.context import FSMContext
from loader import bot, rq
from config import today
from icecream import ic
from app.keyboard import keyboard_Inline, keyboard_Markup
from random import randint

router = Router()

@router.message(CommandStart())
async def start_reaction(message: Message):
    a = randint(1,2)
    if a == 1:
        await message.answer("Сообщение",reply_markup=keyboard_Inline)
    elif a == 2:
        await message.answer("Сообщение",reply_markup=keyboard_Markup)

@router.message(lambda _ : (F.data == "KB1") or (F.data == "KB2"))
async def kb_reaction(message : Message):
    await message.answer("Ты молодец!")


@router.callback_query(F.data == "kb")
async def kbb_reaction(call : CallbackQuery ):
    await call.answer()
    await call.message.answer("Ты холодец!")