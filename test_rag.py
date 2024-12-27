from query_data import query_rag
from langchain_community.llms.ollama import Ollama

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

# Define test cases based on resume content
def test_masters_degree():
    assert query_and_validate(
        question="What degree is Krutik pursuing at Rochester Institute of Technology?",
        expected_response="Master of Science in Data Science",
    )

def test_gpa():
    assert query_and_validate(
        question="What is Krutik's current CGPA?",
        expected_response="4.00/4.00",
    )

def test_data_engineer_experience():
    assert query_and_validate(
        question="How many years of experience does Krutik have as a Data Engineer?",
        expected_response="3 years",
    )

def test_etl_pipeline_project():
    assert query_and_validate(
        question="Which tools were used in Krutik's ETL pipeline project?",
        expected_response="AWS Lambda, Glue, Redshift, SQL, Python",
    )

def test_dashboard_processing_time():
    assert query_and_validate(
        question="What was the reduction in processing time achieved with real-time dashboards?",
        expected_response="from 2 hours to 1 minute",
    )

def test_fraudulent_job_detection():
    assert query_and_validate(
        question="What F1 score did Krutik achieve in his fraudulent job posting detection project?",
        expected_response="0.77",
    )

def test_sql_tools():
    assert query_and_validate(
        question="What data analysis tools does Krutik have experience with?",
        expected_response="SQL, Talend(ETL), Excel",
    )

def test_key_technical_skills():
    assert query_and_validate(
        question="List Krutik's main technical skills.",
        expected_response="Python, SQL, Java, Data Science pipeline, Statistics, Cloud Computing, Machine Learning, NLP, Business Analytics, Web & App Development",
    )

def test_certifications():
    assert query_and_validate(
        question="Which certifications has Krutik completed?",
        expected_response="Microsoft Certified: Power BI Data Analyst Associate, IBM Machine Learning Essentials, Data Mining – NPTEL, Python Specialization from University of Michigan",
    )

def test_stakeholder_engagement():
    assert query_and_validate(
        question="What skill does Krutik demonstrate in client meetings?",
        expected_response="Stakeholder engagement and communication",
    )

def test_cloud_tools():
    assert query_and_validate(
        question="What cloud tools does Krutik have experience with?",
        expected_response="AWS (EC2, S3, Redshift, Lambda, Glue)",
    )

def test_data_quality_improvement():
    assert query_and_validate(
        question="What percentage improvement did Krutik achieve in data quality through analysis?",
        expected_response="36%",
    )

# Function for querying and validating
def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = Ollama(model="mistral")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )
