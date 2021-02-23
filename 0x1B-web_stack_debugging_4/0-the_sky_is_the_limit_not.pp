# set up limits to request 
exec { 'increasing_limits':
    command => 'sudo sed -i "s/15/15000/" /etc/default/nginx;
    	        sudo service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
