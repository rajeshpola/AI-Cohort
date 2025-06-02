import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import getPrompts
import json



def getResponse (persona:str, mesage:str):
    load_dotenv();
    #get the Key system is the one you load and user is the one you ask and assistant is the one which Ai gives
    API_Key=os.getenv("GEMINI_KEY");
    print(API_Key);
    
    client = OpenAI(
        api_key=API_Key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    print(getPrompts("Hitesh"));
    
    messages = [{"role":"system","content":getPrompts("Hitesh")}];
    userQuery = input (">");
    print(userQuery);
    messages.append({"role":"user","content":userQuery});
    

    while True:
        print(messages);
        response = client.chat.completions.create(
        model="gemini-2.0-flash",
        #response_format={"type":"json_object"},
        messages=messages,
        max_tokens=150,
    
        )
        print (response.choices[0].message.content);
        # print(messages)
        #converts to String 
        # json_string = json.dumps(response.choices[0].message.content)
        #convets to object 
        #         Json_string = json.dumps({"test": 1})  # '{"test": 1}'
        # parsed = json.loads(json_string)      # Converts back to dict
        # value = parsed["test"]
        # print(value)  
        # Outp
        # parsed = json.loads(json_string)
        #messages.append({"role":"assistant","content":parsed["response"])
        
        messages.append({"role":"assistant","content":response.choices[0].message.content})
        userQuery = input (">");
        # append them 
        messages.append({"role":"user","content":userQuery});


     


getResponse("one","one")