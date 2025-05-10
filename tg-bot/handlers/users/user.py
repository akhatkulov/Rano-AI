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
        await bot.send_photo(chat_id=call.message.chat.id,photo="https://t.me/the_solodest/178",caption=f"Assalomu alaykum \nO'zbekiston qonunchiligiga oid qanday savolingiz bor? Men sizga yordam berishga tayyorman. Savolingizni aniqroq bersangiz, shuncha yaxshi javob bera olaman. 🙂")
    else:
        await call.message.answer(
                    "📱 Telefon raqamingizni kiriting", reply_markup=send_number()
                )
        await state.set_state(UserState.send_number)

@router.message(UserState.send_number,F.content_type == types.ContentType.CONTACT)
async def send_ad_to_users(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    change_info(cid=message.chat.id, type_data="phonenumber", value=str(contact))
    await bot.send_photo(chat_id=message.chat.id,photo="https://t.me/the_solodest/178",caption=f"Assalomu alaykum \nO'zbekiston qonunchiligiga oid qanday savolingiz bor? Men sizga yordam berishga tayyorman. Savolingizni aniqroq bersangiz, shuncha yaxshi javob bera olaman. 🙂")
    await state.clear()

def escape_markdown_v2(text: str) -> str:
    escape_chars = r'\_[]()~`>#+-=|{}.!'
    for ch in escape_chars:
        text = text.replace(ch, f'\\{ch}')
    return text

MAX_MESSAGE_LENGTH = 2000

def split_message(message):
    # Xabarni 4096 belgidan kichik bo'laklarga bo'lib yuborish
    return [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]
def escape_markdown(message):
    # Markdown belgilari: * _ [ ] ( ) ~ ` > + - = | {} . ! va boshqalar
    escape_chars = ['*', '_', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in escape_chars:
        message = message.replace(char, f'\\{char}')
    return message

def remove_markdown(text):
    # Markdown formatidagi belgilarni olib tashlash
    markdown_patterns = [
        (r'(\*|_){1,2}(.*?)\1{1,2}', ''),  # *bold* yoki _italic_
        (r'`(.*?)`', ''),  # `inline code`
        (r'\[([^\]]+)\]\([^\)]+\)', ''),  # [link](url)
        (r'~~(.*?)~~', ''),  # ~~strikethrough~~
        (r'^(>.*)', ''),  # > blockquotes
        (r'(?<=\n)(#[^\n]+)', ''),  # # headings
        (r'[\\*_`\[\]()~\#\+\-=\|{}!<>]', '')  # escaping all other Markdown special chars
    ]
    
    for pattern, replacement in markdown_patterns:
        text = re.sub(pattern, replacement, text)
    
    return text


@router.message(F.content_type == types.ContentType.TEXT)
async def savol_javob(msg: types.Message):
    x = await msg.answer("🔎")
    res = await ask_rano(msg.text)
    if len(res)>2048:
        res = remove_markdown(res)
        res = split_message(res)
        for r in res:
            await bot.send_message(chat_id=msg.chat.id,text=r)
    else:
        await bot.send_message(chat_id=msg.chat.id,text=res,parse_mode="Markdown")
    await bot.delete_message(chat_id=msg.chat.id,message_id=x.message_id)