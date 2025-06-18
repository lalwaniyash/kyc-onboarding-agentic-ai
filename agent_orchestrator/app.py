from fastapi import FastAPI

app = FastAPI(title="KYC Onboarding Agentic AI")

@app.get("/")

def read_root():

    return {"msg": "KYC Agentic AI is running "}

