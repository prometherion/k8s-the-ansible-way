# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  #
  # LB
  #
  config.vm.define "lb" do |lb|
    lb.vm.box = "centos/7"
    lb.vm.hostname = 'lb'
    lb.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    lb.vm.network :private_network, ip: "10.0.0.125"

    lb.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "lb"]

    end
  end
  #
  # controller #1
  #
  config.vm.define "controller-1" do |controller|
    controller.vm.box = "centos/7"
    controller.vm.hostname = 'controller-1'
    controller.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    controller.vm.network :private_network, ip: "10.0.0.10"

    controller.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller-1"]
    end
  end
  #
  # controller #2
  #
  config.vm.define "controller-2" do |controller|
    controller.vm.box = "centos/7"
    controller.vm.hostname = 'controller-2'
    controller.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    controller.vm.network :private_network, ip: "10.0.0.11"

    controller.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller-2"]
    end
  end
  #
  # controller #3
  #
  config.vm.define "controller-3" do |controller|
    controller.vm.box = "centos/7"
    controller.vm.hostname = 'controller-3'
    controller.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    controller.vm.network :private_network, ip: "10.0.0.12"

    controller.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "controller-3"]
    end
  end
  #
  # worker #1
  #
  config.vm.define "worker-1" do |worker|
    worker.vm.box = "centos/7"
    worker.vm.hostname = 'worker-1'
    worker.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    worker.vm.network :private_network, ip: "10.0.0.20"

    worker.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "25"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "worker-1"]
    end
  end
  #
  # worker #2
  #
  config.vm.define "worker-2" do |worker|
    worker.vm.box = "centos/7"
    worker.vm.hostname = 'worker-2'
    worker.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
    worker.vm.network :private_network, ip: "10.0.0.21"

    worker.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "25"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "worker-2"]
    end
  end
end
