from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

class Config(BaseModel):
    openai_api_key: Optional[str] = Field(None, min_length=20)
    openai_model: str = "gpt-3.5-turbo"
    max_file_size_mb: int = Field(200, gt=0, le=500)
    temperature: float = Field(0.0, ge=0.0, le=2.0)
    debug: bool = False

def load_config() -> Config:

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    temperature = float(os.getenv("OPENAI_TEMPERATURE", "0.0"))
    max_size = int(os.getenv("MAX_FILE_SIZE_MB", "200"))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    # Create config with all values at once
    config = Config(
        openai_api_key=api_key,
        openai_model=model,
        temperature=temperature,
        max_file_size_mb=max_size,
        debug=debug
    )
    
    return config