











from fastapi import FastAPI, Query
import requests
import uvicorn

app = FastAPI()

@app.get("/", tags=["root"])
async def read_root():
    """
    Welcome to the HTTP SIAM API SERVER!

    This endpoint serves as the root of the API.
    """
    return {"message": "Welcome to HTTP SIAM API SERVER :)", }

@app.get('/api/nagad/hulf', tags=["nagad"])
def siam(no: str = Query(default=None, description="The phone number")):
    if not no:
        return {"message": "Please enter a phone number | Parametere !", "developer":"Team Ex !"}

    url = f"https://app.mynagad.com/api/user/check-user-status-for-log-in?msisdn={no}"

    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1152",
        "X-KM-DEVICE-FGP": "172A62186810D06720FE398BB2C4137F45D27D2D5BE1D848FAAAF38A1850BA17",
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01",
        "Host": "app.mynagad.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }

    response = requests.get(url, headers=headers)
    
    name = response.json()["name"]
    userid = response.json()["userId"]  
    status = response.json()["status"]
    userType = response.json()["userType"]
    rbBase = response.json()["rbBase"]
    authTokenInfo = response.json()["authTokenInfo"]
    verificationStatus = response.json()["verificationStatus"]
    executionStatus = response.json()["executionStatus"]
    
    result = {
        "NAME": name,
        "UserID": userid,
        "Status": status,
        "UserType": userType,
        "rbBase": rbBase,
        "authTokenInfo": authTokenInfo,
        "verificationStatus": verificationStatus,
        "executionStatus": executionStatus
    }

    # Additional information
    result["Owner"] = "Team Ex"
    
    return result

if name == "main":
    uvicorn.run(app, host="0.0.0.0", port=81)