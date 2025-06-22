
import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.predict import predict_weather

print(predict_weather('test.jpg'))
