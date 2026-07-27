# Case Studies
## LLM Research paper
2026/02 - 2026/06
https://www.linkedin.com/posts/enzo-juhel_local-ai-on-intel-integrated-gpu-laptops-activity-7479861074494730242-QOu2?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
> Attached Reseach Paper.pdf
Local LLM inference on Intel integrated GPUs: what actually works

Most of the conversation around on-device AI centers on Apple Silicon and discrete NVIDIA GPUs. Intel integrated GPUs ship in hundreds of millions of laptops and remain comparatively unstudied, so I spent this semester's technology watch measuring rather than assuming.

I benchmarked 14 text-generation models, from 1B to 9B parameters, across three inference backends on a single Intel Iris Xe laptop: llama.cpp over SYCL, llama.cpp over Vulkan, and the OpenVINO Model Server. Same hardware, same INT4 quantisation, same protocol.

The dominant constraint turned out to be architectural rather than computational. The Xe-LP command streamer caps any single GPU buffer at 4 GiB, which forces the output projection of larger-vocabulary models back onto the CPU under Vulkan and SYCL. OpenVINO's tiled allocation sidesteps that ceiling, and the measured throughput follows directly: on 7B models it reached roughly 12-14 tokens/second against 4-6 for the other two backends.

Serving Gemma 4 exposed a second problem. Its vision-language export ships as a fragmented graph that a production model server cannot load directly. I resolved it by stitching the embedding sub-graphs back into the decoder at the OpenVINO level, producing a single stateful graph that the model server runs at about 14.8 tokens/second on the E4B variant.

Three of the converted models are now public on Hugging Face:
- https://lnkd.in/es6qRH9u
- https://lnkd.in/e6wEjUnM
- https://lnkd.in/eyNNDr7k

Full report attached, with the complete benchmark table and the stitching implementation. Feedback and questions welcome.
2026/06
## OVHcloud Hackathon winner
> https://miraige.vercel.app/
> ovh-1.jpg
> ovh-2.jpg
## Professional Infra
> https://www.linkedin.com/posts/enzo-juhel_three-months-four-students-a-full-enterprise-activity-7472166096872214528-53vM?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
> infra-1.jpg
2026/06
Three months. Four students. A full enterprise infrastructure, built from scratch.

As part of our 4th-year project at EPITA, we designed and deployed the complete network and systems infrastructure for OPTAVIM, a fictional 2,500-employee company spread across a national headquarters, strategic branches, and standard offices across France.
Here is what we delivered:

A secure multi-site interconnect built on redundant OpenVPN site-to-site tunnels, with pfSense CARP HA clusters running as Proxmox VMs at every site. The HQ runs dual fiber in active/active mode. Strategic branches add a 4G backup link. No downtime is acceptable on the core network.

A six-node Kubernetes cluster hosting all application workloads: Nextcloud, Dolibarr, OrangeHRM, and Wazuh SIEM. Every app is exposed through Traefik with TLS, on dedicated *.optavim.corp subdomains, with certificates managed by cert-manager.

A complete identity stack: multi-master Active Directory replicated between the datacenter and HQ, federated through Keycloak via OIDC/LDAP. Remote VPN access requires TOTP two-factor authentication through privacyIDEA.

High availability at every layer: DRBD + Pacemaker for block-level storage, NFS HA with a floating VIP for Kubernetes persistent volumes, and operator-managed MariaDB Galera multi-master, all running as VMs on our Proxmox cluster.

Full observability with Prometheus, Grafana, dedicated ServiceMonitors, and Wazuh handling security event correlation across the entire stack.

This project taught me as much about architectural discipline as about presenting in front of a COMEX. Thank you to Kylian Nézan, Tanguy DOPLER and Clément Hoyaux for three intense and rewarding months.

## Hack the Shield CTF
> https://www.linkedin.com/posts/enzo-juhel_cybersecurity-infosec-networking-activity-7470504048681652224-p5eO?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
Just wrapped up the Hack the Shield CTF, and I took a slightly unconventional approach this time: full reverse engineering and zero AI.

