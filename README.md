# Generating Event Posters with GANs
## Developed By - Ansh Sharma
---
# Deployed Link 
## Google Colab - https://colab.research.google.com/drive/1MyLMYyGJO1dcYnNZNuUdECuCbFSVATiH?usp=sharing

## **Description**
This project explores the creative potential of Generative Adversarial Networks (GANs) in producing visually appealing event posters based on input textual descriptions such as **event type**, **theme**, or **date**. It includes a comprehensive pipeline: **data preparation, model training, evaluation**, and an optional **web application** for poster generation. The model is evaluated using metrics like **Fréchet Inception Distance (FID)** and visual inspection to ensure quality output. This project offers opportunities to merge creativity with artificial intelligence.

---
## **Dataset**
- **Source**: Publicly available event management website  or scraped data.
- **Requirements**:  
  - **Images**: JPEG/PNG format, high resolution (e.g., 256x256).
  - **Metadata**: JSON/CSV files with attributes like event type, date, location, theme, and color preferences.
    
   ![577774d8-b7e0-4afa-811a-1c62b5efa72d](https://github.com/user-attachments/assets/861a8efd-e9e3-45f7-888e-66a5de9e53ea)
   ![cf5b0ef0-36f1-4eba-9dcd-35544ddbbf2b](https://github.com/user-attachments/assets/4d947788-f75f-4722-8ae1-563031226f26)
  ![fea9c182-79fb-4276-ba6e-35d6eaa4d60a](https://github.com/user-attachments/assets/2f770ffa-9335-4ccd-be3f-f8937bf84697)






## **Key Features**
- **Poster Generation**: Utilize GANs (e.g., CycleGAN, StyleGAN) to create high-quality event posters.
- **Metadata Utilization**: Condition poster generation on metadata such as event type, themes, and keywords.
- **Evaluation**: Quantify poster quality using FID and visual comparisons.
- **Web Application**: Allow users to generate posters based on textual inputs, providing a highly interactive experience.
- **Customizable Architecture**: Easily adapt GAN architecture for specific styles, e.g., artistic themes, typography emphasis.
- **Expandability**: Build pipelines to include new datasets or improve poster styles.

---

## **Project Workflow**
1. **Data Preparation**
   - Collect event posters and associated metadata.
   - Preprocess images for training (resize, normalization).
   - Organize data into training and testing directories.

2. **GAN Model Training**
   - Train CycleGAN or StyleGAN to map textual metadata to poster styles.
   - Save trained models for future inference.

3. **Poster Generation**
   - Use the trained generator to produce new posters.
   - Save generated outputs in a designated directory.

4. **Evaluation**
   - Compute **FID** score to compare real vs. generated posters.
   - Perform manual inspection to ensure visual coherence.

5. **Web Application**
   - Deploy a Flask-based app for user interaction.
   - Input: Text-based event details (type, theme).
   - Output: Generated event poster.

---
## Results - Generated Event Posters
![ccff7cd2-ae76-4e66-8070-755d370dd5f1](https://github.com/user-attachments/assets/c3e4d83e-10f6-4560-b10f-beacbd2ae505)
![539d047e-c00d-439b-9c6e-b25db424edd0](https://github.com/user-attachments/assets/f469c964-3f98-4d4a-8f6f-b81fcf756fee)
![26851811-ba0f-4cab-9906-5e1ad683050e](https://github.com/user-attachments/assets/df82505c-db3a-4c25-8f31-8b46055f3365)





---

## **Project Setup**




### **Prerequisites**
- **Languages and Frameworks**:
  - Python 3.7 or later
  - PyTorch
  - torchvision
  - Flask
- **Libraries**:
  - numpy
  - pandas
  - PIL (Pillow)
  - matplotlib
  - pytorch-fid
- **Tools**:
  - Jupyter Notebook for experiments
  - Docker (optional for deployment)

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Event-Poster-GAN.git
   cd Event-Poster-GAN
