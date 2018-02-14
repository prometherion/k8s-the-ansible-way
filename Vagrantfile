# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  #
  # Controller #1
  #
  config.vm.define "controller1" do |controller1|
    controller1.vm.box = "centos/7"
    controller1.vm.hostname = 'controller1'

    controller1.vm.network :private_network, ip: "10.0.0.10"

    controller1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller1"]
    end
  end
  #
  # Controller #2
  #
  config.vm.define "controller2" do |controller2|
    controller2.vm.box = "centos/7"
    controller2.vm.hostname = 'controller2'

    controller2.vm.network :private_network, ip: "10.0.0.11"

    controller2.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller2"]
    end
  end
  #
  # Controller #3
  #
  config.vm.define "controller3" do |controller3|
    controller3.vm.box = "centos/7"
    controller3.vm.hostname = 'controller3'

    controller3.vm.network :private_network, ip: "10.0.0.12"

    controller3.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller3"]
    end
  end
  #
  # Worker #1
  #
  config.vm.define "worker1" do |worker1|
    worker1.vm.box = "centos/7"
    worker1.vm.hostname = 'worker1'

    worker1.vm.network :private_network, ip: "10.0.0.20"

    worker1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "worker1"]
    end
  end
  #
  # Worker #2
  #
  config.vm.define "worker2" do |worker2|
    worker2.vm.box = "centos/7"
    worker2.vm.hostname = 'worker2'

    worker2.vm.network :private_network, ip: "10.0.0.21"

    worker2.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "worker2"]
    end
  end
end
