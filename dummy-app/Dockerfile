FROM python
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENTRYPOINT [ "bash", "start.sh" ]