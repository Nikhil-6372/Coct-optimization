<h1> 🧹 AWS Lambda: Unused EBS Snapshot Cleaner </h1>

This project is part of an AWS Cost Optimization initiative that automatically deletes unused Amazon EBS snapshots, helping reduce storage costs. The solution uses **AWS Lambda**, **boto3**, and is scheduled via **Amazon EventBridge (CloudWatch Scheduler)**.

---

 <h2>📌 Features </h2>

- ✅ Scans all EC2 instances (running + stopped)
- ✅ Identifies which EBS volumes are in use
- ✅ Lists all EBS snapshots owned by your account
- ✅ Deletes snapshots that are not associated with any current volume
- ✅ Scheduled to run automatically
- ✅ Easily extendable (e.g., delete only snapshots older than 90 days)

---

<h3> 🛠️ Tech Stack </h3>

- **AWS Lambda**
- **AWS EC2**
- **Amazon EBS**
- **Amazon EventBridge Scheduler**
- **Python (boto3 library)**

---

<h4> 🧠 How It Works </h4>

1. Lambda connects to EC2 using **boto3**
2. It fetches all EC2 instances (both running and stopped)
3. Extracts the list of volume IDs currently in use
4. Retrieves all EBS snapshots you own
5. Deletes snapshots that belong to volumes which are no longer attached

<h5> 🔍 Python Logic (Simplified) </h5>

<h6>🎯 Goal:</h6>
Clean up unused snapshots and save 💸 AWS costs.

<h7>🧾 IAM Permissions (Policy Required) </h7>
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

<h8>📅 Automate with EventBridge Scheduler</h8>
To run this Lambda on a schedule:

Go to Amazon EventBridge > Scheduler

Create a new rule

Choose fixed rate (e.g., every 1 day)

Set the Lambda function as the target

Choose a flexible time window (e.g., 15 minutes)

<h9>📂 Project Structure</h9>
.
├── lambda_function.py    # Python code for AWS Lambda





└── README.md             # Project documentation (you are here!)





