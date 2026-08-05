### AI Integration & Full-Stack Engineering at Sentient Scripts

**Overview**  
During a 5-month full-stack development internship at **Sentient Scripts** in Chennai, India—in collaboration with the **AI-Driven Discovery Hub** at SRMIST—I built and deployed two AI-powered web applications. My work focused on integrating local Large Language Models (LLMs), training computer vision models, optimizing API streaming performance, and containerizing microservices for cloud deployment.

### Projects & Technical Highlights

#### 1. Streaming LLM Web Application (GenAI & Real-Time APIs)
- **Local Model Serving**: Evaluated Rasa NLU for structured conversational pipelines before migrating to **Ollama** and **Mistral** for flexible local text generation.
- **Microservice Architecture**: Built a Python Flask backend wrapping the Ollama SDK to handle model inference requests from a Next.js (TypeScript) frontend.
- **Latency & Streaming Optimization**: Solved gateway timeout issues caused by long LLM response generation by implementing chunked HTTP streaming (Server-Sent Events). Token-by-token streaming brought initial UI response time down to near-zero and eliminated Next.js request timeouts.

#### 2. Feature-Specific Computer Vision Pipeline
- **Model Exploration & Pivot**: Benchmarked **YOLOv8** for target element detection in images, identifying limitations in fine-grained attribute classification. Pivoted to **mmfashion** (OpenMMLab / PyTorch framework), adapting existing pre-trained vision models to extract granular features.
- **Frontend & Workflow**: Constructed a Next.js interface with **Shadcn UI** components, handling asynchronous image uploads, feature previewing, and state management.

### Infrastructure & Environment Optimization

- **Docker Containerization**: Packaging PyTorch and OpenCV dependencies into isolated Docker images ensured identical runtime environments across local development and production servers.
- **NixOS Workarounds**: Resolved Python dependency conflicts on NixOS by leveraging Docker and VS Code Remote Containers for development, avoiding Nix store package collisions.
- **Azure Cloud Deployment**: Configured container registries and pushed both finalized microservices to **Microsoft Azure** for production evaluation by the Sentient Scripts team.

### Tech Stack
- **Frontend**: Next.js, TypeScript, React, Shadcn UI
- **Backend & AI**: Python, Flask, Ollama (Mistral), PyTorch, mmfashion, YOLOv8, Rasa NLU
- **DevOps**: Docker, NixOS, Microsoft Azure Container Registry, Git

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="/assets/cases/sentientscript/Internship_Report.pdf" target="_blank" class="button primary pill mt-2" style="display:inline-block; text-decoration:none;">View Internship Report (PDF)</a>
</div>