from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
import pandas as pd
import matplotlib.pyplot as plt
from fastapi.responses import FileResponse
from database import get_db
from models import EmotionData, User
from auth import get_current_user

router = APIRouter()

# Track emotion endpoint
@router.post("/track-emotion/")
def track_emotion(emotion: str, db: Session = Depends(get_db), current_user: User = Security(get_current_user)):
    # Save the emotion to the database
    emotion_entry = EmotionData(user_id=current_user.id, emotion=emotion)
    db.add(emotion_entry)
    db.commit()
    db.refresh(emotion_entry)
    return {"message": "Emotion tracked successfully"}

# Get emotion statistics endpoint
@router.get("/emotion-statistics/")
def get_emotion_statistics(db: Session = Depends(get_db), current_user: User = Security(get_current_user)):
    # Filter data for the current user
    user_emotions = db.query(EmotionData).filter(EmotionData.user_id == current_user.id).all()
    if not user_emotions:
        raise HTTPException(status_code=404, detail="No emotions found for user")
    
    # Create a simple statistics chart
    emotions = [entry.emotion for entry in user_emotions]
    df = pd.DataFrame(emotions, columns=["emotion"])
    emotion_counts = df["emotion"].value_counts()
    chart_path = f"/mnt/data/user_{current_user.id}_emotion_chart.png"
    plt.figure(figsize=(10, 6))
    emotion_counts.plot(kind="bar")
    plt.title("Emotion Tracking Statistics")
    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.savefig(chart_path)
    plt.close()

    return FileResponse(chart_path)
