from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class SourceType(str, Enum):
    NEWS = "news"
    REDDIT = "reddit"
    BOTH = "both"


class Topic(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    source_type: SourceType = SourceType.BOTH


class AudioRequest(BaseModel):
    topics: List[str] = Field(..., min_length=1, max_length=5)
    source_type: SourceType = SourceType.BOTH


class AudioResponse(BaseModel):
    audio_url: str
    topics_analyzed: List[str]
    source_type: SourceType
    duration: Optional[float] = None


class TopicResponse(BaseModel):
    topic: str
    sources: List[dict]
    summary: Optional[str] = None
    sentiment: Optional[str] = None