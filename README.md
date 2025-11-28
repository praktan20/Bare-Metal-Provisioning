# Bare-Metal Provisioning Pipeline

This repo contains a production-ready template for a fully automated bare-metal provisioning pipeline:
Airflow (orchestration) -> GitHub Actions (self-hosted runner) -> PXE/iPXE + Kickstart/Cloud-init -> Ansible bootstrap -> Argo CD sync.

**Replace secrets and environment specifics before use.**

Required services & components:
- Airflow instance with a GitHub PAT (repo:dispatch permission)
- GitHub repo with self-hosted runners in management network
- DHCP/TFTP/iPXE HTTP boot server (httpboot)
- NetBox inventory with BMC info
- Bastion host for Ansible control (or runners have direct SSH)
- Argo CD for app sync

See RUNNER_README.md for runner setup.
