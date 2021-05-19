# hash-tag-generator
Sample hashtag generator

python code generate hashtag from sentence

it uses python nltk module for sentence processing

## Setup
- Install Python3
- ``pip3 install virtualenv``
- ``virtualenv myenv``
- ``source myenv/bin/activate``
- ``pip install -r requirements.txt``
- ``python hash-tag/downloader.py``
- ``python hash-tag/HashTagGenerator.py``

## Setup Docker (Locally)
- Install Docker
- ``docker build -t hash-tag-generator-image:latest . ``
- ``docker run hash-tag-generator-image:latest``