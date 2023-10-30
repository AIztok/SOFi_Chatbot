# SOFi_Chatbot
## Intro / Motivation
The Chatbot was done as part of a course on finite element analysis of structures using the SOFiSTiK software package, especially their language cadinp. The chatbot should show the future of working with the software with a LLM (large language model) "co-pilot". 
The database is continuously expanded by the author.

[SOFi_Chatbot](https://sofichatbot.streamlit.app/)

## Data
The Chatbot has access to different Teddy Examples (see Data Folder):
- Examples provided by the Author
- Examples provided by Sofistik in their Software
- Handbooks from Sofistik (PDFs simply transformed into txt files using pdfplumber library)
The author claims no ownership over the examples and handbooks from SOFiSTiK. As also of his own examples - the data can be used freely.

## Chat Engine
Currently the used model is GPT-4 (however, might be switches back to 3.5-turbo due to financial reasons :))
The chat-engine from [LlamaIndex](https://www.llamaindex.ai/): [context](https://gpt-index.readthedocs.io/en/stable/examples/chat_engine/chat_engine_context.html?ref=blog.streamlit.io)

## Source
The chatbot is based on the [Streamlit Blog Example App](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/?_hsmi=273646914&_hsenc=p2ANqtz--0kq-uFIx10Lo-lJmaxDlBAyTAignYTtHUexrA0VcTKQpqq1FlHXt5IxRxI6rT5obi5-AlBdYSQtjhejThyYgPtgIuKA)

## Futher information
Interesting videos from [Diego](https://www.youtube.com/@DiegoApellaniz)
[Einführung in Sofistik und GPT-4: Unterhaltung mit dem FEM-Modell](https://www.youtube.com/watch?v=syDjDY5DUfM&ab_channel=DiegoApell%C3%A1niz)
[Introduction to the OpenAI API - Programming a Chatbot to generate Sofistik models](https://www.youtube.com/watch?v=6-hzB0nTKX4&ab_channel=DiegoApell%C3%A1niz)
