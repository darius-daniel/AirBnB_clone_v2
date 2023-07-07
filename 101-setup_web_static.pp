# A Manifest that redoes the task #0 but by using Puppet

exec { "install-ngix":
    provider => shell,
    command  => "sudo apt -y update; sudo apt install -y nginx",
    before   => Exec['mkdir_test']
}

exec { "mkdir_test":
    provider => shell,
    command  => "sudo mkdir -p /data/web_static/releases/test/",
    before   => Exec['mkdir_shared']
}

exec { "mkdir_shared":
    provider => shell,
    command  => "sudo mkdir -p /data/web_static/releases/shared/",
    before   => Exec['create_dummy_html']
}

exec { "create_dummy_html":
    provider => shell,
    command  => "sudo echo 'Hello World!' > /data/web_static/releases/test/index.html",
    before   => Exec['rm_existing_symbolic_link']
}

exec { "rm_existing_symbolic_link":
    provider => shell,
    command  => "sudo rm /data/web_static/current",
    before   => Exec['create_new_link']
}

exec { "create_new_link":
    provider => shell,
    command  => "sudo ln -s /data/web_static/releases/test/ /data/web_static/current",
    before   => Exec['change_ownership']
}

exec { "change_ownership":
    provider => shell,
    command  => "sudo chown -R ubuntu:ubuntu /data/ ; sudo chmod -R 777 /data/",
    before   => Exec['configure_and_restart_nginx']
}

exec { "configure_and_restart_nginx":
    provider => shell,
    command  => "sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default ; sudo service nginx restart",
    before   => Exec['exit_success']
}

exec {"exit_success":
    provider => shell,
    command  => "exit 0"
}
