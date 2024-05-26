# Dash 

### Overview
This repository will include my different projects when it comes to the [Python Dash](https://dash.plotly.com/) Python library which is an original low-code framework for rapidly building data apps in Python. 
### Virtual Environment
I was having issues going through the regular installation steps: https://dash.plotly.com/installation, so I just decided to create a virtual environment. 

Virtual Environment:

1. Navigate to your root directory that will contain all of your Dash folders. Create a virtual environment using the following command:

```python
python3 -m venv venv # create a venv folder
source venv/bin/activate # go into the venv environment
```

2. Now, we need to install the necessary packages for Dash inside of the virtual environment, which we can do with: 

```python
pip install dash pandas # install dash and pandas
```

3. Now, we are inside of our virtual environment. Next, navigate to the particular folder that you want to run, then run `python app.py` where `app.py` is the name of the file that you want to run. This will create a Flask app on a specific port where you can make your edits.