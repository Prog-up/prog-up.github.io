### Winning the EPITA Rennes × OVHcloud Hackathon

**MIR[AI]GE** flips the paradigm of infrastructure defense against autonomous LLM agents: instead of blocking them, we detect, isolate, and trap them in an infinite procedural labyrinth to burn their token budget.

**Architecture & Technical Stack:**
- **Load Balancing:** OpenStack Octavia (LBaaS) handling L7 routing via HTTP session cookies.
- **Detection Cascade (Sentinel):** 
  - **T0:** Deterministic Sigma rules for immediate filtering.
  - **T1:** XGBoost model on a 10-second sliding window to detect mass behavioral anomalies.
  - **T2:** Llama-3.1-8B LLM for ambiguous contextual judgments.
- **Orchestrator & MCP:** An orchestrator utilizes a Model Context Protocol (MCP) server to dynamically reconfigure the load balancer.
- **The Ghost Shell:** A fake, endless procedural environment featuring asymmetric content generation, honeycreds loops, and reverse-prompt-injection canaries to waste the attacker's compute.

From an OVH-coupled PoC, we engineered it into a fully agnostic, containerized open-source tool. 

![OVH Hackathon 1](/assets/cases/ovh-hackathon/ovh-1.jpg)
![OVH Hackathon 2](/assets/cases/ovh-hackathon/ovh-2.jpg)

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="https://miraige.vercel.app/" target="_blank" class="button primary pill mt-2" style="display:inline-block; text-decoration:none;">View MIR[AI]GE Website</a>
</div>
