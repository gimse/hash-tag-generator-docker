# hash-tag-generator
Sample hashtag generator

python code generate hashtag from sentence

it uses python nltk module for sentence processing

## Example
Input: "This is a pretty cool day, i loved being here"

Output: "{'#day', '#loved', '#cool', '#pretty'}"

## Setup (Locally)
- Install Python3.
- Clone the repo and enter the folder. 
- ``pip3 install virtualenv``
- ``virtualenv myenv``
- ``source myenv/bin/activate``
- ``pip install -r requirements.txt``
- ``python3 nltk_downloader.py ``
- ``uvicorn main:app --reload --port 42969``
- Open the docs: http://127.0.0.1:42969/docs
- Run example: http://127.0.0.1:42969/v1/hashtags?text=I%20still%20love%20you


## Setup Docker (Online)
- Install Docker
- Pull the newest [image](https://github.com/users/gimse/packages/container/package/hash-tag-generator-docker%2Fhash-tag-generator-docker). For example: ``docker pull ghcr.io/gimse/hash-tag-generator-docker/hash-tag-generator-docker:1.1.0``
- ``docker run -p 42969:42969 docker pull ghcr.io/gimse/hash-tag-generator-docker/hash-tag-generator-docker:1.1.0
## Setup Docker (Locally)
- Install Docker
- ``docker build -t hash-tag-generator-image:latest . ``
- ``docker run hash-tag-generator-image:latest``