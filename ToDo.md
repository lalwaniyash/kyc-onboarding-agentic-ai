# TODO — KYC Onboarding Agentic AI

🗺️ Development Flow (Step-by-step)

---

### Step 1 → Basic Setup

- [ ] Create repo and clone locally

- [ ] Add FastAPI + LangChain 0.2.x + Ollama + Redis (later) + PostgreSQL (later)

- [ ] Write Docker Compose (for future)

- [ ] Verify http://localhost:8000/docs working

---

### Step 2 → Agent Orchestrator Base

- [ ] Build /agent_orchestrator/app.py

- [ ] Add LangChain initialize_agent()

- [ ] Add Ollama LLaMA 3 model

- [ ] Build simple agent with dummy tool (example “say_hello”)

**Goal:**

Agent with one dummy tool running

---

### Step 3 → OCR Tool

- [ ] Add /agent_orchestrator/tools/ocr_tool.py

- [ ] Use Azure Form Recognizer API (preferred), fallback Tesseract

- [ ] Input: PDF / JPG KYC docs

- [ ] Output: Extracted text in JSON

**Goal:**

Agent calls ocr_tool → text comes

---

### Step 4 → Validation Agent & Tool

- [ ] /agent_orchestrator/tools/validation_tool.py

- [ ] PAN validate API hit

- [ ] Aadhaar checksum verify

- [ ] Business rules add

**Goal:**

Agent says: "PAN valid", "Aadhaar valid"

---

### Step 5 → Compliance Tool

- [ ] /agent_orchestrator/tools/compliance_tool.py

- [ ] PEP/AML check (mock first)

- [ ] Output: risk_level pass/low/medium/high

**Goal:**

Agent says: "Customer is low-risk"

---

### Step 6 → Integration Layer

- [ ] /integration_layer/crm_push.py

- [ ] Onboarding complete → data CRM / Core banking

**Goal:**

End-to-end flow → CRM push

---

### Step 7 → Audit Logging

- [ ] /audit_logging/logger.py

- [ ] Log agent actions + tool responses in PostgreSQL

- [ ] WORM storage enabled

**Goal:**

Audit trail generated

---

### Step 8 → Monitoring

- [ ] /monitoring/ Grafana + Prometheus config

- [ ] Track agent latency, errors

**Goal:**

Grafana dashboard active

---

🚀 Final Flow:

1️⃣ User uploads KYC →

2️⃣ API Gateway →

3️⃣ Auth verified →

4️⃣ Agent starts →

5️⃣ OCR tool →

6️⃣ Validation tool →

7️⃣ Compliance tool →

8️⃣ CRM push →

9️⃣ Immutable audit log →

🔟 Monitoring dashboard

---

**Version:** 2025-06-18
