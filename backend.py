from fastapi import FastAPI, HTTPException,File, UploadFile,Response
from dotenv import load_dotenv


from models import AudioRequest, AudioResponse


app = FastAPI()
load_dotenv()



@app.post("/generate-audio")
async def generate_audio(request: AudioRequest):
    try :
        results = {}

        if request.source_type in ["news", "both"]:
            results["news"] = {"News_Scrapped": "This is from Google news"}

        if request.source_type in ["reddit", "both"]:
            results["reddit"] = {"Reddit_Scrapped": "This is from Reddit"}

        news_data = results.get("news", {})
        reddit_data = results.get("reddit", {})

        news_summary = f"Summary for {', '.join(request.topics)}"

        audio_path = f"/audio/{hash(news_summary)}.mp3"

        return AudioResponse(
            audio_url=audio_path,
            topics_analyzed=request.topics,
            source_type=request.source_type,
            duration=30.0
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    