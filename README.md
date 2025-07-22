# SoftwareDevAgenticCrew

> **Multi-agent pipeline for end-to-end software delivery, built with [CrewAI](https://github.com/joaomdmoura/crewai).**

SoftwareDevAgenticCrew turns a plain–English feature request into working, multi-file source code.
It does so by orchestrating specialised AI agents—Customer Success, Architecture, Product Ownership, Development, QA and Integration—each with its own objective and YAML-based prompt profile.

---

## ✨ Key Features

| Stage | Crew                      | What it does                                            |
| ----- | ------------------------- | ------------------------------------------------------- |
| 1     | **CustomerServiceCrew**   | Clarifies requirements with the requester (optional).   |
| 2     | **ArchitectCrew**         | Designs high-level architecture blocks.                 |
| 3     | **ProductOwnerCrew**      | Breaks architecture into concrete source files & specs. |
| 4     | **SoftwareDeveloperCrew** | Generates fully-documented code and unit tests.         |
| 5     | **IntegratorCrew**        | Stitches files together and ensures project coherence.  |

### Dual operating modes

* **Interactive mode** – a customer-service agent interviews you until the requirements are crystal-clear.
* **Direct mode** – skip the interview and jump straight to coding.

### Config-as-YAML

Agents, tasks and I/O schemas live under each `crews/<CrewName>/config/` folder, so you can tweak behaviour without touching Python.

### Visual Flow

Running the pipeline draws a Mermaid graph (`crewai_flow.html`) showing every task and dependency—great for slides or docs.

---

## 🗂️ Project layout

```
SoftwareDevAgenticCrew/
├── SoftwareDevFlow.py          # Entrypoint / main Flow definition
├── crews/                      # All crew packages
│   ├── ArchitectCrew/
│   │   ├── crew.py
│   │   └── config/
│   ├── CustomerServiceCrew/
│   ├── IntegratorCrew/
│   ├── ProductOwnerCrew/
│   └── SoftwareDeveloperCrew/
├── crewai_flow.html            # Auto-generated diagram of the full Flow
├── .gitignore
└── LICENSE                     # MIT
```

---

## 🚀 Quick-start

1. **Clone & enter the repo**

   ```bash
   git clone https://github.com/AhmedH777/SoftwareDevAgenticCrew.git
   cd SoftwareDevAgenticCrew
   ```
2. **Create a virtual environment & install deps** (Python ≥ 3.10)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install crewai crewai-tools python-dotenv
   ```
3. **Add your LLM credentials** – create a `.env` file in the repo root:

   ```env
   MODEL=gpt-4o         # or any model supported by CrewAI's LLM wrapper
   API_KEY=sk-...
   ```
4. **Run the pipeline**

   ```bash
   python SoftwareDevFlow.py
   ```

   Follow the CLI prompts:

   * choose *interactive* or *direct* mode
   * enter your preferred programming language
   * describe the feature you want built

Generated source files land in `projectDir/` and the integrated build in `integratedProj/`.

---

## 🧩 Extending & Customising

* **Swap the LLM** – set `MODEL` (e.g. `gpt-4o`, `anthropic/claude-3`) in `.env`.
* **Tune agent personalities** – edit the YAML in `crews/*/config/agents.yaml`.
* **Add tasks** – append new entries in the crew’s `tasks.yaml` and reference them in `crew.py`.
* **Insert new pipeline stages** – inherit from `Flow` in a new file and link it with `@listen` decorators.

---

## 🤝 Contributing

Pull requests are welcome for new tools, agents, or example flows.
Please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License – see [`LICENSE`](LICENSE) for details.
