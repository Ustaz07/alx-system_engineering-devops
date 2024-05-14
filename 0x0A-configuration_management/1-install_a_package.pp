# Ensure Flask and Werkzeug are installed via pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '>=2.0', # Make sure Werkzeug is at least version 2.0
  provider => 'pip3',
}
