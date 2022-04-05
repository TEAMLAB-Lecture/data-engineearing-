## Ray - distributed computing

### instllation 
- 사전에 가상환경 만들 것을 추천
- pip
```
pip install -U ray  # minimal install
pip install -U "ray[tune]"  # installs Ray + dependencies for Ray Tune
```

- conda
```
conda install -c conda-forge ray-tune
conda install -c conda-forge pyarrow
conda install -c conda-forge boost-cpp
conda install -c anaconda libboost
```


### examples
- https://github.com/ray-project/tune-sklearn/blob/master/examples/xgbclassifier.py