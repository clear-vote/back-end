## *Turn off debug mode in production!!*

## SSH Config (so you can modify AWS code locally)
Insert the following ssh code
1. Ask for the key (keep it somewhere safe)
2. Add the following SSH info to your config
> Host flask-app-ec2
>     HostName ec2-35-88-126-46.us-west-2.compute.amazonaws.com
>     User ubuntu
>     IdentityFile <your-key-name-here>


## Getting started
1. Make sure `app.run(debug=True)` in app.py
2. Run `source venv/bin/activate` to start your virtual environment
3. Run `python app.py` to start locally (optional)

## adding a new dependency
1. Run `pip freeze > requirements.txt` *in the virtual environment*
> Make sure you are in the virtual environment!!

## (we are moving away from this) Restarting for production on AWS EC2 instance
1. Restart and enable the flaskapp: `sudo systemctl restart flaskapp && sudo systemctl enable flaskapp`
2. Check the localhost `curl -v http://localhost:8000`
3. Check the IP `curl http://35.88.126.46/?longitude=0&latitude=0`... *Always append http:// before any IP!*
4. (optional) If you ever change the public IP, make sure to update it in the flaskapp configuration at /etc/nginx/sites-available/flaskapp
5. (optional) reload the configurations and restart nginx. You can also modify gunicorn /etc/systemd/system/flaskapp.service

## Lambda
1. Run the following
cp lambda_function.py my-deployment-package/
cp -r venv/lib/python3.x/site-packages/* my-deployment-package/
2. Push to GH
3. Download zip from GH
4. Deploy via AWS Lambda

## TODO
Amazon RDS (Relational Database Service): To host your MySQL database.
Amazon S3: To store static assets or backup data if needed.
AWS IAM (Identity and Access Management): To manage access and permissions securely.

