# install a specific package using pip3 on puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
