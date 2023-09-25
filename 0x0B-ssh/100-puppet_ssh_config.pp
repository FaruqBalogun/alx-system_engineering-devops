#!/usr/bin/env bash
# Using puppet to comment without password

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path    => 'etc/ssh/ssh_config',
  line    => '^PasswordAuthentication',
}

file_line  { 'Declare identitiy file':
  path      => 'etc/ssh/ssh_config',
  line      => 'identityfile ~/.ssh/school',
  match     => '^#identityFile',
}
