# 🌦️ VisionWeather

**VisionWeather** is an open-source AI project that detects weather conditions (e.g. sunny, rainy, foggy) using only computer vision—no physical sensors required.

## Features
- Detect weather in real-time using images or video frames
- Supports 6+ weather classes
- Based on ResNet50 (or any CNN/Transformer model)
- Sensorless, camera-only weather detection

## How it Works
VisionWeather uses a deep learning model, specifically a Convolutional Neural Network (CNN) or a Transformer model, trained to classify images based on weather conditions. The model takes an image as input and outputs a probability distribution over the supported weather classes.

## Weather Classes
- ☀️ Sunny
- ☁️ Cloudy
- 🌧️ Rainy
- 🌫️ Foggy
- ❄️ Snowy
- 🌩️ Stormy

## Dataset
_(Information about the dataset used to train the model, including its source, size, and any preprocessing steps, should be added here.)_

## Model Architecture
_(Details about the specific model architecture, such as the number of layers, types of layers, and any modifications to the base ResNet50 or other models, should be added here.)_

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/VisionWeather.git
   cd VisionWeather
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run prediction:**
   To predict weather from an image:
   ```bash
   python visionweather.py --image path/to/your/image.jpg
   ```
   To start the Streamlit web application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Training
_(Instructions on how to train the model, including data preparation, training scripts, and hardware requirements, should be added here.)_

## 📌 Contribute
Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more details on how to get started.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if a separate LICENSE file exists, otherwise state "MIT License" directly).

---

### 📄 `requirements.txt`
The `requirements.txt` file lists the Python packages required to run VisionWeather:
```txt
torch
torchvision
Pillow
numpy
streamlit
```
