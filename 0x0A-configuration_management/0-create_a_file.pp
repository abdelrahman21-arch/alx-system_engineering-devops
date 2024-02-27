# This puppet manifest creates a file in the tmp dir.

file{ 'school' :
  path   => '/tmp/school',
  ensure =>file,
  owner =>'www-data',
  group =>'www-data',
  mode => '0744',
  content =>'I love Puppet',
}
