import os

links = {
    "llm-research": [
        '<a href="https://www.linkedin.com/posts/enzo-juhel_local-ai-on-intel-integrated-gpu-laptops-activity-7479861074494730242-QOu2" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>',
        '<a href="/assets/cases/llm-research/Reseach%20Paper.pdf" target="_blank" class="button primary pill mt-2" style="display:inline-block; text-decoration:none;">View Research Paper (PDF)</a>'
    ],
    "infra-pro": [
        '<a href="https://www.linkedin.com/posts/enzo-juhel_three-months-four-students-a-full-enterprise-activity-7472166096872214528-53vM" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>'
    ],
    "ctf": [
        '### Links',
        '<a href="https://www.linkedin.com/posts/enzo-juhel_cybersecurity-infosec-networking-activity-7470504048681652224-p5eO" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Hack the Shield CTF</a>',
        '<a href="https://www.linkedin.com/posts/epita-ecole-ingenieurs-informatique_epita-cybersecurite-breizhctf-ugcPost-7465049868756189184-aWCO" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Breizh CTF</a>',
        '<a href="https://www.linkedin.com/posts/enzo-juhel_ctf-cybersecurity-hacklantique-activity-7438195302441877504-VOaG" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Hack\'lantique 2026</a>'
    ],
    "company-audit": [
        '<a href="https://www.linkedin.com/posts/fabrice-hesling-49215a8b_fuite-massive-chez-medtech-donn%C3%A9es-patients-ugcPost-7462760282323591168-ndZ6" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>'
    ],
    "cyberbreakfast": [
        '<a href="https://www.linkedin.com/posts/enzo-juhel_vendredi-dernier-lepita-ecole-ding%C3%A9nieurs-activity-7450566923194544129-uv6l" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>'
    ],
    "resilient-infra": [
        '<a href="https://www.linkedin.com/posts/enzo-juhel_rennes-nmap-nessus-activity-7439953896153726978-FLfo" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>'
    ]
}

base_dir = "src/assets/cases"

for slug, html_links in links.items():
    filepath = os.path.join(base_dir, slug, "content.md")
    if os.path.exists(filepath):
        with open(filepath, "a") as f:
            f.write("\n\n<div style=\"display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;\">\n")
            for link in html_links:
                f.write(link + "\n")
            f.write("</div>\n")
