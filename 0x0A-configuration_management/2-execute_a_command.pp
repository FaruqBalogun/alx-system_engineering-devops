#The code below kills  & works together with killmenow file which has been provided
  exec  { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
