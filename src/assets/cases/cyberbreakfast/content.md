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
