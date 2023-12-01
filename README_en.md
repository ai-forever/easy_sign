[Русская версия](README.md)
# Easy_sign

Easy_sign is an open source russian sign language recognition project that uses small CPU model for predictions and is designed for easy deployment via Streamlit.

## About the project
Easy_sign uses a machine learning model to recognize Russian sign language gestures. 
The model was trained on ~180,000 examples of Russian sign language gestures. Approximately 20,000 of which are taken from the [Slovo](https://github.com/hukenovs/slovo) dataset.
The model recognizes 1598 Russian sign language gestures and can process 3-3.5 gestures per second on an Intel(R) Core(TM) i5-6600 CPU @3.30GHz. The list of recognized gestures is available in the file [RSL_class_list.txt](RSL_class_list.txt). 

To learn more about the project - visit the link to our article on [habr](https://habr.com/ru/companies/sberbank/articles/775688/).

## Installation
```
conda create --name fleury-env python=3.10
conda activate fleury-env
pip install -r requirements.txt
```

## Usage
```
streamlit run app.py
```
![Good day](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lsZXJvd296NW9qYzhlcThkbnFvOXg3ZG9qaXhkamg1aHJ0OWVpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WyoGGzp74qzWdtPiik/giphy.gif)


## Links
The PINCODE team has released a training simulator based on easy_sign to study Russian sign language. [Habr (Russian)](https://habr.com/ru/articles/777700/), [github](https://github.com/PINCODE-project/RSL-Recognition-API-exe)


 ## License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
