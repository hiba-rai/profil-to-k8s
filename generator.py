import yaml
import os

with open("profiles/web-debian.yaml") as f:
    profile = yaml.safe_load(f)

os_image = profile["os"]
packages = profile["packages"]
profile_id = profile["profile_id"]

dockerfile_content = f"""
FROM {os_image}

RUN apt update && apt install -y {' '.join(packages)} && apt clean

CMD ["nginx", "-g", "daemon off;"]
"""

os.makedirs("generted", exist_ok=True)

with open("generated/Dockerfile", "w") as f:
   f.write(dockerfile_content)

print("dockerfile généré.") 
