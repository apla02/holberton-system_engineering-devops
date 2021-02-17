# Using strace, find out why Apache is returning a 500 error. 
exec { 'fixing_settings':
    command => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
