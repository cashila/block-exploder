# GameCredits Block Explorer

How to run the development environment:

1. `cd env && vagrant up` - Start the Vagrant virtual machine
2. `vagrant ssh` - Log in to the virtual machine
3. `pip install --upgrade pip` - Upgrade pip
4. `sudo pip install --upgrade setuptools` - Upgrade setuptools to latest version
5. `sudo pip install ansible` - Install Ansible
6. `ansible-playbook /exploder/env/configure-vagrant.yml` - Run the configuration

The Swagger UI should be available on [http://localhost:8080/api/ui/](http://127.0.0.1:8080/api/ui/)
