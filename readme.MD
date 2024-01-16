## Dependencies required
* Create a virtual environment using this command in project directory
  ```
  python3 -m  venv venv
  ```
* Then activate the python virtual environment using this command in the same directory
  ```
  source venv/bin/activate
  ```
* Now install following dependencies
  ```
  brew install ghostscript tcl-tk
  ```
* Now install following python dependencies
  ```
  pip install opencv-python
  pip install 'camelot-py[cv]'
  ```
* Once all the dependencies are installed, run python file.
  ```
  python3 main_3.py
  ```

`Running this command will create a output.csv file. ` 

`There is already one sample file in the input/ directory. Run the script as it is to see a working result in output.csv.`

`To convert multiple pdf files, just copy the pdf files in input/ directory and the script will automatically pick it.`

` (main_3.py)  script is best working script as of now,`

