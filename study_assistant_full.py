import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def run_study_assistant(topic, question):
    explainer = Agent(
        role='Subject Explainer',
        goal='Explain academic topics in simple and engaging language.',
        backstory="You explain concepts clearly with analogies and examples.",
        verbose=False
    )

    qa_agent = Agent(
        role='Question Answerer',
        goal='Answer specific academic questions accurately.',
        backstory="You give direct, informative answers.",
        verbose=False
    )

    quiz_maker = Agent(
        role='Quiz Generator',
        goal='Create short quizzes based on content.',
        backstory="You reinforce learning with quizzes.",
        verbose=False
    )

    task1 = Task(
        description=f"Explain the topic '{topic}' in a student-friendly way.",
        expected_output="A simple explanation of the topic.",
        agent=explainer
    )

    task2 = Task(
        description=f"Answer this question: '{question}' in less than 100 words.",
        expected_output="Short and accurate answer.",
        agent=qa_agent
    )

    task3 = Task(
        description=f"Create 3 multiple-choice questions on the topic '{topic}'.",
        expected_output="3 MCQs with 4 options each and correct answers listed.",
        agent=quiz_maker
    )

    crew = Crew(
        agents=[explainer, qa_agent, quiz_maker],
        tasks=[task1, task2, task3]
    )

    return crew.kickoff()
