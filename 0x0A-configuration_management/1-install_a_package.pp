# This code will install the package puppet-list
  package  { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}