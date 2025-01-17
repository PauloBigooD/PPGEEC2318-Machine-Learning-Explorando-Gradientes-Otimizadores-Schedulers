import os
import sys
import errno
import requests
import subprocess
import shutil
from IPython.display import HTML, display
from tensorboard import manager

def tensorboard_cleanup():
    info_dir = manager._get_info_dir()
    shutil.rmtree(info_dir)

FOLDERS = {
    6: ['plots', 'stepbystep', 'stepbystep', 'data_generation', 'data_preparation'],
}
FILENAMES = {
    6: ['chapter6.py', 'v2.py', 'v3.py', 'simple_linear_regression.py', 'v2.py'],
}

try:
    host = os.environ['BINDER_SERVICE_HOST']
    IS_BINDER = True
except KeyError:
    IS_BINDER = False
    
try:
    import google.colab
    IS_COLAB = True
except ModuleNotFoundError:
    IS_COLAB = False

IS_LOCAL = (not IS_BINDER) and (not IS_COLAB)

def download_to_colab(chapter, branch='main'):    
    base_url = 'https://raw.githubusercontent.com/PauloBigooD/PPGEEC2318-Machine-Learning-Explorando-Gradientes-Otimizadores-Schedulers/{}/'.format(branch)

    folders = FOLDERS[chapter]
    filenames = FILENAMES[chapter]
    for folder, filename in zip(folders, filenames):
        if len(folder):
            try:
                os.mkdir(folder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if len(filename):
            path = os.path.join(folder, filename)
            url = '{}{}'.format(base_url, path)
            r = requests.get(url, allow_redirects=True)
            open(path, 'wb').write(r.content)

    try:
        os.mkdir('runs')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

TB_LINK = ''
if IS_BINDER:
    TB_LINK = HTML('''
    <a href="" target="_blank" id="tb">Click here to open TensorBoard</a>
    <script>
        var address=document.location.href;
        a = document.getElementById('tb');
        a.href = address.substr(0, address.lastIndexOf("/")-9).concat("proxy/6006/");
    </script>
    ''')

def config_chapter6(branch='main'):
    if IS_COLAB:
        print('Downloading files from GitHub repo to Colab...')
        download_to_colab(6, branch)
        print('Finished!')
