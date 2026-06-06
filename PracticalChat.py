
import google.generativeai as genai 
import requests

Api_key = "Api_key"
# # genai.configure(api_key = Api_key)
# # model = genai.GenerativeModel("gemini-2.5-flash")
# # response =model.generate_content("Explain python loops ")
# # print(response.text)

# # genai.configure(api_key = Api_key)
# # model = genai.GenerativeModel("gemini-2.5-flash")
# # tokens = 0

# # while True:

# #     if tokens == 2:
# #         break

# #     print(f"tokens left : {tokens}")
# #     userinput = input("User:")
# #     response = model.generate_content(userinput)
# #     print(response.text)
# #     tokens +=1

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pypdf import PdfReader

text=""

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

def chunking():
    chunks = text.split("\n\n")
    relevant_chunks =[]

    for chunk in chunks:
        if "interview" in chunk.lower():
            relevant_chunks.append(chunk)

    return relevant_chunks
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={Api_key}"

history = []
while True:
    current_doc = ""
    print("Enter /file to upload a file")
    prompt = input("You:")
    if prompt.lower() == "exit":
        print("AI:bye")
        break

    full_prompt = f""" You are a senior Python mentor.Explain simply.
            Here's the question {prompt}
            only write in short and straight forward and in simple english"""

    if prompt.lower().startswith("/sumrize"):
        full_prompt = f"""You are going to sumrize this {prompt}
        this should contain all the important infomation about the questions or paragraph """ 
    elif prompt.lower().startswith("/code"):
        full_prompt = f""" You are going to code about the question that is given to you don't write anything else or explain anything just a simple code snippet that will showcase the answer 
        here's the question {prompt} clearly read the quesiton and write a code simple snippet for this question. """

    elif prompt.lower().startswith("/explain"):
        full_prompt = f"""Deeply explain this topic {prompt} with proper explaination and don't write the things that are not related to the question """
    elif prompt.lower().startswith("/file"):
        text = importtingFile()
        chunk = chunking()
        prompting = ""
        full_prompt = f""" analyze this file chunk {chunk} and there will be questions from this file and answer only the answer from this file and don't overwrite about the question
        Here's the question {prompt}"""
        current_doc = chunk
    else:
        full_prompt = f"Analyze the history for the context of the chat here's the question {prompt}"

    combined = f"history :{history}if file is not attached then here should be nothing:{current_doc} question:{full_prompt}"
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
        "content": prompt
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


