[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)o

# Tower QE Dashboard

A set of Tower QE dashboard that allows to have better insight of what is going on

## Install

### Production

### Development

To be able to set up a dev environment, few steps are required.

  1. Ensure `pip` and `virtualenv` are installed

  ```bash
  #> yum -y install python-pip python-virtualenvironment
  ```

  2. Create yourself a virtual environment

  ``` bash
  #> virtualenv /path/to/towerdasboard/venv
  #> source /path/to/towerdashboard/venv
  ```

  3. Clone the repository

  ``` bash
  #> git clone https://github.com/Spredzy/tower-dashboard
  ```

  4. Install the dependencies

  ``` bash
  #> cd tower-dashboard
  #> pip install -r requirements.txt
  ```

  5. Copy and edit the settings.sample.py file

  ``` bash
  #> cp settings.sample.py /tmp/settings.py
  #> vim /tmp/settings.py
  ```

  5. Rock'n'Roll

  ``` bash
  #> FLASK_APP=/path/to/towerdashboard/app.py FLASK_DEBUG=1 TOWERDASHBOARD_SETTINGS=/tmp/settings.py flask run
  ```

tower-dashboard should be running on your local loop on port 5000 (`http://127.0.0.1:5000`)


## License

Apache 2.0


## Contact

  * Tower QE  <ansible-tower-qe@redhat.com>
