BDS^3 Image Analysis with Python and napari
======
_Biological Data Science Summer School, 7-21 July 2024, Uzhhorod, Ukraine._

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/wisstock/BDS-3_2024_img_analysis">BDS^3 2024. Image Analysis with Python and napari </a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/wisstock">Borys Olifirov</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 


Матеріали до практичного курсу з аналізу даних live-cell imaging та свторення плагінів для napari.

## Встановлення Python та створення оточення
### Необхідні бібліотеки
- Python >= 3.9
- Jupyter
- Numpy
- Scipy
- Scikit-image
- Matplotlib
- SymPy (optional, for section 1 only)

Наполегливо рекомендую використовувати менеджер оточень для встановлення бібліотек щоб запобігти конфлікту версій та залежностей ([Miniconda](https://docs.conda.io/en/latest/miniconda.html), [venv](https://docs.python.org/3/library/venv.html) і т.д.), інструкція для роботи з Conda наведена нижче.

### Встановлення Conda та створення оточення
[Встановіть](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) __Miniconda__ (Anaconda одразу містить купу непотрібних для даного проекту пакетів і займай >3GB) для Вашої операційної системи.

Наступні команди вводити в Unix-термінал (у випадку Linux або MacOS) або у конда Anaconda Prompt (у випадку Windows).

Створення оточення з мінімальним набором бібілотек:
```
conda create bds3-img-env python>3.9 jupyter numpy scipy 
```

Створення повного оточення з YAML файла:
```
conda env create -f bds3-img-env.yml
```

Запуск оточення:
```
conda activate bds3-img-env
```

Вихід з оточення:
```
conda deactivate bds3-env
```

### Встановлення napari
[napari](https://napari.org/stable/) є відкритою бібліотекою для візуалізацію та аналізу багатовимірних зображень. Окрім можливості використання napari надає зручний графічний інтерфейс та простий framework для інтеграції нового фукціоналу у вигляді плагінів. Доступні плагіни можна знайти на [napari-hub](https://www.napari-hub.org/).

## Встановлення IDE

Інтегроване середовище розробки (Integrated Development Environment - IDE) значно спростить роботу з оточенями Conda та Jupyter-ноутбуками з яких складається даний курс.

Встановлення та налаштування:
- [Встановіть](https://code.visualstudio.com/) __Visual Studio Code__ відповідно Вашій оперційній системі
- Для роботи з кодом на Python та Jupyter-ноутбуками користуючись вкладкою _Розширення_ (_Extensions_) на лівій панелі IDE встановіть розширення __Python__ та __Jupyter__
- Для запуску Jupyter-ноутбука в середовищі Conda натисніть на меню _Select Kernel_ у верхньому правому кутку вікна відкритого Jupyter-ноутбука та оберіть __bds3-img-env__ серед запропонованих варіантів інтерпретаторів чи середовищ (у випадку такого підключення середовища запуск через термінал/Prompt не потрібен)

## Реєстрація на PyPI

## Корисні посилання
- [Scikit-image examples](https://scikit-image.org/docs/stable/auto_examples/index.html)
- [Image processing learning resorces](https://homepages.inf.ed.ac.uk/rbf/HIPR2/hipr_top.htm)
- [Scientific Volume Imaging](https://svi.nl/Huygens-Imaging-Academy)
- [Introduction to Modeling for Neuroscience](https://dabane-ghassan.github.io/ModNeuro/)
- [Convolutions in image processing, YouTube](https://www.youtube.com/watch?v=8rrHTtUzyZA)


## Література
- [Fundamentals of Fluorescence Imaging](https://www.taylorfrancis.com/books/edit/10.1201/9781351129404/fundamentals-fluorescence-imaging-guy-cox)
- [Handbook of Biological Confocal Microscopy](https://link.springer.com/book/10.1007/978-0-387-45524-2)
- [Enzyme Kinetics: Principles and Methods](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527806461)
- [Calcium Signaling in Dendrites and Spines: Practical and Functional Considerations](https://pubmed.ncbi.nlm.nih.gov/18817730/)
- [Competitive Calcium Binding: Implications for Dendritic Calcium Signaling](https://link.springer.com/article/10.1023/A:1008891229546)
- [Decoding glutamate receptor activation by the Ca2+sensor protein hippocalcin in rat hippocampal neurons](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1460-9568.2010.07303.x)