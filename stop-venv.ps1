Set-Location -Path ".\core-venv\Scripts\"
deactivate
Set-Location -Path ..
Set-Location -Path ..
pip freeze > requirements.txt
pip install -r .\requirements.txt