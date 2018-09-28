# filedemo_03.py

import shutil
import os

shutil.copytree('source','target_new') ## 하위 폴더까지 전부 복사
shutil.move('source','new_source') ## 기존의 source는 사라지고 있는걸 new source로.