import os

# Define folder structure

folders = [

    "agent_orchestrator",

    "agent_orchestrator/tools",

    "integration_layer",

    "audit_logging",

    "monitoring/grafana",

    "monitoring/prometheus"

]

# Define files to create with optional initial content

files = {

    "agent_orchestrator/__init__.py": "",

    "agent_orchestrator/app.py": '''from fastapi import FastAPI

app = FastAPI(title="KYC Onboarding Agentic AI")

@app.get("/")

def read_root():

    return {"msg": "KYC Agentic AI is running "}

''',

    "agent_orchestrator/agent.py": "",

    "agent_orchestrator/tools/__init__.py": "",

    "agent_orchestrator/tools/ocr_tool.py": "",

    "agent_orchestrator/tools/validation_tool.py": "",

    "agent_orchestrator/tools/compliance_tool.py": "",

    "integration_layer/__init__.py": "",

    "integration_layer/crm_push.py": "",

    "audit_logging/__init__.py": "",

    "audit_logging/logger.py": "",

    "requirements.txt": '''fastapi

uvicorn

langchain==0.2.*

pydantic

python-dotenv

ollama

''',

    "docker-compose.yaml": "",

    "README.md": "# KYC Onboarding Agentic AI\n",

    "TODO.md": "",  # You can copy the TODO.md content I gave above

    ".gitignore": "*.pyc\n__pycache__/\n.env\n"

}

# Create folders

for folder in folders:

    os.makedirs(folder, exist_ok=True)

    print(f"Created folder: {folder}")

# Create files

for file_path, content in files.items():

    with open(file_path, "w") as f:

        f.write(content)

    print(f"Created file: {file_path}")

print(" Project structure setup complete!")
 