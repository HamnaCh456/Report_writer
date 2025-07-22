# 🕵️ Web Research & Report Generator

This project automates the process of researching a topic from the web and generating a well-structured, factual report using AI agents powered by [CrewAI](https://github.com/joaomdmoura/crewAI). It uses a researcher agent to find trustworthy sources and a scraper agent to extract content and compile it into a markdown-formatted report.

### 🔍 Features

- Web search using **Serper.dev API**
- Web scraping via **Firecrawl**
- Report generation using **Gemini 2.5 Flash** via CrewAI
- Fully automated agent collaboration
- Simple **Streamlit UI** for user interaction

### 📦 How It Works

1. User enters a topic (e.g. a product or company).
2. A Researcher Agent finds highly relevant source.
3. A Scraper Agent extracts content from that source and writes a clean, cited report.
4. The report is displayed in the Streamlit interface.

### 🧠 Agents

- **Researcher Agent**: Searches for official documentation related to the topic.
- **Scraper Agent**: Scrapes and compiles information only from the selected URL.

### 💻 Tech Stack

- Python
- Streamlit
- CrewAI
- Serper.dev API
- Firecrawl API
- Gemini API

### 🚀 How to Run

1. Clone this repo.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
````

3. Set your API keys in a `.env` file:

   ```
   GEMINI_API_KEY=your_gemini_key
   SERPER_API_KEY=your_serper_key
   FIRECRAWL_API_KEY=your_firecrawl_key
   ```
4. Run the app:

   ```bash
   streamlit run main.py
 

---


