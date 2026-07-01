import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app=FastAPI()

@app.post("/chat")
def chat(payload:dict):
    print(f"[CHAT]{payload.get('telegramId')}:{payload.get('message')}")
    return {"reply":f"Backend received: {payload.get('message')}","buttons":[]}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=int(os.getenv("PORT",3000)))

 