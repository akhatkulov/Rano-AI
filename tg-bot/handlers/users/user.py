from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from utils.db.alchemy import get_info,change_info
from states.test import UserState
from keyboards.reply.phonenumber import send_number
from utils.api.rano_ai import ask_rano
from loader import bot
import re 

router = Router()



@router.callback_query(F.data == "check_join")
async def check_join_cb_answer(call: types.CallbackQuery,state:FSMContext):
    await bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )
    if get_info(cid=call.message.chat.id, type_data="phonenumber") != "null":
        await call.message.answer("Salom, O'zbekiston qonunchiligiga oid qanday savolingiz bor? Men sizga yordam berishga tayyorman. Savolingizni aniqroq bersangiz, shuncha yaxshi javob bera olaman. 🙂")
    else:
        await call.message.answer(
                    "📱 Telefon raqamingizni kiriting", reply_markup=send_number()
                )
        await state.set_state(UserState.send_number)

@router.message(UserState.send_number,F.content_type == types.ContentType.CONTACT)
async def send_ad_to_users(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    change_info(cid=message.chat.id, type_data="phonenumber", value=str(contact))
    message.answer("Salom, O'zbekiston qonunchiligiga oid qanday savolingiz bor? Men sizga yordam berishga tayyorman. Savolingizni aniqroq bersangiz, shuncha yaxshi javob bera olaman. 🙂")
    await state.clear()

def escape_markdown_v2(text: str) -> str:
    escape_chars = r'\_[]()~`>#+-=|{}.!'
    for ch in escape_chars:
        text = text.replace(ch, f'\\{ch}')
    return text

@router.message(F.content_type == types.ContentType.TEXT)
async def savol_javob(msg: types.Message):
    text = """**Huquqni muhofaza qilish organlariga murojaat qiling:** Eng muhimi, darhol politsiyaga xabar bering."""
    escaped_text = escape_markdown_v2(text)

    await msg.answer(escaped_text, parse_mode="MarkdownV2")

    x = await msg.answer("🔎")
    res = await ask_rano(msg.text)
    print(res)
    html_text = escape_markdown_v2(res)
    await msg.answer(html_text, parse_mode="MarkdownV2")
    await bot.delete_message(chat_id=msg.chat.id,message_id=x.message_id)