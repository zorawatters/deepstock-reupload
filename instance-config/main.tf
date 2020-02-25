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

  metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install flask"

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