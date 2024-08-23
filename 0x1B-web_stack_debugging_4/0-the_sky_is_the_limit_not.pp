# This Puppet manifest optimizes Nginx for high concurrency by adjusting key configuration parameters.

exec { 'tune-nginx':
  command => 'sed -i -e "s/worker_processes 1;/worker_processes auto;/" \
                      -e "s/worker_connections 768;/worker_connections 1024;/" \
                      -e "s/# multi_accept on;/multi_accept on;/" \
                      /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin:/usr/bin',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['tune-nginx'],
}

# Ensure Apache is not running as Nginx should handle all requests.
service { 'apache2':
  ensure => stopped,
}
