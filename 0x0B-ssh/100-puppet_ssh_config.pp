file { '/root/.ssh':
  ensure  => 'directory',
  owner   => 'root',
  group   => 'root',
  mode    => '0700',
}


file { '/root/.ssh/school':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
}



