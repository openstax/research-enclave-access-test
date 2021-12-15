FROM python:latest
WORKDIR /app
COPY Highlights_BarGraph.py ./
RUN python -m pip install --upgrade pip
RUN python -m pip install pandas
RUN python -m pip install matplotlib
CMD [ "python", "./Highlights_BarGraph.py"]