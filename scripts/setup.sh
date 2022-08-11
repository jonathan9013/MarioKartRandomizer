curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install virtualenv
virtualenv -p python yourVenv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt