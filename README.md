# Kubernetes: the Ansible way

Based on `Kubernetes: The Hard Way` by Kelsey Hightower but made of Ansible
playbook alongside with roles.

## Disclaimer

This tutorial doesn't use Google Cloud or any other IaaS: I had to focus on
Kubernetes components to proceed on bare metal instances and I wanted to deep
dive in installing and configuring a cluster.

Use the simple `Vagrantfile` to create some local VM and use them without
relying on any cloud provider.

## Requirements

* Mac OS X: `brew` is required for installing SSL utility tools instead (`cfssl`
  and `cfssljson`)