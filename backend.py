from fastapi import FastAPI, HTTPException,File, UploadFile,Response
from dotenv import load_dotenv


from moels import TopicRequest, AudioResponse,NewsRequest,NewsResponse


app = FastAPI()
load_dotenv()



@app.post("/generate-news-audio")
async def generate_news_audio(request: NewsRequest):
    try :
        results ={}

        #Scrape the data

        if request.source_type in ["news", "both"]:
           # scape news data and store in results["news"]
            results["news"] = {"News_Scrapped": "This is from Google news"}

        if request.source_type in ["reddit", "both"]:
            # scrape reddit data and store in results["reddit"]
            results["reddit"] = {"Reddit_Scrapped": "This is from Reddit"}

        news_data = results.get("news", {})
        reddit_data = results.get("reddit", {})


        # Setup LLM Summarizer 

        news_summary = my_function_to_summarize(news_data,reddit_data)

        # Convert Summary to Audio

        audio_path = convert_summary_to_audio(news_summary)

        if audio_path:
            return response,headers,etc
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        else:
            raise HTTPException(status_code=500, detail="Audio generation failed")
