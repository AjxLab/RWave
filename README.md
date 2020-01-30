RWave
=====

[![PyPi](https://badge.fury.io/py/rwave.svg)](https://pypi.python.org/pypi/rwave/)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

A utility that handle audio for Python.


## Usage
### Simple Example
```python
import rwave
# Load audio file
wave, fs = rwave.read_wave('wave file path')

# Write audio file
# (wave file path, wave data, fs)
rwave.write_wave('wave file path', wave, 16000)

# Nomalize wave data
rwave.nomalize(wave)
# => audio data normalized to 0~1

# Convert sampling rate (16000->8000)
wave, fs = rwave.convert_fs(wave, 16000, 8000)

# Convert audio length (->5.0s)
wave, fs = rwave.convert_fs(wave, 16000, 5.0)

# Convert to MFCC
mfcc = rwave.to_mfcc('wave file path', 16000)
```


## Installation
```sh
$ pip install rwave
```


## Contributing
Bug reports and pull requests are welcome on GitHub at [https://github.com/AjxLab/RWave](https://github.com/AjxLab/RWave).
