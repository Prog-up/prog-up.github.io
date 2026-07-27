import os

cases_content = {
    "excense": """
### Software Engineering Internship

During this intermediate internship at Excense, I worked on bridging modern AI paradigms with robust enterprise applications.

**Key Contributions:**
- Developed a Universal Windows Platform (UWP) Proof of Concept (PoC) integrating a Model Context Protocol (MCP) server.
- Built an automated testing web service designed to evaluate and ensure the quality of LLM (Large Language Model) interfaces.
- Contributed to the strategic system migration from older frameworks to **.NET 9 (C#)**, ensuring better performance and maintainability.
""",

    "sentientscript": """
### Full-Stack Development Internship

Completed an international internship in Chennai, India, focusing on modern web development and local AI integration.

**Key Contributions:**
- Architected and developed two major full-stack web applications utilizing **Next.js**.
- Integrated the **Ollama SDK** to leverage local AI models seamlessly within the web applications, focusing on low-latency inference and scalable deployment.
""",

    "agrial": """
### Seasonal Employment

During this summer job at Agrial in Douvres-la-Délivrande, I worked on the operational side of the supply chain and retail.

**Key Contributions:**
- Managed warehouse inventory and stock rotation.
- Organized store displays to optimize product visibility and access.
- Handled customer order preparation and logistical tracking.
"""
}

base_dir = "src/assets/cases"

for slug, content in cases_content.items():
    case_dir = os.path.join(base_dir, slug)
    filepath = os.path.join(case_dir, "content.md")
    if os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(content.strip() + "\n")
            print(f"Updated {slug}")

