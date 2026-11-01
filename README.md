# 🔬 ResearchMind – Multi-Agent AI Research System

ResearchMind is an AI-powered multi-agent research automation system that uses specialized AI agents to search the web, extract detailed information, generate comprehensive research reports, and evaluate the quality of the generated reports.

Built using **Python, Streamlit, and LangChain**, ResearchMind automates the research workflow through four specialized components working together in a sequential pipeline.

## 🚀 Features

- **Search Agent:** Searches the web for recent, reliable, and relevant information about a given research topic.
- **Reader Agent:** Identifies relevant URLs, scrapes web pages, and extracts detailed content for deeper research.
- **Writer Chain:** Generates a structured and comprehensive research report using the collected information.
- **Critic Chain:** Reviews the generated report and provides feedback on its quality, accuracy, and completeness.
- **Interactive Dashboard:** Provides a clean, modern Streamlit interface with real-time pipeline status indicators.
- **Raw Research Outputs:** Allows users to inspect search results and scraped content.
- **Report Download:** Download the final research report in Markdown (`.md`) format.

## 🏗️ System Architecture

ResearchMind follows a sequential multi-agent architecture in which each component performs a specialized task.

```text
              User Input
                  |
                  v
          Research Topic
                  |
                  v
          +---------------+
          |  Search Agent |
          +---------------+
                  |
                  v
          +---------------+
          |  Reader Agent |
          +---------------+
                  |
                  v
          +---------------+
          |  Writer Chain |
          +---------------+
                  |
                  v
          +---------------+
          |  Critic Chain |
          +---------------+
                  |
                  v
          +---------------+
          | Final Research|
          |     Report    |
          +---------------+
                  |
                  v
            Download Report
```

## 🧠 Agent Responsibilities

| Component | Responsibility |
|---|---|
| Search Agent | Finds recent and reliable web information. |
| Reader Agent | Scrapes relevant web pages and extracts detailed content. |
| Writer Chain | Converts research material into a structured report. |
| Critic Chain | Evaluates the report and provides improvement feedback. |

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Framework:** LangChain
- **Agent Architecture:** Multi-Agent AI Workflow
- **Web Scraping:** Requests, BeautifulSoup
- **LLM Integration:** LLM APIs configured in the agent and chain modules
- **Styling:** Custom CSS
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
ResearchMind/
│
├── app.py                  # Streamlit application
├── agents.py               # Agent and chain definitions
├── requirements.txt        # Project dependencies
├── .env                    # API keys and environment variables
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

*Note: Update the filenames above if your actual project structure differs.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd ResearchMind
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows:**
```bash
.venv\Scripts\activate
```

** macOS / Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add the API credentials required by your configured LLM provider and search tools.

```env
GROQ_API_KEY=your_groq_api_key
```

Add any additional API keys required by your implementation.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 💡 How to Use

1. Launch the ResearchMind application.
2. Enter your research topic in the input field.
3. Click **Run Research Pipeline**.
4. The Search Agent gathers relevant information from the web.
5. The Reader Agent scrapes selected resources for detailed content.
6. The Writer Chain generates a comprehensive research report.
7. The Critic Chain reviews the generated report and provides feedback.
8. View the final research report and download it as a Markdown file.

## 📌 Example Research Topics

You can explore topics such as:

- Large Language Model (LLM) Agents
- Multi-Agent AI Systems
- Quantum Computing Breakthroughs
- CRISPR Gene Editing
- Fusion Energy Progress
- Generative AI Applications
- Retrieval-Augmented Generation (RAG)

## 🔮 Future Enhancements

- Implement parallel agent execution to improve research efficiency.
- Add source citations and references to generated reports.
- Introduce human-in-the-loop review and approval.
- Add persistent research history using a database.
- Implement agent memory for context retention.
- Add PDF report generation.
- Integrate additional search providers.
- Implement more advanced report evaluation and fact-checking mechanisms.

## 🔐 Security

- Store API keys in environment variables.
- Never commit `.env` files or API credentials to GitHub.
- Add `.env` and `.venv/` to `.gitignore`.

## 👨‍💻 Author

**Divakar B**

MCA Graduate | Java Full Stack Developer | Generative AI Enthusiast

---

⭐ If you find this project interesting, consider giving the repository a star!
