import subprocess
from flask import Flask, request, jsonify


def rollout_update_image(image_name: str, tag: str, deployment: str, container_name: str):
    """
    Updates the image used in the deployment and triggers a rolling update.
    
    Parameters:
    - image_name: e.g., 'rajatraj45/repo1'
    - tag: e.g., '1.0.1'
    - deployment: e.g., 'repo1-deployment'
    - container_name: e.g., 'repo1-container'
    """
    new_image = f"{image_name}:{tag}"
    try:
        # Update the image in the deployment
        print(f"Updating deployment '{deployment}' to image: {new_image}")
        subprocess.run(
            ["kubectl", "set", "image", f"deployment/{deployment}", f"{container_name}={new_image}"],
            check=True
        )

        # Optionally, watch rollout status
        subprocess.run(["kubectl", "rollout", "status", f"deployment/{deployment}"], check=True)

        print("Deployment updated successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during rollout:", e)


app = Flask(__name__)

@app.route('/dockerhub-webhook', methods=['POST'])
def dockerhub_webhook():
    data = request.get_json()
    print("🚀 Webhook Received!")
    tag = data.get('push_data', {}).get('tag')
    print("Tag:", tag)
    print("Pusher:", data.get('push_data', {}).get('pusher'))
    print("Repository:", data.get('repository', {}).get('repo_name'))
    # return jsonify({'status': 'Webhook received'}), 200

    rollout_update_image("rajatraj45/repo1", tag, "repo1-deployment", "repo1-container")

    return jsonify({'status': 'Deployment restart triggered'}), 200







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)