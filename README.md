# LangChain Prompts Project

A Python-based **LangChain Prompt Engineering and Chatbot Toolkit** that demonstrates how to create, manage, store, and use different types of prompts in AI applications.  
This project includes examples of:

- **Static Prompt UI**
- **Dynamic Prompt UI**
- **Chat Prompt Templates**
- **Console Chatbot**
- **Console Chatbot with Memory**
- **Prompt Generator**
- **JSON-based Prompt Templates**
- **Saved Dynamic Prompt Files**

The project is useful for understanding how prompt templates can be structured, reused, and integrated into chatbot workflows using **LangChain + Python**.


# Project Overview

This project is built to explore and implement multiple prompt-related workflows in **LangChain**.  
Instead of using a single hardcoded prompt, the project demonstrates different prompt handling approaches such as:

- creating **fixed/static prompts**
- generating **dynamic prompts based on user input**
- using **chat prompt templates**
- building **console-based chatbot interactions**
- adding **conversation memory**
- storing prompt templates and generated prompts in **JSON files**

The goal of the project is to make prompt creation and chatbot interaction more modular, reusable, and easier to test.

This repository can be used by:
- students learning **LangChain**
- beginners exploring **prompt engineering**
- developers building **LLM-powered chatbot applications**
- anyone who wants to understand **static vs dynamic prompts** in Python projects

---

# Features

## 1. Static Prompt Handling
A predefined prompt is used for interacting with the model.  
This is useful when:
- the task is fixed
- prompt content does not change frequently
- a reusable instruction template is needed

---

## 2. Dynamic Prompt Generation
Prompts can be created dynamically based on user input, variable fields, or templates stored in JSON.  
This helps when:
- prompt text depends on user choices
- you want customizable AI instructions
- multiple prompt variations are required

---

## 3. Chat Prompt Templates
The project contains support for **chat-style prompt templates**, where prompts can be structured into:
- system instructions
- human/user messages
- assistant placeholders
- reusable template variables

This is useful for chatbot-style conversations.

---

## 4. Console Chatbot
A command-line chatbot implementation is included for interacting with the model directly from the terminal.

Typical use:
- user enters a message in terminal
- prompt is processed
- model generates response
- response is printed back in console

---

## 5. Chatbot with Memory
A memory-enabled chatbot script is also included.  
This allows the chatbot to remember previous messages within the session and produce more context-aware responses.

Benefits:
- better conversation continuity
- follow-up questions become meaningful
- user does not need to repeat previous context

---

## 6. Prompt Storage in JSON
Prompt templates and dynamically created prompt data can be stored in JSON files.  
This makes prompt management easier because:
- prompts can be edited without changing Python code
- templates become reusable
- prompt history or generated prompts can be saved

---

## 7. UI-Based Prompt Utilities
The project contains UI-based scripts for working with prompts.  
These likely allow interaction with static and dynamic prompt systems through a simple interface rather than only terminal-based execution.

---

# Project Structure

Below is the structure of the project:

```bash
LANGCHAIN_PROMPTS/
│
├── used_prompt_file_dynamically/
│   ├── Dynamic_prompt_used_savedJSON.py
│   ├── prompt_generator.py
│   └── template.json
│
├── .env
├── .gitignore
├── chat_prompt_Template.py
├── console_chatbot_with_memory.py
├── console_chatbot.py
├── Dynamic_prompt2_ui.py
├── LICENSE
├── message.py
├── README.md
└── static_prompt_ui.py
