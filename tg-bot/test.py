import httpx
import asyncio

async def ask_rano(text: str) -> dict:
    url = f"https://api.u2s.uz/rano-ai?savol={text}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Misol uchun ishlatish:
async def main():
    text = input("Savolingizni kiriting: ")
    javob = await ask_rano(text)
    print(javob)

if __name__ == "__main__":
    asyncio.run(main())
