# 🕵️ Web Research & Report Generator

This project automates the process of researching a topic from the web and generating a well-structured, factual report using AI agents powered by [CrewAI](https://github.com/joaomdmoura/crewAI). It uses a researcher agent to find trustworthy sources and a scraper agent to extract content and compile it into a markdown-formatted report.

### 🔍 Features

- Web search using **Serper.dev API**
- Web scraping via **Firecrawl**
- Report generation using **Gemini 2.5 Flash** via CrewAI
- Fully automated agent collaboration
- Simple **Streamlit UI** for user interaction

### Demo
[![Watch the demo]](https://youtu.be/B1h4NpqzXkU)

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

### 🚀 How to Run the Project

1. **Clone the repository**
   Open your terminal and run:

   ```bash
   git clone https://github.com/HamnaCh456/Report_writer
   
2. **Install dependencies**
   Make sure you have Python ≥ 3.8 installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add the following keys:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   SERPER_API_KEY=your_serper_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

4. **Run the Streamlit app**
   Use the following command to start the app:

   ```bash
   streamlit run main.py
   ```

5. **Use the App**

   * Enter a product, topic, or company name in the input field.
   * Click **"Generate Report"**.
   * The AI agents will search, scrape, and compile a clean report directly in the interface.
