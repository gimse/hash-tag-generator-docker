FROM python:3.8-buster
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
RUN mkdir myenv
ENV NLTK_DATA=myenv/nltk_data
COPY ./nltk_downloader.py ./nltk_downloader.py
RUN python3 nltk_downloader.py 
COPY hash-tag ./hash-tag
CMD ["python3", "hash-tag/HashTagGenerator.py"]