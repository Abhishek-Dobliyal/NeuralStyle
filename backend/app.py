""" Required Imports """
import os

import uvicorn
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response


import nst_model


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_images(contentImage: UploadFile = File(...),
                        styleImage: UploadFile = File(...),
                        epochs: int = Form(...),
                        contentWeight: float = Form(...),
                        styleWeight: float = Form(...)):

    content_img_name, style_img_name = contentImage.filename, styleImage.filename
    with open(content_img_name, "wb") as content, open(style_img_name, "wb") as style:
        content_img = await contentImage.read()
        style_img = await styleImage.read()

        content.write(content_img)
        style.write(style_img)

    model = nst_model.NST(content_img_name, style_img_name, epochs=epochs,
                        content_weight=contentWeight, style_weight=styleWeight)

    model.generate_stylized_img()
    for file in (content_img_name, style_img_name):
        os.remove(file)
    return {"status_code": 200, "loss": model.loss}

@app.get("/result", response_class=Response)
def get_stylized_image():
    with open("stylized.jpg", "rb") as img:
        image_bytes = img.read()

    os.remove("stylized.jpg")
    return Response(content=image_bytes, media_type="image/jpg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
