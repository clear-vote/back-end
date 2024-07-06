*Turn off debug mode in production*

## SSH Config (so you can modify AWS code locally)
Insert the following ssh code
1. Ask for the key (keep it somewhere safe)
2. ```
Host flask-app-ec2
    HostName ec2-35-88-126-46.us-west-2.compute.amazonaws.com
    User ubuntu
    IdentityFile <your-key-name-here>
```

## Getting started
1. Make sure `app.run(debug=True)`
2. `source venv/bin/activate`
> starts the virtual environment
3. `python app.py`
> runs the app locally

## adding a new dependency
pip freeze > requirements.txt
> Make sure you are in the virtual environment!!

## Restarting for production on AWS EC2 instance
1. Restart and enable the flaskapp
sudo systemctl restart flaskapp && sudo systemctl enable flaskapp
2. Check the localhost
curl http://localhost:8000
3. Check the IP
curl http://35.88.126.46
*Always append http:// before any IP!*
4. (optional) If you ever change the public IP, make sure to update it in the flaskapp configuration at
/etc/nginx/sites-available/flaskapp
5. (optional) reload the configurations and restart nginx (not sure if this is necessary)


# TODO
We probably want to use lamdba for our usecase, not an EC2 instance
Amazon API Gateway: To handle incoming requests from callers and route them to your application.
AWS Lambda: For serverless computing to execute your application logic without managing servers.
Amazon RDS (Relational Database Service): To host your MySQL database.
Amazon S3: To store static assets or backup data if needed.
AWS IAM (Identity and Access Management): To manage access and permissions securely.

/etc/systemd/system/flaskapp.service
