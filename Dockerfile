FROM python:3.8-buster
EXPOSE 42969
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
RUN mkdir myenv
ENV NLTK_DATA=myenv/nltk_data
COPY ./nltk_downloader.py ./nltk_downloader.py
RUN python3 nltk_downloader.py 
COPY hashtag ./hashtag
COPY main.py .
CMD ["uvicorn","main:app","--port","42969","--host","0.0.0.0"]