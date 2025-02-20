echo make a venv for you
python3 -m venv venv
echo activate the venv
source venv/bin/activate
echo install the pip package for system. (in venv)
pip install tqdm psutil rich PyYAML pytz requests
echo start the system (in venv)
python main.py