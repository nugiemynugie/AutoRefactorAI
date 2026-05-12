import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",        # Bisa diganti "claude-3-5-sonnet" dll
    temperature=0.2
)

# ================== AGENTS ==================
planner = Agent(
    role="Senior Software Architect & Planner",
    goal="Buat rencana refactoring yang detail dan efisien",
    backstory="Anda adalah arsitek senior dengan 15 tahun pengalaman modernisasi codebase besar.",
    verbose=True,
    llm=llm,
    allow_delegation=False
)

analyst = Agent(
    role="Code Analyst & Tech Debt Detective",
    goal="Temukan semua tech debt, code smell, dan area improvement",
    backstory="Anda ahli mendeteksi masalah kode tersembunyi dan memberikan rekomendasi arsitektur.",
    verbose=True,
    llm=llm
)

refactorer = Agent(
    role="Senior Refactoring Engineer",
    goal="Menulis ulang kode menjadi clean, modern, dan maintainable",
    backstory="Anda master refactoring yang selalu mengikuti best practices terbaru.",
    verbose=True,
    llm=llm
)

tester = Agent(
    role="Test Engineer",
    goal="Menulis unit test lengkap dengan pytest",
    backstory="Anda sangat ketat dalam coverage testing dan edge cases.",
    verbose=True,
    llm=llm
)

reviewer = Agent(
    role="Principal Code Reviewer",
    goal="Melakukan review mendalam dan meminta perbaikan jika perlu",
    backstory="Anda reviewer paling keras di perusahaan FAANG.",
    verbose=True,
    llm=llm
)

supervisor = Agent(
    role="Project Supervisor",
    goal="Memastikan semua output berkualitas tinggi dan siap di-PR",
    backstory="Anda supervisor yang mengawasi seluruh workflow agentic.",
    verbose=True,
    llm=llm
)

# ================== TASKS ==================
task1 = Task(
    description="Buat rencana refactoring lengkap untuk file berikut:\n\n{code}",
    expected_output="Rencana refactoring yang detail dan langkah-langkah prioritas",
    agent=planner
)

task2 = Task(
    description="Analisis tech debt dan berikan rekomendasi arsitektur",
    expected_output="Laporan analisis tech debt yang lengkap",
    agent=analyst
)

task3 = Task(
    description="Refactor kode sesuai rencana dan best practices",
    expected_output="Kode yang sudah direfactor sepenuhnya",
    agent=refactorer
)

task4 = Task(
    description="Buat unit test lengkap dengan pytest",
    expected_output="File test yang komprehensif",
    agent=tester
)

task5 = Task(
    description="Review keseluruhan hasil dan berikan feedback jika perlu",
    expected_output="Review final + approval atau perbaikan",
    agent=reviewer
)

# ================== CREW ==================
crew = Crew(
    agents=[planner, analyst, refactorer, tester, reviewer, supervisor],
    tasks=[task1, task2, task3, task4, task5],
    process=Process.sequential,   # long-chain reasoning
    verbose=2,
    memory=True
)

# ================== RUN ==================
if __name__ == "__main__":
    print("🚀 AutoRefactorAI Multi-Agent Crew Started...\n")
    
    # Contoh legacy code (bisa diganti dengan file kamu)
    legacy_code = """
# Legacy code example
def process_data(x):
    if x > 100:
        return "big"
    else:
        return "small"
"""

    result = crew.kickoff(inputs={"code": legacy_code})
    print("\n✅ FINAL RESULT:")
    print(result)
