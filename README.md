# AutoRefactorAI - Multi-Agent Code Refactoring Crew

**Multi-agent AI workflow** built with **CrewAI** that automatically:
- Analyzes legacy/technical debt code
- Refactors to modern standards (clean architecture, type hints, etc.)
- Generates comprehensive unit tests
- Performs closed-loop review & iteration
- Produces ready-to-PR refactored code

## Core Logic Flow (Long-chain Reasoning + Multi-Agent Collaboration)
1. **Planner Agent** → decomposes task & creates detailed plan
2. **Code Analyst Agent** → deep analysis of tech debt
3. **Refactoring Engineer** → produces refactored code
4. **Test Engineer** → writes pytest + edge cases
5. **Quality Reviewer Agent** → critic & suggests improvements (multiple iterations)
6. **Supervisor Agent** → final verification & approval

**Built as preparation for OpenClaw + MiMo-V2.5 integration.**

## Quick Start
```bash
pip install -r requirements.txt
cp .env.example .env
# Isi OPENAI_API_KEY (atau gunakan Groq/Claude)
python main.py
