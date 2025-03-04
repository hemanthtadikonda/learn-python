import yaml

def update_image(file_path, new_image):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Update the image
    data['spec']['template']['spec']['containers'][0]['image'] = new_image

    with open(file_path, 'w') as file:
        yaml.dump(data, file)

    print(f"Updated image to {new_image} in {file_path}")

# Example usage
update_image('deploy.yaml', 'hemanthtadikonda/my-app:v2.0.0')