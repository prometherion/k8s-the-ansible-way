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
    lb.vm.network :private_network, ip: "10.240.0.125"

    lb.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]

    end
  end
  #
  # Controllers
  #
  (1..3).each do |i|
    config.vm.define "controller-#{i}" do |controller|
      controller.vm.box = "centos/7"
      controller.vm.hostname = "controller-#{i}"
      controller.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
      controller.vm.network :private_network, ip: "10.240.0.1#{i}"

      config.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--memory", 1024]
      end
    end
  end
  #
  # Workers
  #
  (1..2).each do |i|
    config.vm.define "worker-#{i}" do |controller|
      controller.vm.box = "centos/7"
      controller.vm.hostname = "worker-#{i}"
      controller.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime", run: "always"
      controller.vm.network :private_network, ip: "10.240.0.2#{i}"

      config.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--memory", 1024]
      end
    end
  end
end
