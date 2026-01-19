#### Step 1: Launch EC2 Instance #######
Amazon Linux 2 or Ubuntu
Allow inbound security group:
Port 22 → SSH
Port 5000 → Flask
Port 3306 → Only from EC2 to RDS

#### Step 2: Install Dependencies on EC2 #########
SSH into EC2:
```bash
sudo yum update -y
sudo yum install python3 -y
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
