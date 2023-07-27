from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def getDashboard():
    return {"message": "Dashboard Page "}
