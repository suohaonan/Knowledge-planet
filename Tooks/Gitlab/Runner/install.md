

# Install
1. Simply download one of the binaries for your system:
curl -L --output /usr/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/v15.10.1/binaries/gitlab-runner-linux-amd64

2. Give it permissions to execute:
sudo chmod +x /usr/local/bin/gitlab-runner

3. Create a GitLab CI user:
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
4. Install and run as service:
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
5. Register a runner
gitlab-runner register




