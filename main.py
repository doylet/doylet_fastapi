
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define request model for the function call
class WeatherRequest(BaseModel):
    location: str


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# Your function that GPT will call
@app.post("/get_weather")
def get_weather(data: WeatherRequest):
    location = data.location
    # Dummy response (replace with real API call if needed)
    return {"location": location, "temperature": "22°C", "condition": "Sunny"}


# OpenAI tool definition for function calling
@app.get("/openapi.json")
def openapi_schema():
    return {
        "name": "weather_tool",
        "description": "Get weather info for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name to fetch weather for"
                }
            },
            "required": ["location"]
        }
    }