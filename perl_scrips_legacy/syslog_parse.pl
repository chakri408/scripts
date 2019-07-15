#!/usr/bin/perl
$check = `ps -auxww | grep ntp | grep -v grep`;
$Log_not= "logger 'ntp processnot running'";
$Log_yes= "logger 'ntp process running' ";
if(!$check){
#system (logger "ntp process not running");
system ($Log_not);
 # print "process not running";
}else{
 # print "process running";
system ($Log_yes);

}
#print "\n";
