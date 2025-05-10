import telebot

TOKEN = '6459864183:AAGfHQ_xo1NhgU8ic0iihMLh13xPAtodPFs'
CHAT_ID = '6521895096'

bot = telebot.TeleBot(TOKEN)

message = (
    "Agar sizga hujum qilishsa, O'zbekiston qonunchiligiga muvofiq quyidagi choralarni ko'rishingiz mumkin:\n\n"
    "1. **Tez yordam va politsiyaga murojaat qiling:** Agar jarohatlangan bo'lsangiz, darhol tez yordam chaqiring. "
    "Shuningdek, politsiyaga xabar bering. Politsiya hodisa joyiga kelib, bayonnoma tuzadi va tergov boshlaydi.\n"
    "2. **Dalillarni saqlash:** Hujum bilan bog'liq har qanday dalillarni saqlashga harakat qiling. "
    "Bu tibbiy xulosalar, guvohlar, fotosuratlar yoki videoyozuvlar bo'lishi mumkin.\n"
    "3. **Advokat bilan maslahatlashing:** Huquqlaringizni himoya qilish va keyingi harakatlar rejasini tuzish uchun advokat bilan maslahatlashing.\n"
    "4. **Ariza yozish:** Politsiyaga hujum faktini tekshirish va aybdorlarni javobgarlikka tortish to'g'risida ariza yozing. "
    "Arizada hodisa tafsilotlarini, hujum qilgan shaxsning (agar ma'lum bo'lsa) shaxsini va guvohlarning ismlarini ko'rsating.\n"
    "5. **Tibbiy ko'rikdan o'tish:** Agar jarohatlangan bo'lsangiz, tibbiy ko'rikdan o'ting va barcha tibbiy xulosalarni saqlang. "
    "Ular sudda dalil sifatida ishlatilishi mumkin.\n\n"
    "**O'zbekiston Respublikasi qonunchiligida hujum uchun javobgarlik:**\n\n"
    "* **Ma'muriy javobgarlik:** Agar hujum oqibatida jiddiy jarohatlar yetkazilmagan bo'lsa, aybdorga ma'muriy javobgarlik qo'llanilishi mumkin "
    "(O'zbekiston Respublikasi Ma'muriy javobgarlik to'g'risidagi kodeksining 41-moddasi - \"Mayda bezorilik\").\n"
    "* **Jinoyat javobgarligi:** Agar hujum oqibatida jiddiy jarohatlar yetkazilgan bo'lsa yoki uzoq muddatli sog'liqqa zarar yetkazilgan bo'lsa, "
    "aybdorga jinoyat javobgarligi qo'llanilishi mumkin (O'zbekiston Respublikasi Jinoyat kodeksining 104-106-moddalari - "
    "\"Qasddan badanga og'ir shikast yetkazish\", \"Qasddan badanga o'rtacha og'irlikdagi shikast yetkazish\", \"Qasddan badanga yengil shikast yetkazish\").\n\n"
    "**Muhim eslatma:** Bu ma'lumot faqat ma'lumot berish uchun mo'ljallangan va huquqiy maslahat emas. Har bir holat o'ziga xosdir, "
    "shuning uchun professional huquqiy yordam olish tavsiya etiladi."
)

bot.send_message(CHAT_ID, message, parse_mode='Markdown')

