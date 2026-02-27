#### Step 1: Launch EC2 Instance #######
Amazon Linux 2 or Ubuntu
Allow inbound security group:
Port 22 → SSH
Port 5000 → Flask
Port 3306 → Only from EC2 to RDS

#### Step 2: Install Dependencies on EC2 #########
SSH into EC2:
sudo yum update -y \
sudo yum install python3 -y \
sudo yum install python3-pip -y 

#### Clone/Upload your app: #####
```bash
mkdir flask-rds-app
cd flask-rds-app

Upload your app.py & requirements.txt OR clone from GitHub.
Install dependencies:
pip3 install -r requirements.txt

##### Step 3: Run the Flask App ########
python3 app.py

Visit in browser:
http://<EC2-Public-IP>:5000

##### mysql table ######
#### MySQL Table for RDS
#### Run this SQL in your RDS MySQL:

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    salary DECIMAL(10,2)
);

### additional command for cicd###
'''bash
 1  aws configure 
    2  aws s3 ls
    3  aws configure
    4  aws s3 ls
    5  sudo yum install git -y
    6  sudo yum install docker
    7  curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    8  chmod +x kubectl
    9  sudo mv kubectl /usr/local/bin/
   10  curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz
   11  sudo mv eksctl /usr/local/bin
   12  eksctl create cluster --name mycluster --region ap-south-1 --node-type m7i-flex.large --nodes 2 --nodes-min 1 --nodes-max 3
   13  kubectl get  nodes
   14  java --version
   15  sudo usermod -aG docker jenkins
   16  sudo systemctl restart jenkins
   17  ls -la
   18  sudo cp -r .aws/ /var/lib/jenkins/
   19  sudo chown -R jenkins:jenkins /var/lib/jenkins/.aws/
   20  ls -ld /var/lib/jenkins/.aws/
   21  ls -la 
   22  sudo cp -r .kube/ /var/lib/jenkins/
   23  sudo chown -R jenkins:jenkins /var/lib/jenkins/.kube/
   24  kubectl get all
   25  kubectl exec -it mysql-fbb4f56bd-qh5cj  -- bash
   '''
