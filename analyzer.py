from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text):
    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume.

Rules:
- Keep the response concise.
- Do NOT write long paragraphs.
- Use bullet points only.
- Maximum 1 line for each bullet.
- Resume Summary: only 3-4 bullet points.
- Skills: only skill names.
- Resume Score: only one number out of 100.
- ATS Compatibility: only "ATS Friendly" or "Needs Improvement" with one reason.
- Missing Skills: maximum 5 skills.
- Suggestions: maximum 5 short bullet points.

Return in this exact format:

## Resume Summary
- ...
- ...
- ...

## Skills
- Python
- SQL
- Power BI

## Resume Score
85/100

## ATS Compatibility
ATS Friendly
Reason: ...

## Missing Skills
- Pandas
- NumPy
- Tableau

## Suggestions
- Add project metrics.
- Add certifications.
- Improve summary.
- Add GitHub links.
- Include internships.

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text