# 🧠 AI Storage Copilot

An AI-powered storage management assistant that analyzes file usage, detects duplicate and unused files, predicts future storage requirements, and provides intelligent recommendations for cleaning and archiving data safely.

Instead of simply telling users **what is taking up storage**, AI Storage Copilot answers the more useful question:

> **"What should I do about it?"**

---

## 🚀 Problem

Modern computers accumulate large amounts of unnecessary data over time:

* Duplicate files
* Old project backups
* Unused downloads
* Temporary files
* Build artifacts
* Cache files
* Large files that are rarely accessed
* Multiple versions of the same document
* Regeneratable development dependencies

Traditional disk-cleaning tools mostly provide lists of large or old files. They don't understand the **context, importance, or risk** associated with deleting them.

This project aims to build an intelligent storage assistant that can analyze this information and make **explainable, personalized, and safe recommendations**.

---

## 💡 Solution

AI Storage Copilot combines filesystem analysis, machine learning, and an AI agent to provide:

### 📊 Storage Analysis

Understand how storage is distributed across:

* Documents
* Images
* Videos
* Audio
* Projects
* Archives
* Applications
* Temporary files
* Cache
* Development artifacts

### 🔁 Duplicate Detection

Identify:

* Exact duplicate files using file hashes
* Duplicate groups
* Potentially similar files
* Redundant versions of documents and projects

### 💤 Unused File Detection

Identify files based on factors such as:

* Last access time
* Last modification time
* File age
* File size
* File type
* Usage frequency

### 🔮 Storage Prediction

Analyze historical storage usage to predict:

* Future storage consumption
* Storage growth rate
* Estimated time until capacity is reached
* Categories responsible for future growth

Example:

```text
Current storage:       382 GB
Capacity:              512 GB
Current usage:         74%

Estimated growth:      1.2 GB/day

Predicted usage:
30 days:               418 GB
90 days:               490 GB

Estimated capacity:
~108 days
```

### 🤖 Intelligent Recommendations

The system classifies files into categories such as:

```text
KEEP
REVIEW
ARCHIVE
CLEAN
```

Recommendations consider:

* File importance
* File age
* Usage history
* Duplicate status
* File size
* Regeneratability
* Potential deletion risk
* User preferences

---

## ✨ Key Features

* 🔍 Intelligent filesystem scanning
* 📁 File metadata analysis
* 🔐 SHA-256 duplicate detection
* 💤 Unused file detection
* 🧠 AI-powered storage recommendations
* 🔮 Storage growth prediction
* 📦 Archive recommendations
* 🧹 Safe cleanup workflow
* 💬 Natural-language storage assistant
* 🎯 File importance and risk scoring
* 📈 Storage usage visualization
* 🔮 "What-if" storage simulation
* 🛡️ User confirmation before destructive actions
* 🧠 Personalized cleanup preferences

---

## 🧩 AI Assistant

Users can interact with the storage assistant using natural language.

Examples:

```text
"What is taking most of my storage?"

"Find files larger than 2 GB that I haven't used in 6 months."

"What can I safely remove?"

"How can I free 20 GB?"

"When will my storage run out?"

"Show me duplicate files."

"Which folders are growing the fastest?"

"What would happen if I archived my old videos?"
```

The AI agent uses specialized tools to analyze the filesystem and provide evidence-backed recommendations.

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    AI Storage       │
                         │       Agent         │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
             ┌────────────┐  ┌────────────┐  ┌────────────┐
             │  Scanner   │  │  Analyzer  │  │ Predictor  │
             └─────┬──────┘  └──────┬─────┘  └──────┬─────┘
                   │                │                │
                   └────────────────┼────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │      Database       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Recommendation      │
                         │ Engine              │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┼──────────┐
                         ▼          ▼          ▼
                       KEEP      ARCHIVE     CLEAN
```

---

## 📂 Project Structure

```text
ai-storage-copilot/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── config/
│   └── settings.py
│
├── agent/
│   ├── storage_agent.py
│   ├── prompts.py
│   └── tools/
│       ├── scan_tool.py
│       ├── duplicate_tool.py
│       ├── usage_tool.py
│       ├── prediction_tool.py
│       ├── recommendation_tool.py
│       └── cleanup_tool.py
│
├── scanner/
│   ├── filesystem.py
│   ├── metadata.py
│   ├── hashing.py
│   ├── file_classifier.py
│   └── usage_tracker.py
│
├── analyzer/
│   ├── duplicate_detector.py
│   ├── similarity_detector.py
│   ├── unused_detector.py
│   ├── risk_analyzer.py
│   └── storage_analyzer.py
│
├── predictor/
│   ├── feature_engineering.py
│   ├── storage_forecast.py
│   └── capacity_predictor.py
│
├── recommender/
│   ├── recommendation_engine.py
│   ├── scoring.py
│   └── action_planner.py
│
├── database/
│   ├── database.py
│   ├── models.py
│   └── repository.py
│
├── models/
│   ├── file_model.py
│   ├── analysis_model.py
│   ├── prediction_model.py
│   └── recommendation_model.py
│
├── ui/
│   ├── dashboard.py
│   ├── storage_overview.py
│   ├── duplicates.py
│   ├── recommendations.py
│   ├── predictions.py
│   ├── assistant.py
│   └── components/
│
├── services/
│   ├── archive_service.py
│   ├── cleanup_service.py
│   └── scan_service.py
│
├── utils/
│   ├── logger.py
│   ├── file_utils.py
│   ├── date_utils.py
│   └── security.py
│
├── data/
│   ├── scans/
│   ├── history/
│   └── cache/
│
├── tests/
│   ├── test_scanner.py
│   ├── test_duplicates.py
│   ├── test_usage.py
│   ├── test_prediction.py
│   ├── test_recommendations.py
│   └── test_agent.py
│
└── scripts/
    ├── initialize_db.py
    ├── generate_test_data.py
    └── run_scan.py
