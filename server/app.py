from fastapi import FastAPI
from server.cloud_env import CloudEnv
from server.models import Action

app = FastAPI()

env = CloudEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: Action):
    return env.step(action.action)