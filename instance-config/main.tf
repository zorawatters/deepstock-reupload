variable "cred_key_path" {
  type = string
}

variable "name" {
  type = string
}

provider "google" {
	credentials = "${file(var.cred_key_path)}"
	project = "deep-stock-268818"
	region	= "us-central1"
	zone		= "us-central1-c"
}

resource "google_compute_instance" "vm_instance" {
  name         = var.name
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  metadata_startup_script=<<-EOT
  sudo apt-get install -yq git-all
  sudo apt-get update
  printf "#! /bin/bash \nsudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.9/install.sh | bash \nexport NVM_DIR=\"\$HOME/.nvm\" \n[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\""> /tmp/setup-nvm.sh
  printf "#! /bin/bash \nif [ -a /var/tmp/first-login ]; then \necho \"Returning Customer\"\nelse \necho \"First Time\" \n\. /tmp/setup-nvm.sh \ntouch /var/tmp/first-login \nnvm install stable \necho \"Node version: \" \nnode -v \nfi" > /etc/profile.d/first-login-prompt.sh
  EOT

  metadata = {
    enable-oslogin="TRUE"
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "default"

    access_config {
    }
  }
  
}

output "ip" {
  value = "${google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip}"
}