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

```python
if snapshot['VolumeId'] not in used_volume_ids:
    ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
🎯 Goal: Clean up unused snapshots and save 💸 AWS costs.


 IAM Permissions (Policy Required)
