FROM python:3.7-slim
ADD whatsapp.py /whatsapp.py
RUN pip install --target=/app requests
RUN pip install twilio
RUN chmod +x /whatsapp.py
CMD ["python", "/whatsapp.py"]