# DeepStock
BigData Project


## Instance Setup
A Terraform config file is located in the instance-config folder. In order for it to work correctly you must download a service account key from the GCP console, then create a file called terraform.tfvars, with contents  
```
cred_key_path="deep-stock-service-key.json"
name="YOUR_NAME-instance"
```
__If you name your key something other than what is listed above, make sure to add it to the .gitignore file.__

Then make sure terraform is properly setup on your computer, then run `terraform init` while inside the instance-config directory. After that run `terraform apply`, and your instance will be created in the DeepStock GCP project.  
After confirming the creation, wait 3-4 minutes, then ssh into the instance through the GCP console.  
Clone the DeepStock repo into your home directory, then start development.
