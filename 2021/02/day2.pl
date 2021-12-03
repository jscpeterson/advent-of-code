#!/usr/bin/perl

my ($inputFile) = @ARGV;
open(my $fh, "<", $inputFile) or die "bad file";
my $x = 0;
my $y = 0;
while (<$fh>) {
    ($action, $value) = split(' ', $_);
    $x += ($action =~ 'forward') * $value;
    $y += ($action =~ 'up') * $value;
    $y -= ($action =~ 'down') * $value;
}
print("Part 1: \033[1;37m" . $x*($y*-1) . "\033[0;m\n");
close $fh;