A huge shoutout to my teammates Kylian Nézan, Tanguy DOPLER, Mathis Le Guillous and Nino Lesueur for committing to the no-AI challenge alongside me!

I chose to focus on understanding exactly what those agents do under the hood when analyzing a binary. My scoreboard points weren't my highest ever, but the real ROI? Deep-diving into Ghidra and dusting off Assembly flags from last year’s lectures.

Something that I noticed is, during CTFs, we get network switches access that are often completely open and compared to hyper-secure Wi-Fi (WPA 2/3 Personal and Enterprise). Anyone can plug in a laptop, grab an IP, and roam the network anonymously without being easily traceable.

This security gap sent me down a rabbit hole, which led me to IEEE 802.1X (Network Access Control). Right now, I’m remotely deploying an OPNsense router + RADIUS Authentication Server hooked up to a network switch at EPITA.

Over a second phase, I want to enhance this environment with an Active Directory to handle user management for RADIUS and setup Dynamic VLANs. My goal: giving an admin full access to internal services while keeping a guest entirely isolated over the exact same physical Ethernet cable!
2026/06
## Breizh CTF
> https://www.linkedin.com/posts/epita-ecole-ingenieurs-informatique_epita-cybersecurite-breizhctf-ugcPost-7465049868756189184-aWCO?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
> breizh.jpg
classment: 12/100 
2026/05
## Company Audit
> audit-1.jpg
> https://www.linkedin.com/posts/fabrice-hesling-49215a8b_fuite-massive-chez-medtech-donn%C3%A9es-patients-ugcPost-7462760282323591168-ndZ6?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
2026/05
## Cyberbreakfast
> cyberbreakfast-1.jpg
> cyberbreakfast-2.jpg
> https://www.linkedin.com/posts/enzo-juhel_vendredi-dernier-lepita-ecole-ding%C3%A9nieurs-activity-7450566923194544129-uv6l?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
2026/04
## Resiliant infra
> dos.jpg
> https://www.linkedin.com/posts/enzo-juhel_rennes-nmap-nessus-activity-7439953896153726978-FLfo?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
2026/03
## Hack'lantique 2026
> https://www.linkedin.com/posts/enzo-juhel_ctf-cybersecurity-hacklantique-activity-7438195302441877504-VOaG?utm_source=share&utm_medium=member_desktop&rcm=ACoAAERBFWYBjG7fKQwL7D5v4I7qWtHPOA0kcMU
2026/03

MY FIRST CTF — feedback and takeaways

This weekend, I competed in my very first CTF at IMT Atlantique: CTF Hack’lantique 2026. Our team secured 5th place out of 40 teams, which is a fantastic result for our first run.
 
This experience was a massive reality check on how incredibly vast the cybersecurity landscape truly is. Entering the arena as a student made one thing instantly clear: classroom theory is foundational, but taking the time to read the man pages and practice in home labs is absolutely mandatory.
 
To keep it actionable, here are my biggest takeaways from the weekend:
— I practiced steganography methodology for the very first time and learned that following a strict process is what actually uncovers the flag.
— Escaping VLAN networks looks straightforward on paper, but executing it in a live environment is far more complex.
— Web CTFs require strict discipline to stay focused on the actual flaw and avoid wasting hours down rabbit holes.
— Building a custom setup with Arch Linux and the AUR provides excellent integration for cybersecurity tools, proving Kali Linux is not strictly necessary.
— In complex challenges, teamwork is your greatest asset for exploring alternative paths and catching the small errors that cost you the flag.
— AI agents are already capable of completing basic red team tasks, showing how fast the offensive landscape is shifting.
— Network CTFs become significantly harder when the Ethernet cable is actually unplugged from the switch.

It was a highly rewarding experience, and I’ll definitely be signing up for more local CTFs soon!