```

---

## 🔄 System Workflow

```text
1. Scan filesystem
        ↓
2. Extract file metadata
        ↓
3. Calculate hashes
        ↓
4. Store file information
        ↓
5. Detect duplicates
        ↓
6. Analyze file usage
        ↓
7. Calculate file risk/importance
        ↓
8. Predict storage growth
        ↓
9. Generate recommendations
        ↓
10. Explain recommendations using AI
        ↓
11. User reviews recommendations
        ↓
12. User approves cleanup/archive
        ↓
13. Execute safe operation
        ↓
14. Update storage history
```

---

## 🛡️ Safety Philosophy

The system is designed around **recommendation before deletion**.

The AI should never have unrestricted permission to delete files.

Instead:

```text
AI Analysis
     ↓
Recommendation
     ↓
Risk Assessment
     ↓
User Confirmation
     ↓
Cleanup / Archive
```

Important files such as personal documents, photographs, financial records, or active projects should be treated conservatively.

---

## 🧠 Storage Intelligence Score

Each file can receive an intelligence score based on multiple factors:

```text
File age
File size
Access frequency
Modification frequency
Duplicate probability
Regeneratability
File category
Importance
User preferences
```

Example:

```text
old_project_backup.zip

Size:                4.8 GB
Age:                 420 days
Duplicates:          3
Last accessed:       380 days ago
Regeneratable:       No

Recommendation:      ARCHIVE
Confidence:          91%
Potential savings:   9.6 GB
```

---

## 🔮 Storage Forecasting

The system maintains historical storage information and uses it to estimate future requirements.

```text
Historical Usage
       ↓
Feature Engineering
       ↓
Growth Rate Analysis
       ↓
Forecast Model
       ↓
Future Storage Prediction
       ↓
Capacity Warning
```

Example:

```text
⚠️ Storage Alert

Your storage is growing at approximately 1.1 GB/day.

At the current growth rate:

30 days → 415 GB
60 days → 448 GB
90 days → 481 GB

Your storage may reach 90% capacity
in approximately 75 days.
```

---

## 🧪 Development

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-storage-copilot
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env`:

```env
LLM_API_KEY=your_api_key
LLM_BASE_URL=your_base_url
LLM_MODEL=your_model
```

Additional environment variables can be added as the project evolves.

### 5. Initialize the database

```bash
python scripts/initialize_db.py
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🐳 Docker

Build the image:

```bash
docker build -t ai-storage-copilot .
```

Run the application:

```bash
docker run --env-file .env -p 8501:8501 ai-storage-copilot
```

The Streamlit application will be available at:

```text
http://localhost:8501
```

> **Note:** Filesystem access inside Docker requires explicit directory mounting. The application should only receive access to directories that the user intentionally exposes to the container.

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_scanner.py
```

---

## 🛠️ Technology Stack

| Component           | Technology                         |
| ------------------- | ---------------------------------- |
| Frontend            | Streamlit                          |
| Backend             | Python                             |
| AI Agent            | LangChain / LangGraph              |
| LLM                 | NVIDIA NIM / OpenAI-compatible API |
| Database            | SQLite                             |
| Vector Database     | Qdrant                             |
| ML                  | Scikit-learn                       |
| File Analysis       | Python standard library            |
| Document Processing | PyMuPDF / python-docx              |
| Containerization    | Docker                             |
| Testing             | Pytest                             |

---

## 🗺️ Roadmap

### Phase 1 — Storage Scanner

* [x] Project architecture
* [ ] Filesystem scanner
* [ ] Metadata extraction
* [ ] File categorization
* [ ] Hash generation

### Phase 2 — Storage Analysis

* [ ] Exact duplicate detection
* [ ] Unused file detection
* [ ] Large file analysis
* [ ] Development artifact detection
* [ ] Storage analytics

### Phase 3 — Intelligence

* [ ] File importance scoring
* [ ] Cleanup risk scoring
* [ ] AI recommendations
* [ ] Archive recommendations

### Phase 4 — Prediction

* [ ] Historical storage tracking
* [ ] Storage growth analysis
* [ ] Future storage prediction
* [ ] Capacity forecasting
* [ ] What-if simulation

### Phase 5 — AI Agent

* [ ] Natural-language queries
* [ ] Tool-based agent
* [ ] Agent memory
* [ ] Personalized storage preferences
* [ ] Multi-step storage analysis

### Phase 6 — Production & Demo

* [ ] Safe cleanup workflow
* [ ] Archive system
* [ ] Confirmation mechanisms
* [ ] Docker deployment
* [ ] Hackathon demo

---

## 🏆 Hackathon Value Proposition

AI Storage Copilot goes beyond traditional disk-cleaning tools by combining:

**Filesystem Intelligence + Machine Learning + AI Agents + Predictive Analytics**

Instead of simply identifying large files, the system understands:

> **What the files are, how they are being used, how important they may be, what will happen to storage in the future, and what action is safest.**

---

## 📄 License

This project is developed as a hackathon project.
