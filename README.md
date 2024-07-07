BDS^3 2024
==========

## Image Analysis with Python and napari

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)

_Biological Data Science Summer School, 7-20 July 2024, Uzhhorod, Ukraine._


---

## Структура курсу
|        | 0 (13.07)                  | 1 (15.07)                                                    | 2 (16.07)                                                    | 3 (17.07)                          | 4 (18.07)                                                    | 5 (19.07)           |
| ------ | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------ | ------------------- |
| __1h__ (11:30-12:30) | -                          | Біологічна основа проекту, формат презентації результатів    | Q/A                                                          | Q/A                                | Q/A                                                          | -                   |
| __2h__ (13:30-15:30)| -                          | Робота з багатовимірними масивами, відображення даних live-cell imaging, попередня обробка даних | Побудова профілів інтенсивностей з використанням масок, візуалізація профілів | Упаковка коду в функції та класи   | Потокові розрахунки в napari, збірка плагіну | Підготовка постера  |
| __2h__ (16:00-18:00)| Основи роботи з масивами numpy, зображення як масиви | Маскування і морфологічні операції із бінарними зображеннями | Оцінка біофізичних характеристик на основі даних декількох спектральних каналів | Побудова простих віджетів в napari | Підбирання хвостів                                           | Презентація постера |


> [!TIP]
> Перед початком курсу варто пригадати синтаксис функцій та класів в Python [українською](https://w3schoolsua.github.io/python/python_functions.html#gsc.tab=0) або [англійською](https://www.w3schools.com/python/python_functions.asp).

> [!TIP]
> Перед початком курсу варто пригадати основи роботи з масивами NumPy [українською](https://devzone.org.ua/post/chomu-vam-slid-vykorystovuvaty-numpy) або [англійською](https://numpy.org/doc/stable/user/absolute_beginners.html).


## Підготовка оточення
#### Необхідні бібліотеки
- Python >= 3.8
- Jupyter
- Numpy
- Scipy
- Scikit-image
- Matplotlib
- SymPy (optional)

Наполегливо рекомендую використовувати менеджер оточень для встановлення бібліотек щоб запобігти конфлікту версій та залежностей ([Miniconda](https://docs.conda.io/en/latest/miniconda.html), [venv](https://docs.python.org/3/library/venv.html) і т.д.), інструкція для роботи з Conda наведена нижче.

#### Встановлення Conda та створення оточення
[Встановіть](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) __Miniconda__ для Вашої операційної системи.

> [!WARNING]
> Рекомендую встановлювати саме Miniconda, оскільки Anaconda одразу містить багато непотрібних для проекту бібліотек і важить > 2GB.

Наступні команди вводити в Unix-термінал (у випадку Linux або MacOS) або Anaconda Prompt (у випадку Windows).

Створення повного оточення з YAML файла:
```
conda env create -f bds3-img-env.yml
```

Створення оточення з мінімальним набором бібілотек:
```
conda create -n bds3-img-env python>3.9 jupyter numpy matplotlib
```

Запуск оточення:
```
conda activate bds3-img-env
```

Вихід з оточення:
```
conda deactivate bds3-img-env
```

#### Встановлення napari
[napari](https://napari.org/stable/) є відкритою бібліотекою для візуалізацію та аналізу багатовимірних зображень. Окрім можливості використання napari надає зручний графічний інтерфейс та простий framework для інтеграції нового фукціоналу у вигляді плагінів. Доступні плагіни можна знайти на [napari-hub](https://www.napari-hub.org/).

Встановлення за допомогою `pip` через Unix-термінал/Anaconda Prompt, встановлювати слід в оточенні __bds3-img-env__:
```
python -m pip install "napari[all]"
```

Для запуска графічного інтерфейса виконайте команду ```napari``` в Unix-терміналі/Anaconda Prompt в оточені __bds3-img-env__.

> [!TIP]
> До початку курсу рекомендую ознайомитись з  матеріалами [napari how-to guides](https://napari.org/stable/howtos/index.html).


## Встановлення IDE

Інтегроване середовище розробки (Integrated Development Environment - IDE) значно спростить роботу з оточенями Conda та Jupyter-ноутбуками з яких складається даний курс.

Встановлення та налаштування:
- [Встановіть](https://code.visualstudio.com/) __Visual Studio Code__ відповідно Вашій оперційній системі
- Для роботи з кодом Python та Jupyter-ноутбуками користуючись вкладкою _Розширення_ (_Extensions_) на лівій панелі IDE встановіть розширення __Python__ та __Jupyter__
- Для запуску Jupyter-ноутбука в середовищі Conda натисніть на меню _Select Kernel_ у верхньому правому кутку вікна відкритого Jupyter-ноутбука та оберіть __bds3-img-env__ серед запропонованих варіантів інтерпретаторів чи оточень (у випадку такого підключення середовища запуск оточення через Unix-термінал/Anaconda Prompt не потрібен)


## Обліковий запис PyPI (optional)

Створення облікового запису [Python Package Index](https://pypi.org/) (PyPI) дозволить розповсюджувати і встановлювати створені Вами бібліотеки та плагіни napari за допомогою системи керування пакетами pip.

#### Додаткові бібліотеки для збірки та публікації бібліотек:
- setuptools >= 61.0
- build
- twine


## Корисні посилання

- [Scikit-image examples](https://scikit-image.org/docs/stable/auto_examples/index.html)
- [Image processing learning resorces](https://homepages.inf.ed.ac.uk/rbf/HIPR2/hipr_top.htm)
- [The Carl Zeiss Microscopy Online Campus](https://zeiss-campus.magnet.fsu.edu/index.html)
- [Scientific Volume Imaging](https://svi.nl/Huygens-Imaging-Academy)
- [Introduction to Modeling for Neuroscience](https://dabane-ghassan.github.io/ModNeuro/)
- [Convolutions in image processing, YouTube](https://www.youtube.com/watch?v=8rrHTtUzyZA)


## Література

- [Fundamentals of Fluorescence Imaging](https://www.taylorfrancis.com/books/edit/10.1201/9781351129404/fundamentals-fluorescence-imaging-guy-cox)
- [Imaging Cellular and Molecular Biological Functions](https://link.springer.com/book/10.1007/978-3-540-71331-9)
- [Handbook of Biological Confocal Microscopy](https://link.springer.com/book/10.1007/978-0-387-45524-2)
- [An introduction to optical super-resolution microscopy for the adventurous biologist](https://www.researchgate.net/publication/323073291_An_introduction_to_optical_super-resolution_microscopy_for_the_adventurous_biologist)
- [Nanoscopy and Multidimensional Optical Fluorescence Microscopy](https://www.tandfonline.com/doi/pdf/10.1080/00107514.2011.580375)
- [Enzyme Kinetics: Principles and Methods](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527806461)
- [Calcium Signaling in Dendrites and Spines: Practical and Functional Considerations](https://pubmed.ncbi.nlm.nih.gov/18817730/)
- [Competitive Calcium Binding: Implications for Dendritic Calcium Signaling](https://link.springer.com/article/10.1023/A:1008891229546)
- [Decoding glutamate receptor activation by the Ca2+sensor protein hippocalcin in rat hippocampal neurons](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1460-9568.2010.07303.x)

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/wisstock/BDS-3_2024_img_analysis">BDS^3 2024. Image Analysis with Python and napari </a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/wisstock">Borys Olifirov</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 