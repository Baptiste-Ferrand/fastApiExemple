# Fastt Api Exemple
Hello me, this is just a rest api built with Fast Api for my own training 🤩

I recommande myselft to use the env python and I give me a requirements.txt for the dependance 😉

For me if i forgot how to do it 🤔 

## Using Linux

#### For create my env 
```bash
python3 -m venv venv 
```
#### For activate it
```bash
source venv/bin/activate
```
#### For install the dependance 
```bash
pip install -r requirements.txt
```
#### And if u want to touch the grass 
```bash
deactivate
```
## Generate Secret Key For JWT
First u need to copy the .env.example and rename it .env 
#### For generate the key in the .env 
```bash
echo -e "\nSECRET_KEY=$(openssl rand -hex 32)" >> .env
```
## For Starting The Api
```bash
uvicorn src.main:app --reload
``` 

## [The Swagger Documentation](http://127.0.0.1:8000/docs) (local)

And that's all there is to it: enjoy a good cup of coffee ☕☕