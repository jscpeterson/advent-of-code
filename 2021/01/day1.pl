#!/usr/bin/perl

my ($inputFile) = @ARGV;
open(my $fh, "<", $inputFile) or die "bad file";
my @measurements = <$fh>; 
my $count = 0;
for (my $i = 1; $i <= $#measurements; $i++) {
   $count += $measurements[$i] > $measurements[$i-1];
}
print("Part 1: \033[1;37m" . $count . "\033[0;m\n");
$count = 0;
for (my $i = 1; $i <= $#measurements; $i++) {
   $sum = $measurements[$i] + $measurements[$i+1] + $measurements[$i+2];
   $lastSum = $measurements[$i-1] + $measurements[$i] + $measurements[$i+1];
   $count += $sum > $lastSum;
}
print("Part 2: \033[1;33m" . $count . "\033[0;m\n");
close $fh;
