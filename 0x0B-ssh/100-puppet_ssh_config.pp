# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

augeas { 'Set IdentityFile':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set Host/*/IdentityFile ~/.ssh/school',
  ],
  onlyif  => 'match Host/*/IdentityFile[.="~/.ssh/school"] size == 0',
}

augeas { 'Turn off PasswordAuthentication':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set Host/*/PasswordAuthentication no',
  ],
  onlyif  => 'match Host/*/PasswordAuthentication[.="no"] size == 0',
}
