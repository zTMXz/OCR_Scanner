# OCR_Scanner
To run the application you need:
1. Python 3.9.5
2. Install all libraries from requirements.txt (pip install -r requirements.txt)
3. Link the database to the project (you need to do this in settings.py)
4. Run migrations (manage.py makemigrations then migrate)
5. Create superuser (manage.py createsuperuser)
6. Run the project (manage.py runserver)

To use tensorflow with gpu delete TF and Keras and install them manually:
1. pip install tensorflow==2.10
2. pip install keras==3.10

To use EasyOcr with gpu delete torch, torchvision, easyocr and install them manually: 
1. pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
2. pip install easyocr
