# EmergingAssigment

set FLASK_APP=MachineLearning.py<br>
python -m flask run<br>
docker build . -t assigment-image<br>
docker run --name rando-container -d -p 5000:5000 assigment-image<br>