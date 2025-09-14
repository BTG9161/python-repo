#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 12:39:38 2025

@author: bhupatejassingh
"""

import os
from google import genai
from dotenv import load_dotenv



load_dotenv(dotenv_path = "/Users/bhupatejassingh/aiagent/.env")

API = os.getenv("GEMINI_API_KEY")

#print(API)
  
while True:  
    m= input('>>> ')
    client = genai.Client(api_key = API)
    
    x=client.models.generate_content(model= 'gemini-2.0-flash-001', contents= m)
    
    print(x.text)
    
    if m=='exit':
        break







