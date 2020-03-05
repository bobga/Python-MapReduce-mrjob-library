# Python-MapReduce-mrjob-library
Python MapReduce sample project with mrjob library

Python version 3.8.0

This project requires you to write four MapReduce programs. These programs should be written using Python 3  and the Python mrjob library.
Each solution should distribute computaton across multiple map and/or reducer tasks.

<h3>Part 1</h3>
Given a CSV file where each line cotains a set of numbers, write a MapReudce program which determines the maximum of all numbers in the file. <br>
<i>For example</i>, consider the following sample CSV file: <br>
2,2,3 <br>
4,3 <br>

Given this CSV file, the maximum is 4.

Entitle the python program in question part1.py. That is, entering the following command at the terminal should result in your MapReduce program being applied to fileName.csv pipenv run python part1.py fileName.csv

<h3>Part 2</h3>
Given a CSV file where each line contains a set of numbers, write a MapReduce program which determines the mean of all numbers in the file. <br>
<i>For example</i>, consider the following sample CSV file:
<p>2,2,3</p>
<p>4,3</p>

Given this CSV file, the mean is 2.8.

Entitle the python program in question part2.py. That is, entering the following command at the terminal should result in your MapReduce program being applied to fileName.csv pipenv run python part2.py fileName.csv

<h3>Part 3</h3>
Uniform Resource Locator (URL) links describe the structure of the web. Consider a CSV file where each line contains two URLs which specify a single link. That is, the first and second values on each line specify the source and destination of the link in question.<br>
<i>For examplem</i>, consider the following sample CSV file:
<p>url1,url2</p>
<p>url1,url3/p>
<p>url2,url3</p>
<p>url4,url5</p>
<p>url2,url4</p>

Given such s CSV file, write a MapReduce program which finds all paths of length two in the corresponding URL links. That is, it finds the triples of URLs(u, v, w) such taht there is a link from u to v and a link from v to w.

<i>For example</i>, the sample CSV file above contains the following paths of length two:
<p>url2,url4,url5</p>
<p>url1,url2,url3</p>
<p>url1,url2,url4</p>

Entitle the python program in question part3.py. That is, entering the following command at the terminal should result in your MapReduce program being applied th filaName.csv pipenv run python part3.py fileName.csv

<h3>part 4</h3>
Write a MapReduce program which takes as input a file containing comma seperated words and outputs for each word the lines that the word appears in. 
<i>For example</i>, consider the following file:
<p>goat,chicken,horse</p>
<p>cat,horse</p>
<p>dog,cat,sheep</p>
<p>buffalo,dolphin,cat</p>
<p>sheep</p>

The corresponding output will be the following:
<p>"buffalo" ["buffalo, dolphin, cat"]</p>
<p>"cat" ["buffalo, dolphin, cat", "cat,horse","dog,cat,sheep"]</p>
<p>"chicken" ["goat,chicken,horse"]</p>
<p>"dog" ["dog,cat,sheep"]</p>
<p>"dolphin" ["buffalo,dolphin,cat"]</p>
<p>"goat" ["goat,chicken,horse"]</p>
<p>"horse" ["cat,horse","goat,chicken,horse"]</p>
<p>"sheep" ["dog,cat,sheep","sheep"]</p>

Entitle the python program in question part4.py. That is, entering the following command at the terminal should result in your MapReduce program being applied to fileName.csv pipenv run python part4.py fileName.csv

<h3>Results</h3>

  





