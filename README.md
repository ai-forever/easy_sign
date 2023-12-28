[English version](README_en.md)
# Easy_sign
Easy_sign - опенсорс проект по распознаванию Русского жестового языка, спроектированный для развёртывания через [Streamlit](https://streamlit.io/). В проекте используется "лёгкая" ML-модель, способная работать на CPU. 

## О проекте
Easy_sign использует ML-модель для распознавания отдельных жестов Русского жестового языка.
Модель была обучена на ~180 000 примеров жестов. Приблизительно 20 000 из которых были взяты из датасета [Slovo](https://github.com/hukenovs/slovo). 
Модель распознаёт 1598 жестов Русского жестового языка и может обеспечить распознавание 3-3.5 жестов в секунду на процессоре Intel(R) Core(TM) i5-6600 CPU @3.30GHz. Список распознаваемых жестов содержится в файле [RSL_class_list.txt](RSL_class_list.txt). 

Больше информации о проекте - в статье на [habr](https://habr.com/ru/companies/sberbank/articles/775688/).

## Порядок установки
```
conda create --name fleury-env python=3.10
conda activate fleury-env
pip install -r requirements.txt
```

## Использование
```
streamlit run app.py
```
![Good day](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lsZXJvd296NW9qYzhlcThkbnFvOXg3ZG9qaXhkamg1aHJ0OWVpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WyoGGzp74qzWdtPiik/giphy.gif)


## Ссылки
Команда ПИН-КОД выпустила на базе easy_sign тренажёр для изучения РЖЯ. [Статья на хабр](https://habr.com/ru/articles/777700/), [репозиторий](https://github.com/PINCODE-project/RSL-Recognition-API-exe)  

S3D модели, обученные на датасете [Slovo](https://github.com/hukenovs/slovo) для различного количества кадров, подаваемых на вход.  

| Кол-во кадров | Ссылка | Mean accuracy, % |
|:---------------:|:--------:|:----------------:|
|       32        |  https://sc.link/l8VTi  |      44.22       |
|       48        |  https://sc.link/GSojW  |      52.28       |
|       64        |  https://sc.link/fhLfd  |      55.86       |


## Лицензия
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
