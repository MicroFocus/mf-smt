#!/usr/bin/env perl

use SMT::Mirror::Job;
use Test::Simple tests => 2;

$job = SMT::Mirror::Job->new();
$job->uri( "http://download.opensuse.org/repositories/home:/dmacvicar/openSUSE_10.3" );
$job->resource( "/repodata/repomd.xml" );
$job->localdir( "./testdata/jobtest/" );
ok($job->modified() > 0);
ok($job->outdated());
