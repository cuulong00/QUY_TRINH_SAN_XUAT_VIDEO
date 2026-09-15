import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

CREDS_DIR = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

def check_and_create_jobs():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    reporting = build('youtubereporting', 'v1', credentials=creds)
    
    print("Checking report types...")
    try:
        report_types = reporting.reportTypes().list().execute()
        rts = report_types.get('reportTypes', [])
        print(f"Found {len(rts)} available report types:")
        for rt in rts:
            print(f"• {rt['id']}: {rt['name']}")
            
        print("\nChecking existing reporting jobs...")
        jobs_res = reporting.jobs().list().execute()
        jobs = jobs_res.get('jobs', [])
        print(f"Found {len(jobs)} active jobs:")
        job_ids = {}
        for j in jobs:
            print(f"• Job ID: {j['id']}, Type: {j['reportTypeId']}, Name: {j.get('name')}")
            job_ids[j['reportTypeId']] = j['id']
            
        # Create reach job if not exists
        target_types = ['channel_reach_basic_a1', 'channel_basic_a2']
        for tt in target_types:
            if tt not in job_ids:
                print(f"Creating reporting job for {tt}...")
                try:
                    new_job = reporting.jobs().create(body={
                        "reportTypeId": tt,
                        "name": f"Daily_{tt}"
                    }).execute()
                    print(f"✅ Created job {tt}: {new_job['id']}")
                    job_ids[tt] = new_job['id']
                except Exception as e:
                    print(f"❌ Failed to create job {tt}: {e}")
                    
        # Check for generated reports in active jobs
        for tt, jid in job_ids.items():
            try:
                reports = reporting.jobs().reports().list(jobId=jid).execute()
                reps = reports.get('reports', [])
                print(f"\nJob {tt} ({jid}): Found {len(reps)} ready reports.")
                for r in reps[:5]:
                    print(f"  - Report: {r['id']}, Date: {r.get('startTime')} to {r.get('endTime')}, URL: {r.get('downloadUrl')}")
            except Exception as e:
                print(f"Error checking reports for {jid}: {e}")
                
    except Exception as e:
        print(f"API Call Error: {e}")

if __name__ == "__main__":
    check_and_create_jobs()
