# This Puppet manifest kills a process named 'killmenow' using pkill

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}
