from reportlab.pdfgen import canvas
import os

os.makedirs("sample_folder", exist_ok=True)

files = {
    "cricket.pdf": """
    Cricket is a popular sport played between two teams.
    Each team has eleven players.
    """,

    "artificial_intelligence.pdf": """
    Artificial Intelligence allows machines to perform human-like tasks.
    AI is used in NLP, computer vision, and robotics.
    """,

    "machine_learning.pdf": """
    Machine Learning is a branch of AI.
    It learns patterns from data.
    """,

    "python_basics.pdf": """
    Python is a programming language used in AI,
    automation, and data science.
    """
}


for filename, text in files.items():
    path = os.path.join("sample_folder", filename)

    pdf = canvas.Canvas(path)

    y = 750
    for line in text.split("\n"):
        pdf.drawString(50, y, line)
        y -= 20

    pdf.save()

print("PDFs created")