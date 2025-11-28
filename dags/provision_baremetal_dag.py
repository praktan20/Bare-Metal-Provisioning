from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests, os, json

GITHUB_REPO = "org/provisioning-repo"           # update
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

default_args = {
    'owner': 'platform',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def trigger_github_provision(**context):
    payload = {
        "event_type": "provision-node",
        "client_payload": {
            "node_name": context["params"].get("node_name"),
            "mac": context["params"].get("mac"),
            "netbox_id": context["params"].get("netbox_id")
        }
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    url = f"https://api.github.com/repos/{GITHUB_REPO}/dispatches"
    r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=30)
    r.raise_for_status()
    return r.status_code

with DAG("provision_baremetal", default_args=default_args, schedule_interval=None,
         start_date=datetime(2025,1,1), catchup=False) as dag:

    trigger = PythonOperator(
        task_id="trigger_github_dispatch",
        python_callable=trigger_github_provision,
        params={"node_name":"node-123","mac":"aa:bb:cc:dd:ee:ff","netbox_id": 42},
    )
