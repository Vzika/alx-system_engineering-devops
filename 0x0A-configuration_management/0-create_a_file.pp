# creates a file in /tmp

file { '/tmp/school':
  content =>'I love Puppet',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
