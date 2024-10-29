# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, Diary
from schemas import RegisterUser, LoginUser, DiaryEntry
from utils import generate_image, image_to_blob

app = FastAPI()

# 초기화
init_db()

# DB 세션 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 회원가입
@app.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    new_user = User(username=user.username, password=user.password, 
                    appearance=user.appearance, art_style=user.art_style)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully!"}

# 로그인
@app.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username, User.password == user.password).first()
    if db_user:
        return {"message": "Login successful!", "user_id": db_user.id}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials.")

# 일기 생성
@app.post("/create_diary")
def create_diary(diary: DiaryEntry, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == diary.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    img = generate_image(db_user.appearance, db_user.art_style)
    img_blob = image_to_blob(img)

    new_diary = Diary(user_id=diary.user_id, date=diary.date, content=diary.content, image=img_blob)
    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return {"message": "Diary created successfully!"}

# 특정 날짜의 일기 불러오기
@app.get("/get_diary/{date}")
def get_diary(date: str, user_id: int, db: Session = Depends(get_db)):
    diary = db.query(Diary).filter(Diary.date == date, Diary.user_id == user_id).first()
    if diary:
        return {
            "date": date,
            "content": diary.content,
            "image": diary.image  # 이미지 데이터를 반환하는 방법은 조정 가능
        }
    else:
        raise HTTPException(status_code=404, detail="Diary not found.")
