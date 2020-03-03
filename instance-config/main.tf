variable "cred_key_path" {
  type = string
}

variable "name" {
  type = string
}

variable "git_public" {}
variable "git_private" {}

provider "google" {
	credentials = "${file(var.cred_key_path)}"
	project = "deep-stock-268818"
	region	= "us-central1"
	zone		= "us-central1-c"
}

resource "google_compute_instance" "vm_instance" {
  name         = var.name
  machine_type = "f1-micro"
  tags         = ["http", "http-server"]
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  metadata_startup_script=<<-EOT
  sudo apt-get install -yq git-all
  sudo apt-get -y update  
  sudo apt-get install -yq build-essential python3-pip rsync
  sudo apt-get install -yq nginx
  sudo apt-get install -yq python3-venv
  printf "#! /bin/bash \nsudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.9/install.sh | bash \nexport NVM_DIR=\"\$HOME/.nvm\" \n[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\""> /tmp/setup-nvm.sh
  printf "#! /bin/bash \nmkdir \$HOME/.ssh \ncat > \$HOME/.ssh/deep-stock-git-key <<-EOT \n${file(var.git_private)}" > /tmp/create-private-key.sh
  printf "#! /bin/bash \necho \"${file(var.git_public)}\" > \$HOME/.ssh/deep-stock-git-key.pub" > /tmp/create-public-key.sh
  printf "#! /bin/bash \nsudo service apache2 stop \nif [ -a /var/tmp/first-login ]; then \necho \"Returning Customer\"\nelse \necho \"First Time\" \n\. /tmp/setup-nvm.sh \n\. /tmp/create-private-key.sh \n\. /tmp/create-public-key.sh \nchmod 400 \$HOME/.ssh/deep-stock-git-key \neval \"\$(ssh-agent -s)\" \nssh-add \$HOME/.ssh/deep-stock-git-key \ntouch /var/tmp/first-login \nnvm install stable \necho \"Node version: \" \nnode -v \nssh-keyscan github.com >> \$HOME/.ssh/known_hosts \ngit clone git@github.com:CUBigDataClass/DeepStock.git \nfi" > /etc/profile.d/first-login-prompt.sh
  EOT

  metadata = {

  }

  network_interface {
    # A default network is created for all GCP projects
    network = "default"

    access_config {
    }
  }
}

resource "google_compute_firewall" "default" {
  name    = "flask-app-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "5000"]
  }
  target_tags=["http"]
}

output "ip" {
  value = "${google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip}"
}