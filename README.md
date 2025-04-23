<div align="Left">
 <h1> 🧹 AWS Lambda: Unused EBS Snapshot Cleaner </h1>

This project is part of an AWS Cost Optimization initiative that automatically deletes unused Amazon EBS snapshots, helping reduce storage costs. The solution uses **AWS Lambda**, **boto3**, and is scheduled via **Amazon EventBridge (CloudWatch Scheduler)**.

---

 <h2>📌 Features </h2>

- ✅ Scans all EC2 instances (running + stopped)
- ✅ Identifies which EBS volumes are in use
- ✅ Lists all EBS snapshots owned by your account
- ✅ Deletes snapshots that are not associated with any current volume
- ✅ Scheduled to run automatically
- ✅ Easily extendable 

---

<h3> 🛠️ Tech Stack </h3>

- **AWS Lambda**
- **AWS EC2**
- **Amazon EBS**
- **Amazon EventBridge Scheduler**

---

<h4> 🧠 How It Works </h4>

1. Lambda connects to EC2 using **boto3**
2. It fetches all EC2 instances (both running and stopped)
3. Extracts the list of volume IDs currently in use
4. Retrieves all EBS snapshots you own
5. Deletes snapshots that belong to volumes which are no longer attached


<h5>🎯 Goal: </h5>
Clean up unused snapshots and save 💸 AWS costs.

<h6>🧾 IAM Permissions (Policy Required) </h6>
Attach the following policy to your Lambda execution role:
{
  "Effect": "Allow",
  "Action": [
    "ec2:DescribeInstances",
    "ec2:DescribeSnapshots",
    "ec2:DeleteSnapshot"
  ],
  "Resource": "*"
}

<h7>📅 Automate with EventBridge Scheduler</h7>
To run this Lambda on a schedule:

Go to Amazon EventBridge > Scheduler

Create a new rule

Choose fixed rate (e.g., every 1 day)

Set the Lambda function as the target

Choose a flexible time window (e.g., 15 minutes)

<h8>📂 Project Structure</h8>


.
├── lambda_function.py    # Python code for AWS Lambda











└── README.md             # Project documentation (you are here!)
</div>

<h9>So here is the success screenshot</h9>
![Screenshot 2025-04-19 160217](https://github.com/user-attachments/assets/116c3c69-9cf1-4753-b94e-8b8fd9a33ebe)






