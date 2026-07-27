import os
import shutil

cases_content = {
    "llm-research": """
Most of the conversation around on-device AI centers on Apple Silicon and discrete NVIDIA GPUs. Intel integrated GPUs ship in hundreds of millions of laptops and remain comparatively unstudied, so I spent this semester's technology watch measuring rather than assuming.

I benchmarked 14 text-generation models, from 1B to 9B parameters, across three inference backends on a single Intel Iris Xe laptop: llama.cpp over SYCL, llama.cpp over Vulkan, and the OpenVINO Model Server. Same hardware, same INT4 quantisation, same protocol.

The dominant constraint turned out to be architectural rather than computational. The Xe-LP command streamer caps any single GPU buffer at 4 GiB, which forces the output projection of larger-vocabulary models back onto the CPU under Vulkan and SYCL. OpenVINO's tiled allocation sidesteps that ceiling, and the measured throughput follows directly: on 7B models it reached roughly 12-14 tokens/second against 4-6 for the other two backends.

Serving Gemma 4 exposed a second problem. Its vision-language export ships as a fragmented graph that a production model server cannot load directly. I resolved it by stitching the embedding sub-graphs back into the decoder at the OpenVINO level, producing a single stateful graph that the model server runs at about 14.8 tokens/second on the E4B variant.

Three of the converted models are now public on Hugging Face:
- [Gemma 4V INT4](https://lnkd.in/es6qRH9u)
- [Llama 3 INT4](https://lnkd.in/e6wEjUnM)
- [Mistral 7B INT4](https://lnkd.in/eyNNDr7k)

You can read the full report here:
[View Research Paper (PDF)](/assets/cases/llm-research/Reseach%20Paper.pdf)
""",
    
    "infra-pro": """
Three months. Four students. A full enterprise infrastructure, built from scratch.

As part of our 4th-year project at EPITA, we designed and deployed the complete network and systems infrastructure for OPTAVIM, a fictional 2,500-employee company spread across a national headquarters, strategic branches, and standard offices across France.

Here is what we delivered:

A secure multi-site interconnect built on redundant OpenVPN site-to-site tunnels, with pfSense CARP HA clusters running as Proxmox VMs at every site. The HQ runs dual fiber in active/active mode. Strategic branches add a 4G backup link. No downtime is acceptable on the core network.

A six-node Kubernetes cluster hosting all application workloads: Nextcloud, Dolibarr, OrangeHRM, and Wazuh SIEM. Every app is exposed through Traefik with TLS, on dedicated `*.optavim.corp` subdomains, with certificates managed by cert-manager.

A complete identity stack: multi-master Active Directory replicated between the datacenter and HQ, federated through Keycloak via OIDC/LDAP. Remote VPN access requires TOTP two-factor authentication through privacyIDEA.

High availability at every layer: DRBD + Pacemaker for block-level storage, NFS HA with a floating VIP for Kubernetes persistent volumes, and operator-managed MariaDB Galera multi-master, all running as VMs on our Proxmox cluster.

Full observability with Prometheus, Grafana, dedicated ServiceMonitors, and Wazuh handling security event correlation across the entire stack.

This project taught me as much about architectural discipline as about presenting in front of a COMEX.

![Enterprise Infrastructure Architecture](/assets/cases/infra-pro/infra-1.jpg)
""",

    "ctf": """
### Hack the Shield CTF
Just wrapped up the Hack the Shield CTF, and I took a slightly unconventional approach this time: full reverse engineering and zero AI.

I chose to focus on understanding exactly what those agents do under the hood when analyzing a binary. My scoreboard points weren't my highest ever, but the real ROI was deep-diving into Ghidra and dusting off Assembly flags from last year’s lectures.

Something that I noticed is, during CTFs, we get network switches access that are often completely open compared to hyper-secure Wi-Fi (WPA 2/3 Personal and Enterprise). Anyone can plug in a laptop, grab an IP, and roam the network anonymously without being easily traceable.

This security gap sent me down a rabbit hole, which led me to IEEE 802.1X (Network Access Control). I ended up remotely deploying an OPNsense router + RADIUS Authentication Server hooked up to a network switch at EPITA to experiment with secure internal services segregation using Dynamic VLANs.

### Breizh CTF
Ranked 12th out of 100 teams.
![Breizh CTF Ranking](/assets/cases/ctf/breizh-1.jpg)

### Hack'lantique 2026
My first CTF! Our team secured 5th place out of 40 teams, which was a fantastic result for our first run.

This experience was a massive reality check on how incredibly vast the cybersecurity landscape truly is. Some of my biggest takeaways:
- Practicing steganography methodology for the very first time and learning that following a strict process is what actually uncovers the flag.
- Escaping VLAN networks looks straightforward on paper, but executing it in a live environment is far more complex.
- Web CTFs require strict discipline to stay focused on the actual flaw and avoid wasting hours down rabbit holes.
- Building a custom setup with Arch Linux and the AUR provides excellent integration for cybersecurity tools.
- In complex challenges, teamwork is your greatest asset for exploring alternative paths and catching the small errors.
""",

    "ovh-hackathon": """
Won the OVHcloud hackathon by building and deploying a cloud-native solution on their infrastructure.

![OVH Hackathon 1](/assets/cases/ovh-hackathon/ovh-1.jpg)
![OVH Hackathon 2](/assets/cases/ovh-hackathon/ovh-2.jpg)
""",

    "company-audit": """
Conducted an extensive security audit following a massive patient data leak at a MedTech company. Evaluated the attack vectors, secured the existing infrastructure, and drafted comprehensive recovery and mitigation policies.

![Company Audit](/assets/cases/company-audit/audit-1.jpg)
""",

    "cyberbreakfast": """
Participated in the EPITA Cyberbreakfast, focusing on cybersecurity knowledge sharing, threat landscape analysis, and practical workshops.

![Cyberbreakfast 1](/assets/cases/cyberbreakfast/cyberbreakfast-1.jpg)
![Cyberbreakfast 2](/assets/cases/cyberbreakfast/cyberbreakfast-2.jpg)
""",

    "resilient-infra": """
Designed and tested resilient infrastructure topologies focusing on mitigating Denial of Service (DoS) attacks and maintaining high availability under stress.

![Resilient Infra](/assets/cases/resilient-infra/dos.jpg)
""",
    
    "excense": "",
    "sentientscript": "",
    "agrial": "Managed inventory, organized displays, and handled customer orders and logistics during my summer job."
}

moves = {
    "llm-research": ["Reseach Paper.pdf"],
    "infra-pro": ["infra-1.jpg"],
    "ctf": ["breizh-1.jpg"],
    "ovh-hackathon": ["ovh-1.jpg", "ovh-2.jpg"],
    "company-audit": ["audit-1.jpg"],
    "cyberbreakfast": ["cyberbreakfast-1.jpg", "cyberbreakfast-2.jpg"],
    "resilient-infra": ["dos.jpg"]
}

base_dir = "src/assets/cases"

for slug, content in cases_content.items():
    case_dir = os.path.join(base_dir, slug)
    os.makedirs(case_dir, exist_ok=True)
    with open(os.path.join(case_dir, "content.md"), "w") as f:
        f.write(content.strip())
    
    if slug in moves:
        for filename in moves[slug]:
            src_file = os.path.join("attached-tmp", filename)
            dst_file = os.path.join(case_dir, filename)
            if os.path.exists(src_file):
                shutil.copy(src_file, dst_file)
                print(f"Copied {filename} to {slug}")

