
# 🌦️ VisionWeather

**VisionWeather** is an open-source AI project that detects weather conditions (e.g. sunny, rainy, foggy) using only computer vision—no physical sensors required.

## Features
- Detect weather in real-time using images or video frames
- Supports 6+ weather classes
- Based on ResNet50 (or any CNN/Transformer model)
- Sensorless, camera-only weather detection

## Weather Classes
- ☀️ Sunny
- ☁️ Cloudy
- 🌧️ Rainy
- 🌫️ Foggy
- ❄️ Snowy
- 🌩️ Stormy

## 🚀 How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt

## To Run The Predicttion
python visionweather.py --image path/to/image.jpg

##📌Contribute 
 
Fork the repo

Submit PRs with new features, datasets, model tweaks

## More in CONTRIBUTING.md
## CONTRIBUTING.md

# Contributing to VisionWeather

Thanks for your interest in contributing! You can:
- Improve model performance (add ViT or MobileNet support)
- Add real-world datasets
- Build web or mobile apps
- Localize for regional weather types

Fork the repo → Create a branch → Make your changes → Submit a PR!


## License
MIT License

yaml
Copy
Edit


---

### 📄 `requirements.txt`

```txt
torch
torchvision
Pillow
numpy

