import napari
from napari import Viewer
from napari.layers import Image, Labels
from napari.utils.notifications import show_info
from napari.qt.threading import thread_worker

from magicgui import magic_factory

import os
import pathlib
import datetime

import numpy as np

from skimage import data
from skimage import filters

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas


@magic_factory(call_button="Press me",
               slider_float={"widget_type": "FloatSlider", 'min': -5, 'max': 5},
               dropdown={"choices": ['first', 'second', 'third']},)
def widget_demo(viewer: Viewer,
                maybe: bool,
                some_int: int,
                spin_float:float=3.14159,
                slider_float:float=2.71828,
                string:str="Text goes here",
                dropdown:str='first',
                date=datetime.datetime.now(),
                filename=pathlib.Path('/some/path.ext')):
    ''' Widget fields example
    
    '''
    show_info(f'Buttom pressed')


@magic_factory(call_button="Build plot",
               b={"choices": [2, 5, 10]},)
def plot_demo(viewer: Viewer,
              b:int=5):
    ''' Matplotlib plotting example
    
    '''
    # Langmuir adsorption equation
    x = np.linspace(0,1,100)
    y = b*x / (1+b*x)
    
    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)
    ax.plot(x,y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Langmuir adsorption model')
    viewer.window.add_dock_widget(FigureCanvas(mpl_fig), name='Plot')


@magic_factory(call_button="Build labels",)
def threading_demo(viewer: Viewer, classes_num:int=3):

    def _save_img_and_label(img_and_label):
        img = img_and_label[0]
        label = img_and_label[1]
        viewer.add_image(img, name='demo_img', colormap='turbo')
        viewer.add_labels(label, name='demo_label', opacity=0.75)

    @thread_worker(connect={'yielded':_save_img_and_label})
    def _threading_demo():
        img = data.human_mitosis()
        thresholds = filters.threshold_multiotsu(img, classes=classes_num)
        labels = np.digitize(img, bins=thresholds)
        yield (img, labels)

    _threading_demo()   