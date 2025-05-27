# Smart Study Scheduler

Welcome to the **Smart Study Scheduler**! 

This AI-powered app helps you plan your daily study tasks based on how much time you have, how busy you are, and even how you're feeling that day. It creates a personalized schedule, tracks your progress, and adapts your tasks over time.

---

## Features

- **AI-Powered Scheduling:** Generates a daily study plan tailored to your availability and mood.
- **Task Tracking:** Update your progress by marking completed tasks.
- **Database Integration:** Stores schedules and task completion data in an Amazon RDS PostgreSQL database.
- **AWS Lambda Integration:** Sends you daily emails to collect feedback on completed tasks, which are then fed into an LLM to improve scheduling.
- **Adaptive Learning:** Reminds you to complete unfinished tasks before adding new ones.
- **MCP Server:** Updates the database by syncing completed tasks.

---

## Tech Stack

- Frontend: Streamlit
- Backend: FastAPI
- Database: Amazon RDS PostgreSQL
- AI: OpenAI API via LangChain
- AWS Lambda: For daily email feedback and task completion updates
- MCP Server: For database updates

---

## Getting Started

### Prerequisites

- Python 3.8+
- Amazon RDS PostgreSQL database
- AWS account with Lambda setup
- OpenAI API key

### Installation

1. Clone the repo

   ```bash
   git clone https://github.com/essharmavi/smart_scheduler_app.git
   cd smart_scheduler_app
2. Create and activate a virtual environment
  python -m venv venv
  source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install dependencies
  pip install -r requirements.txt
4. Create a .env file in the root directory and add:
  RDS_POSTGRES_KEY=your_postgres_password
  OPENAI_API_KEY=your_openai_api_key

## Running the App

- Start the backend FastAPI server:

  ```bash
  uvicorn main:app --reload

- Start the Streamlit frontend:
  ```bash
  streamlit run frontend.py

## How to Use

1. Input your available study hours, current workload, and mood.  
2. The app generates a personalized study schedule.  
3. Mark tasks as completed — your progress will be saved.  
4. Receive daily emails (via AWS Lambda) prompting you to update completed tasks.  
5. The app uses that feedback, fed into a Large Language Model, to improve future scheduling.  
6. When choosing the same topic again, the app will check your past progress to suggest new tasks or remind you to finish incomplete ones.

## Future Plans

- Improve adaptive scheduling based on task completion history.  
- Add mobile app integration.  
- Include analytics dashboard to visualize study progress.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit pull requests.

## License

MIT

## Contact

Created by Vishal Sharma — feel free to reach out!




