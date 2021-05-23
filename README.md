# hash-tag-generator
Sample hashtag generator

python code generate hashtag from sentence

it uses python nltk module for sentence processing

## Setup (Locally)
- Install Python3.
- Clone the repo and enter the folder. 
- ``pip3 install virtualenv``
- ``virtualenv myenv``
- ``source myenv/bin/activate``
- ``pip install -r requirements.txt``
- ``python3 nltk_downloader.py ``
- ``python hash-tag/HashTagGenerator.py``

## Setup Docker (Locally)
- Install Docker
- ``docker build -t hash-tag-generator-image:latest . ``
- ``docker run hash-tag-generator-image:latest``