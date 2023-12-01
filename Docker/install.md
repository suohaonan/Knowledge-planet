
官方文档（centos）
https://docs.docker.com/engine/install/centos/

# Uninstall old versions

sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

# Install using the rpm repository

## Set up the repository
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

## Install Latest Docker Engine
1. Install Docker Engine, containerd, and Docker Compose:
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
2. Start Docker
sudo systemctl start docker
