import httpx

async def ask_rano(text: str) -> dict:
    url = f"https://api.u2s.uz/rano-ai?savol={text}"
    timeout = httpx.Timeout(15.0)  # 15 sekund kutadi

    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            res = await client.get(url)
            res.raise_for_status()
            return res.json()['javob']
        except httpx.ReadTimeout:
            return {"javob": "⏳ Server javob bermadi. Keyinroq urinib ko'ring."}
        except httpx.HTTPError as e:
            return {"javob": f"❗ HTTP xato: {str(e)}"}
        except Exception as e:
            return {"javob": f"❗ Noma'lum xato: {str(e)}"}
