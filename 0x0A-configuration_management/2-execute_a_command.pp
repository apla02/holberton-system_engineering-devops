# create a manifest that kills a process named killmenow
exec { 'pkill killmenow':
    path    => '/usr/bin/',
    command => 'pkill killmenow',
}
