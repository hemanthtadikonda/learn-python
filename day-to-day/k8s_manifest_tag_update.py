import yaml

def update_image_tag(file_path, new_tag):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Get the current image and update only the tag
    image = data['spec']['template']['spec']['containers'][0]['image']
    repo = image.split(":")[0]  # Keep only the repository name
    data['spec']['template']['spec']['containers'][0]['image'] = f"{repo}:{new_tag}"

    with open(file_path, 'w') as file:
        yaml.dump(data, file)

    print(f"Updated image tag to {new_tag} in {file_path}")

# Example usage
update_image_tag('deployment.yaml', 'v2.0.0')
