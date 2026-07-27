import os

cases_content = {
    "ovh-hackathon": """
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
""",

    "ctf": """
### Breizh CTF
As part of the **EPIT'HACK** team, we secured an impressive **12th place out of 116 teams**. Beyond the competition, EPITA sponsored the event to foster a strong cybersecurity culture in the region. At our stand, we engaged attendees with hands-on activities like "Hack me if you can", the "Cyber Iceberg", and LLM hijacking to promote ethical hacking and digital critical thinking.

![Breizh CTF Ranking](/assets/cases/ctf/breizh-1.jpg)

### Hack the Shield CTF
Just wrapped up the Hack the Shield CTF, and I took a slightly unconventional approach this time: full reverse engineering and zero AI.

I chose to focus on understanding exactly what those agents do under the hood when analyzing a binary. My scoreboard points weren't my highest ever, but the real ROI was deep-diving into Ghidra and dusting off Assembly flags from last year’s lectures.

Something that I noticed is, during CTFs, we get network switches access that are often completely open compared to hyper-secure Wi-Fi (WPA 2/3 Personal and Enterprise). Anyone can plug in a laptop, grab an IP, and roam the network anonymously without being easily traceable.

This security gap sent me down a rabbit hole, which led me to IEEE 802.1X (Network Access Control). I ended up remotely deploying an OPNsense router + RADIUS Authentication Server hooked up to a network switch at EPITA to experiment with secure internal services segregation using Dynamic VLANs.

### Hack'lantique 2026
My first CTF! Our team secured 5th place out of 40 teams, which was a fantastic result for our first run.

This experience was a massive reality check on how incredibly vast the cybersecurity landscape truly is. Some of my biggest takeaways:
- Practicing steganography methodology for the very first time and learning that following a strict process is what actually uncovers the flag.
- Escaping VLAN networks looks straightforward on paper, but executing it in a live environment is far more complex.
- Web CTFs require strict discipline to stay focused on the actual flaw and avoid wasting hours down rabbit holes.
- Building a custom setup with Arch Linux and the AUR provides excellent integration for cybersecurity tools.
- In complex challenges, teamwork is your greatest asset for exploring alternative paths and catching the small errors.

### Links
<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="https://www.linkedin.com/posts/enzo-juhel_cybersecurity-infosec-networking-activity-7470504048681652224-p5eO" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Hack the Shield CTF</a>
<a href="https://www.linkedin.com/posts/epita-ecole-ingenieurs-informatique_epita-cybersecurite-breizhctf-ugcPost-7465049868756189184-aWCO" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Breizh CTF</a>
<a href="https://www.linkedin.com/posts/enzo-juhel_ctf-cybersecurity-hacklantique-activity-7438195302441877504-VOaG" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Hack'lantique 2026</a>
</div>
""",

    "cyberbreakfast": """
### The Invisible Intruder: How LiteLLM Was Hijacked

During the EPITA Cyberbreakfast, I delivered a technical presentation analyzing the **LiteLLM Supply Chain Attack** orchestrated by the threat actor "TeamPCP".

**Presentation Highlights:**
- **Attack Kill-Chain:** Detailed the timeline from the Trivy CI exploitation and PyPI token theft to the active poisoning of the Telnyx PyPI SDK.
- **Malware Tactics:** Explored how the malware stole development secrets (AWS/GCP/Azure credentials, K8s tokens, TLS certificates) and executed parallel payloads masked within `.wav` audio files using **steganography**.
- **Defensive Takeaways:** Advocated for critical supply chain defense mechanisms:
  1. Pinning dependencies to strict commit hashes instead of vulnerable tags.
  2. Abandoning static tokens in favor of OIDC (Trusted Publishers) pipelines.
  3. Shifting from simple file-type detection to robust behavioral monitoring.

![Cyberbreakfast 1](/assets/cases/cyberbreakfast/cyberbreakfast-1.jpg)
![Cyberbreakfast 2](/assets/cases/cyberbreakfast/cyberbreakfast-2.jpg)

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="https://www.linkedin.com/posts/enzo-juhel_vendredi-dernier-lepita-ecole-ding%C3%A9nieurs-activity-7450566923194544129-uv6l" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>
</div>
"""
}

base_dir = "src/assets/cases"

for slug, content in cases_content.items():
    filepath = os.path.join(base_dir, slug, "content.md")
    with open(filepath, "w") as f:
        f.write(content.strip() + "\n")
        print(f"Updated {slug}")

