from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
     return {"project": "ŞAŞIRT AI Studio", "status": "running", "version": "0.1.0"}