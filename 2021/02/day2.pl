#!/usr/bin/perl
use v5.10; 

my ($inputFile) = @ARGV;
print("Part 1: \033[1;37m" . silver($inputFile) . "\033[0;m\n");
print("Part 2: \033[1;33m" . gold($inputFile) . "\033[0;m\n");

sub silver {
   open(my $fh, "<", $inputFile) or die "bad file";
   my $x = 0;
   my $y = 0;
   while (<$fh>) {
       ($action, $value) = split(' ', $_);
       $x += ($action =~ 'forward') * $value;
       $y += ($action =~ 'up') * $value;
       $y -= ($action =~ 'down') * $value;
   }
   close $fh;
   return $x*($y*-1);
}

sub gold {
   open(my $fh, "<", $inputFile) or die "bad file";
   my $x = 0;
   my $y = 0;
   my $aim = 0;
   while (<$fh>) {
       ($action, $value) = split(' ', $_);
       if ($action =~ 'forward') {
           $x += $value; 
           $y -= $aim * $value;
       } elsif ($action =~ 'up') {
           $aim -= $value;
       } elsif ($action =~ 'down') {
           $aim += $value;
       } 
   }
   close $fh;
   return $x*($y*-1);;
}
