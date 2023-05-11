#!/bin/bash

echo 'hi from the pre generation hook';

export PATH=$PATH:/bin
whoami
uptime

echo 'hi after the path change the pre generation hook';


curl 'https://www.google.com'
