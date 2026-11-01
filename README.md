# 🔬 ResearchMind – Multi-Agent AI Research System

**ResearchMind** is an AI-powered multi-agent research automation system designed to simplify and automate the research process.

It uses specialized AI agents and LangChain to search the web, scrape relevant content, generate comprehensive research reports, and evaluate the quality of those reports.

Built with Python and Streamlit, ResearchMind demonstrates how multiple AI agents and LLM-powered chains can collaborate to perform an end-to-end research workflow.

## 🚀 Key Features

- **Web Search Agent:** Uses Tavily Search API to discover recent and relevant information from the web.
- **Reader Agent:** Extracts and cleans webpage content using Requests and BeautifulSoup.
- **Writer Chain:** Generates detailed, structured research reports using an LLM.
- **Critic Chain:** Evaluates generated reports, assigns a score out of 10, identifies strengths, and suggests improvements.
- **Interactive Dashboard:** Provides a modern Streamlit interface to monitor the research pipeline.
- **Research Results:** Displays raw search results and scraped content for transparency.
- **Download Reports:** Allows users to download generated research reports in Markdown format.

## 🏗️ System Architecture

ResearchMind follows a sequential multi-agent workflow where each agent or chain performs a specific responsibility.

```text
                  USER INPUT
                      |
                      v
              Research Topic
                      |
                      v
          +----------------------+
          |    Search Agent      |
          |   (Tavily Search)    |
          +----------------------+
                      |
                      v
          +----------------------+
          |     Reader Agent     |
          | (Web Scraping &      |
          |  Content Extraction) |
          +----------------------+
                      |
                      v
          +----------------------+
          |     Writer Chain     |
          | (Research Report     |
          |     Generation)      |
          +----------------------+
                      |
                      v
          +----------------------+
          |     Critic Chain     |
          | (Report Evaluation)  |
          +----------------------+
                      |
                      v
          +----------------------+
          |   Final Research     |
          |       Report         |
          +----------------------+
                      |
                      v
              Download Report
```

## 🧠 Multi-Agent Components

### 1. Search Agent
- Searches the internet using the Tavily Search API.
- Retrieves up to five relevant search results.
- Collects titles, URLs, and content snippets.
- Focuses on finding recent and reliable information.

### 2. Reader Agent
- Receives search results from the Search Agent.
- Identifies a relevant URL for deeper research.
- Uses the custom `scrape_url` tool to extract webpage content.
- Removes unnecessary HTML elements such as scripts, styles, navigation, and footers.
- Extracts clean text for the research process.

### 3. Writer Chain
- Combines search results and extracted webpage content.
- Uses an LLM to generate a detailed research report.
- Organizes the report into:
  - Introduction
  - Key Findings
  - Conclusion
  - Sources

### 4. Critic Chain
- Reviews the generated research report.
- Evaluates the overall report quality.
- Assigns a score out of 10.
- Identifies strengths and areas for improvement.
- Provides a final verdict.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive frontend |
| LangChain | Agent and chain orchestration |
| LangChain Agents | Building specialized AI agents |
| Groq | LLM inference |
| GPT-OSS-120B | Language model |
| Tavily API | Web search integration |
| Requests | HTTP requests |
| BeautifulSoup | Web scraping and HTML parsing |
| Python-dotenv | Environment variable management |
| Rich | Console output formatting |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
ResearchMind/
│
├── app.py                  # Streamlit frontend application
│
├── agent.py                # AI agents and LLM chains
│
├── tool.py                 # Custom web search and scraping tools
│
├── requirements.txt        # Project dependencies
│
├── .env                    # API keys and environment variables
│
├── .gitignore              # Git ignored files
│
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd ResearchMind
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory.

Add the following API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

**Important:** Never expose your API keys or commit your `.env` file to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will be accessible at:

```text
http://localhost:8501
```

## 📦 Requirements

The main dependencies used in this project include:

```txt
streamlit
langchain
langchain-core
langchain-groq
langgraph
requests
beautifulsoup4
tavily-python
python-dotenv
rich
```

## 💡 How to Use

1. Open the ResearchMind application.
2. Enter your desired research topic.
3. Click **Run Research Pipeline**.
4. The Search Agent searches the web for relevant information.
5. The Reader Agent extracts detailed content from a selected webpage.
6. The Writer Chain generates a structured research report.
7. The Critic Chain evaluates the generated report and provides feedback.
8. Review the final report and critic evaluation.
9. Download the research report in Markdown format.

## 📌 Example Research Topics

Try researching the following topics:

- Multi-Agent AI Systems
- Large Language Model (LLM) Agents
- Generative AI Applications
- Retrieval-Augmented Generation (RAG)
- Quantum Computing Breakthroughs
- CRISPR Gene Editing
- Fusion Energy Progress

## 🔮 Future Enhancements

- Implement parallel agent execution for improved performance.
- Add source citations and reference verification.
- Introduce human-in-the-loop approval.
- Implement long-term agent memory.
- Add research history using a database.
- Integrate multiple search providers.
- Implement advanced fact-checking mechanisms.
- Support PDF report generation.
- Improve error handling and retry mechanisms.

## 🔐 Security

- Store API credentials using environment variables.
- Never commit `.env` files to version control.
- Add `.env` and `.venv/` to `.gitignore`.
- Avoid exposing sensitive API information in application logs.

## 👨‍💻 Author

**Divakar B**

MCA Graduate | Java Full Stack Developer | Generative AI Enthusiast

---

⭐ If you find this project interesting, consider giving the repository a star!
