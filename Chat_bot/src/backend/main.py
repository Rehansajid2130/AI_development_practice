from email import message
from enum import unique
from fastapi import FastAPI
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pypdf import PdfReader
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Replymessage = ""
RecivedMessage =""
ID = 0
@app.post('/chat')
def chat(data: dict,RecivedMessage):

    RecivedMessage = data.get("message","")
    Aireply = CallingAi()
    reply = {Replymessage:f"{Aireply}",id:ID}
    return {
        "reply":reply
    }

text=""
stop_words = [
    "how",
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "for",
    "to",
    "of",
    "in",
    "should",
    "can",
    "i",
    "?",
    ".",
    "!",
    "and",
]

def importtingFile():
    text = ""
    Tk().withdraw()
    file_path = askopenfilename()
    if file_path.endswith(".txt"):
        with open(file_path, "r" , encoding="utf-8") as file:
          text = file.read()
        print("txt_file")
    elif file_path.endswith(".pdf"):
        print("pdf_file")
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    else:
        print("No file")
    return text

def chunking(prompt):
    text = importtingFile()
    chunks = text.split("\n")
    question = prompt.lower()
    words = question.split()

    keywords = []

    for word in words:
        if word not in stop_words:
            keywords.append(word)

    relevant_chunks =[]
    for chunk in chunks:
        for word in keywords:
            if word.lower() in str(keywords).lower():
                relevant_chunks.append(chunk)
                break
    return relevant_chunks



def CallingAi():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={Api_key}"

    history = []
    while True:
        current_doc = ""
        print("Enter /file to upload a file")
        prompt = RecivedMessage
        if prompt.lower() == "exit":
            print("AI:bye")
            break

        if prompt.lower().startswith("/sumrize"):
            full_prompt = f"""You are going to sumrize this {prompt}
            this should contain all the important infomation about the questions or paragraph """ 
        elif prompt.lower().startswith("/code"):
            full_prompt = f""" You are going to code about the question that is given to you don't write anything else or explain anything just a simple code snippet that will showcase the answer 
            here's the question {prompt} clearly read the quesiton and write a code simple snippet for this question. """

        elif prompt.lower().startswith("/explain"):
            full_prompt = f"""Deeply explain this topic {prompt} with proper explaination and don't write the things that are not related to the question """
        elif prompt.lower().startswith("/file"):
            chunk = chunking(prompt)
            full_prompt = f""" analyze this file chunk {chunk} and there will be questions from this file and answer only the answer from this file and don't overwrite about the question
            Here's the question {prompt}"""
            current_doc = chunk
        else:
            full_prompt = f"Analyze the history if there is for the context of the chat here's the question {prompt}"

        combined = f"history file is this but if there is nothing in it so don't mention it:{history} if there is a response already answered before then don't mention anything about it and generate the answer but in different way or write a summary version of it. if there is a content of the file then use the file to answer the question and if you are using the content of the file always say 'According to the attached file '{current_doc} question:{full_prompt}"
        data = {
            "contents" :[
                {

                "parts": [
                    {
                        "text": combined
                    }

                ]
                }
            ]
        }
        response = requests.post(
            url,
            json=data
        )
        history.append({
            "role":"user",
            "content": prompt,
            "file_content":chunk
        })

        if response.status_code == 200:
            result = response.json()
            reply = result["candidates"][0]["content"]["parts"][0]["text"]
            print("AI:",reply)

            history.append({
                "role":"assistant",
                "content": reply
            })

        else:
            result = response.json()
            reply = result["error"]["message"]
            print("There's error")
            print(reply)

    return reply


