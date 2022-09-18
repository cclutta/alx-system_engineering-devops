# Setup a SSH client configuration file to connect to server without password

file_line { 'No password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true
}

file_line { 'Identity file conf':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true
}
