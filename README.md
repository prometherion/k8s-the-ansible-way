# Kubernetes: The Ansible Way

Based on `Kubernetes: The Hard Way` by Kelsey Hightower but made of Ansible
playbook alongside with roles.

## Disclaimer

This tutorial doesn't use Google Cloud or any other IaaS: I had to focus on
Kubernetes components to proceed on bare metal instances and I wanted to deep
dive in installing and configuring a cluster.

Use the simple `Vagrantfile` to create some local VMs and use them without
relying on any cloud provider: some extra options had to be implemented due to
some issues with Vagrant (especially with NAT interface).

## Requirements

* Mac OS X: `brew` is required for installing SSL utility tools instead (`cfssl`
  and `cfssljson`)

## Vagrant: private and public addresses

Since Vagrant uses `eth0` as NAT interface you have to customize Private and
Public addreses using `host`-level variables: in case of adoption over a cloud
provider you have to fill just one between public or private one.
