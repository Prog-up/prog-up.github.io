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

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="https://www.linkedin.com/posts/enzo-juhel_three-months-four-students-a-full-enterprise-activity-7472166096872214528-53vM" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Read more on LinkedIn</a>
</div>
