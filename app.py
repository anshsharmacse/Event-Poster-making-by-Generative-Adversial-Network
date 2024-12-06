from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Load the trained model (ensure the generator is loaded)
generator = Generator(latent_dim, label_dim).cpu()
generator.load_state_dict(torch.load('generator.pth'))  # Load the pre-trained generator model

@app.route('/generate', methods=['POST'])
def generate_poster():
    data = request.json
    event_type = data.get('event_type', 'music')
    theme = data.get('theme', 'festival')

    # Convert event metadata to one-hot encoded tensor
    label = torch.zeros(len(metadata))
    label[label_map[event_type]] = 1
    label[label_map[theme]] = 1

    # Generate the poster
    z = torch.randn(1, latent_dim).cpu()  # Latent vector
    generated_image = generator(z, label)

    # Convert tensor to image and return
    generated_image = generated_image.squeeze().detach().cpu().numpy()
    return jsonify({'message': 'Poster generated!', 'image': generated_image.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
