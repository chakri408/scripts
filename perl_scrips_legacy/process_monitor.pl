#!/usr/bin/perl

  my @services = ( 'ntpd', 'sshd', 'httpd' );
  my $alert_email = 'chakradherd\@yahoo.com';
  my $host = `/bin/hostname`;
  chomp $host;

  foreach my $service (@services) {
  my $status = `/bin/ps auxww | /bin/grep $service | /bin/grep -v grep `;
  if (!$status) {
  my $alert = `/bin/mailx -s "ALERT! $host: $service stopped" $alert_email < /dev/null > /dev/null`;
print "$alert_email \n";
   }
   }
