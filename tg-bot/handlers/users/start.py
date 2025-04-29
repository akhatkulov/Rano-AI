from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from states.test import UserState
from aiogram.client.session.middlewares.request_logging import logger
from loader import bot
from utils.db.alchemy import create_user,get_info
from keyboards.inline.phonenumber import send_number

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message,state: FSMContext):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    create_user(cid=message.chat.id)
    if get_info(cid=message.chat.id, type_data="phonenumber") != "null":
        await message.answer(f"Assalomu alaykum <b> {full_name} </b>\nO'zbekiston qonunchiligiga oid qanday savolingiz bor? Men sizga yordam berishga tayyorman. Savolingizni aniqroq bersangiz, shuncha yaxshi javob bera olaman. 🙂")
    else:
        await message.answer(
                    "📱 Telefon raqamingizni kiriting", reply_markup=send_number()
                )
        await state.set_state(UserState.send_number)