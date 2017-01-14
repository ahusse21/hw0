<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Meta, title, CSS, favicons, etc. -->
        <meta charset="utf-8">
    <title>CS 450: Introduction to Networking &middot; Homework 0</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Course web page for CS 450 at UIC.">
    <link rel="shortcut icon" type="image/ico" href="/~ckanich/cs450/s17/images/favicon.ico">
    <link href="/~ckanich/cs450/s17/css/bootstrap.css" rel="stylesheet">
    <link href="/~ckanich/cs450/s17/css/site.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Droid+Sans:400,700' rel='stylesheet' type='text/css'>
    
      
        <link href="/~ckanich/cs450/s17/css/syntax.css" rel="stylesheet">
      
    


    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></sc\
ript>
    <![endif]-->
    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-21532225-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>


    <!-- Place anything custom after this. -->
  </head>
  <body>
    
    <div class="navbar navbar-default navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/~ckanich/cs450/s17">CS 450: Introduction to Networking</a>
        </div>
      </div>
    </div>

    

    <div class="container">
      <div class="row">
        <div class="col-md-3">
  <div class="bs-sidebar hidden-print" >
    <ul class="nav bs-sidenav">
      

      
      
        <li ><a href="/~ckanich/cs450/s17/">home</a> </li>
        
        

      
      
        <li ><a href="/~ckanich/cs450/s17/syllabus.html">syllabus</a> </li>
        
        

      
      
        <li ><a href="/~ckanich/cs450/s17/schedule.html">schedule</a> </li>
        
        

      
      
        <li ><a href="/~ckanich/cs450/s17/homeworks.html">homeworks</a> </li>
        
        <ul class="nav">
          
            <li class="active"  ><a href="/~ckanich/cs450/s17/homework0.html">homework 0</a> </li>
          
        </ul>
        
        
        <li><a href="https://piazza.com/class/ixjtb7hqvod4n0">discussion</a></li>
    </ul>
  </div>
</div>

        <div class="col-md-9" role="main">
          <h2 id="homework-0-intro-to-python-and-git">Homework 0: Intro to Python and Git</h2>

<p><strong>This assignment is due at the start of class (3pm) on Wednesday, January 18.</strong></p>

<p>This assignment has three purposes:</p>

<ol>
  <li><a href="#using-git-section">To give you some practice using git</a>,</li>
  <li><a href="#intro-to-python-section">To get python 3.6 installed on you system</a>, and</li>
  <li><a href="#assignment-section">To do some basic tasks in python 3.6 to make sure you’re familiar with the language’s basic syntax and features</a>.</li>
</ol>

<h2 id="using-git-and-github"><a name="using-git-section"></a>Using Git and GitHub</h2>
<p>In this course you will use <a href="https://git-scm.com/">git</a> to
receive and submit your homework assignments.  We’ll be using
<a href="https://github.com/">GitHub</a> to manage all of the code provided to you, and
the homework assignments you submit.</p>

<h3 id="what-are-git-and-github">What are Git and GitHub?</h3>
<p>Git is a popular, open source version control system. It helps you keep track
of changes to your files, and helps you collaborate with others.
GitHub provides several convinces on top of git (a web interface, stores
a remote copy of your code, manages access for you etc.).  Git and GitHub are
complementary, not supplementary, tools.</p>

<p>A full introduction to git is beyond the scope of this document, but there are
<a href="https://guides.github.com/activities/hello-world/">many</a>
<a href="https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control">good</a>
<a href="https://www.git-tower.com/learn/git/ebook/en/command-line/basics/what-is-version-control#start">guides</a>
on the web that will be helpful for learning git.  For this class you will
need to understand the <a href="https://www.git-scm.com/docs/git-clone">clone</a>,
<a href="https://www.git-scm.com/docs/git-add">add</a>,
<a href="https://www.git-scm.com/docs/git-commit">commit</a> and
<a href="https://www.git-scm.com/docs/git-push">push</a>
commands in git.</p>

<p>Git is a complicated, powerful system, but learning it is valuable and worth
the time you put into it.</p>

<h3 id="getting-git">Getting Git</h3>
<p>Git may already be installed on your machine.  If it is not, you will need to
download and install git, either from the <a href="https://git-scm.com/">git</a> website,
from your linux distribution, or wherever else is most convenient.</p>

<p>All instructions in this course will be given using the command line version
of git.  Students wishing to use GUI tools will be responsible for learning
them on their own.  You are strongly encouraged to use the command line version
of git.</p>

<h3 id="using-git-in-this-course">Using Git in This Course</h3>
<p>Assignments will be given to you in git “repositories”, or code collections
that you will modify with your solutions and then resubmit.  Git tracks
directories (and sub-directories), not individual files.  When you commit
your assignment for grading, you will be submitting an entire directory tree
in git for grading, not just certain files.</p>

<p>In general, you will follow the below pattern when using git.</p>

<div class="language-bash highlighter-rouge"><pre class="highlight"><code><span class="c"># First you will copy the git repo containing the assignment to your local</span>
<span class="c"># machine.  This will give you a complete local copy of the project.</span>
<span class="c"># This will create a directory on your machine, along with some files.</span>
git clone &lt;URL to git project&gt;

<span class="c"># You will need to change and add to the files in the directory, so that</span>
<span class="c"># the entire directory matches how you'd like to submit your assignment</span>
<span class="c"># for grading.</span>
<span class="nb">cd</span> &lt;project directory&gt;
... <span class="o">(</span>editing the files to <span class="nb">complete </span>your assignment<span class="o">)</span>

<span class="c"># Once you're ready to send your work for grading.  This will generally take</span>
<span class="c"># three steps:</span>
<span class="c">#</span>
<span class="c">#   First, "add" the changes you'd like to send to the server.</span>
<span class="c">#   In most cases, this will be all the files in the directory.</span>
<span class="c">#   The "-A" in the below example tells git to also keep track of where you</span>
<span class="c">#   deleted a file, and the "." means "everything in the current directory"</span>
<span class="c">#   and below.</span>
git add -A .

<span class="c">#   Second, "commit" the changes, telling git "ok, treat all the changes</span>
<span class="c">#   I've "added" far together, I'm getting them ready to send to the</span>
<span class="c">#   server".  The "-m" means "I'm going to add a message to this set of</span>
<span class="c">#   changes, so that I'll know what they're about in the future".</span>
git commit -m <span class="s2">"completed homework 0"</span>

<span class="c">#   Third and last, "push" the changes back to the server.  This tells git</span>
<span class="c">#   "I've made some changes to the code, I want you to make the code on the</span>
<span class="c">#   server match my local version".</span>
git push
</code></pre>
</div>

<p>Git is extremely powerful, and you may need to access other parts of its
functionality in this class, but in general, the above example covers
the most common git use cases.</p>

<h3 id="when-git-breaks">When Git “Breaks”</h3>
<p>When you’re first learning git, its very easy to get your repository into
a state where it seems “broken”, and the system isn’t acting in a way
you understand.  When this happens, you might find the best thing to do
is to stop trying to “fix” things, and instead:</p>

<ol>
  <li>back up your work to a different directory,</li>
  <li>delete your existing repo from your local machine,</li>
  <li>clone a clean copy of the repo,</li>
  <li>copy your work back into the repo, and</li>
  <li>commit and push your work in your new, “clean” repo.</li>
</ol>

<p>While the above steps aren’t a good long term strategy for using git,
they can get you out of a bind while you’re still learning the tools.</p>

<h2 id="intro-to-python"><a name="intro-to-python-section"></a>Intro to Python</h2>
<p>This class requires the current version of python, <strong>Python 3.6</strong>.  Please
make sure that you are using Python 3.6 for all assignments.  Python 3
is similar to Python 2, but the two are incompatible in many ways.
Programs that work on Python 2 may not work on Python 3.  You will be
responsible for making sure your assignments work with Python 3.6.</p>

<p>If you’re unsure what version of python you are using, you can always check
by typing <code class="highlighter-rouge">python --version</code> on the command line.</p>

<p>Python is a popular, dynamic, memory managed language.  It has many features
that make it easier to work with than other languages.
If you’re already familiar with python, feel free to
skip over this section.  For those new to the language, this section
provides an overview of some of the unique features of the language.</p>

<h3 id="getting-python">Getting Python</h3>
<p>You should make sure you have Python 3.6 installed on
your computer.  You can get python by going to the
<a href="https://www.python.org/">Python website</a>, going to the download section,
and installing the appropriate download.</p>

<p>If you’re using linux, you might find it faster to use the package manager
for your linux distribution to get python (again, making sure it is the
correct version).  If you’re using OSX and have a system like
<a href="http://brew.sh/">homebrew</a> installed, you can use that to easily install
Python 3.6.</p>

<p>You are responsible for getting Python 3.6 installed.  If you have
any questions or problems, please contact the TA.</p>

<h3 id="syntax">Syntax</h3>
<p>If you’re used to languages like C and Java, python might look a little alien.
This is because python does not use curly braces (<code class="highlighter-rouge"><span class="p">{</span></code> or <code class="highlighter-rouge">}</code>) to denote
the end of blocks, or semi-colons to denote the end of lines.  Instead, Python
relies on white space.</p>

<div class="language-c highlighter-rouge"><pre class="highlight"><code><span class="c1">// In C you end up repeating yourself a lot, indenting things and wrapping
// blocks in curly braces.
</span><span class="kt">void</span> <span class="nf">a_function</span><span class="p">(</span><span class="kt">int</span> <span class="o">*</span> <span class="n">firstArg</span><span class="p">,</span> <span class="kt">int</span> <span class="o">*</span> <span class="n">secondArg</span><span class="p">)</span> <span class="p">{</span>
    <span class="c1">// You also repeat yourself, but using both ";" and new lines
</span>    <span class="c1">// to mark the end of a line of code.
</span>    <span class="kt">int</span> <span class="n">firstInt</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
    <span class="kt">int</span> <span class="n">secondInt</span> <span class="o">=</span> <span class="mi">2</span><span class="p">;</span>
<span class="p">}</span>
</code></pre>
</div>

<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c"># In Python, you type less, and have less redundancy.  You</span>
<span class="c"># may find that this reduces the number of errors you make, and makes</span>
<span class="c"># your programs easier to maintain.</span>
<span class="k">def</span> <span class="nf">a_function</span><span class="p">(</span><span class="n">first_arg</span><span class="p">,</span> <span class="n">second_arg</span><span class="p">):</span>
    <span class="n">first_int</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">second_int</span> <span class="o">=</span> <span class="mi">2</span>
</code></pre>
</div>

<h3 id="dynamic-types">Dynamic Types</h3>
<p>Languages like Java and C require you to declare types in function signatures
and variable declarations.  If, for example, you’re writing a program C, you
and you want to declare a variable to be an integer, and another variable to
be a character, you need to do something like the following:</p>

<div class="language-c highlighter-rouge"><pre class="highlight"><code><span class="cp">#include &lt;stdio.h&gt;
</span>
<span class="c1">// Defining some variables in C
</span><span class="kt">int</span> <span class="n">myInt</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span>
<span class="kt">char</span> <span class="n">someChar</span> <span class="o">=</span> <span class="sc">'a'</span><span class="p">;</span>

<span class="c1">// Defining a function in C
</span><span class="kt">int</span> <span class="nf">some_function</span><span class="p">(</span><span class="kt">int</span> <span class="n">anInt</span><span class="p">,</span> <span class="kt">char</span> <span class="n">aChar</span><span class="p">)</span> <span class="p">{</span>
    <span class="n">printf</span><span class="p">(</span><span class="s">"Here is the integer I was given: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">anInt</span><span class="p">);</span>
    <span class="n">printf</span><span class="p">(</span><span class="s">"And here is the character I was given: %c</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">aChar</span><span class="p">);</span>
    <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>

<span class="c1">// C programs always start with the main function
</span><span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">int</span> <span class="n">argc</span><span class="p">,</span> <span class="kt">char</span> <span class="o">*</span> <span class="n">argv</span><span class="p">[])</span> <span class="p">{</span>
    <span class="c1">// Calling a function in C
</span>    <span class="n">some_function</span><span class="p">(</span><span class="n">myInt</span><span class="p">,</span> <span class="n">someChar</span><span class="p">);</span>
<span class="p">}</span>
</code></pre>
</div>

<p>In most ways, python is much less strict about types.  You don’t specify a
type when you declare a variable, and variables can take on values of any type,
even changing over the lifetime of your program.  The below, for example,
is valid python code:</p>

<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c"># Defining some variables in python.  Note that we don't define any</span>
<span class="c"># types, python does that automatically.</span>
<span class="n">my_int</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">some_char</span> <span class="o">=</span> <span class="s">"a"</span>

<span class="c"># Defining a function in python.  Note that you don't declare types</span>
<span class="c"># for the arguments in python, the language handles that for you.</span>
<span class="c"># We also don't have to declare a return type, thats handled automatically</span>
<span class="c"># too.</span>
<span class="k">def</span> <span class="nf">some_function</span><span class="p">(</span><span class="n">an_int</span><span class="p">,</span> <span class="n">a_char</span><span class="p">):</span>
    <span class="k">print</span><span class="p">(</span><span class="s">"Here is the integer I was given:"</span><span class="p">,</span> <span class="n">an_int</span><span class="p">)</span>
    <span class="k">print</span><span class="p">(</span><span class="s">"And here is the character I was given:"</span><span class="p">,</span> <span class="n">a_char</span><span class="p">)</span>

<span class="n">some_function</span><span class="p">(</span><span class="n">my_int</span><span class="p">,</span> <span class="n">some_char</span><span class="p">)</span>
</code></pre>
</div>

<h3 id="native-data-structures">Native Data Structures</h3>
<p>Python provides many conveniences for defining and working with data structures
compared to languages like Java and C.  Python doesn’t
allow you to do anything you can’t do in Java and C, Python makes it much
easier, and much less error prone, to interact with structures like arrays
(which python calls <em>lists</em>), hash tables (which python calls <em>dicts</em>), and
sets (which python calls… <em>sets</em>).</p>

<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c"># In python, you can define an array (or, in python terms, a list) of</span>
<span class="c"># variables in line, and then loop over them easily.  The below code</span>
<span class="c"># creates a list / array of three strings, and then prints them all out.</span>
<span class="n">list_of_strings</span> <span class="o">=</span> <span class="p">[</span><span class="s">"first"</span><span class="p">,</span> <span class="s">"second"</span><span class="p">,</span> <span class="s">"third"</span><span class="p">]</span>

<span class="c"># Python provides this short hand syntax for iterating over each element</span>
<span class="c"># in a list.  In C, you might use a for loop and index into each element</span>
<span class="c"># in the list.</span>
<span class="c">#</span>
<span class="c"># The below list will print out the following text:</span>
<span class="c">#</span>
<span class="c">#   first</span>
<span class="c">#   second</span>
<span class="c">#   third</span>
<span class="k">for</span> <span class="n">a_string</span> <span class="ow">in</span> <span class="n">list_of_strings</span><span class="p">:</span>
    <span class="k">print</span><span class="p">(</span><span class="n">a_string</span><span class="p">)</span>

<span class="c"># We can do the same thing with a hash table, or a mapping of values</span>
<span class="c"># to values.  The below code maps the names of numbers (as strings) to</span>
<span class="c"># their actual value (as integers).</span>
<span class="n">number_mapping</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s">"one"</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
    <span class="s">"two"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
    <span class="s">"three"</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
<span class="p">}</span>

<span class="c"># Now we loop over each item in the hash table (or dict) we created,</span>
<span class="c"># which will produce the following lines (though the order is</span>
<span class="c"># unpredictable).</span>
<span class="c">#</span>
<span class="c">#   one can also be written as 1</span>
<span class="c">#   two can also be written as 2</span>
<span class="c">#   three can also be written as 3</span>
<span class="k">for</span> <span class="n">string_version</span><span class="p">,</span> <span class="n">int_version</span> <span class="k">for</span> <span class="n">number_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="k">print</span><span class="p">(</span><span class="n">string_version</span><span class="p">,</span> <span class="s">"can also be written as"</span><span class="p">,</span> <span class="n">int_version</span><span class="p">)</span>
</code></pre>
</div>

<h3 id="large-standard-library">Large Standard Library</h3>
<p>Python comes with a large standard library, and includes “out of the box”
a large amount of functionality to help you complete common tasks.
This is true compared to Java, and <em>especially</em> compared to C. This reduces the
amount of third party code you need in Python to complete common tasks.</p>

<p>A full list of all the functionality included in the
<a href="https://docs.python.org/3.6/library/index.html">python standard library</a>
can be found online.</p>

<h3 id="other-python-features">Other Python Features</h3>
<p>The above just scratches the surface of what makes python an interesting
and useful language.  Python has powerful object oriented tools like Java,
closures and anonymous functions like Lisp and JavaScript, and
a full module system for structuring your code and taking advantage of code
written by others.</p>

<p>You wont be using most of these features in this class,
but they’re in the language and it will benefit you to learn more about them
as you become more familiar with the language.</p>

<h3 id="writing-better-python">Writing Better Python</h3>
<p>There are great tools to help you become a better python programmer, and to
help you write better, cleaner, less-bug-laden code.  Its highly recommended
that you use these tools, and they can help you catch, fix and prevent errors,
and write code that will be easier to understand if you ever need to revist
them (plus, if you ever use any of these assignments as code samples in a job
application, its a good thing to show that you’re familiar with and already
following python best practices.</p>

<p>One tool is <a href="https://pep8.readthedocs.io/en/release-1.7.x/">pep8</a>, a command
line tool that checks that your code is following python formatting and style
best practices.  Making that your code is well formatted will make it easier
to understand, revisit, revise, and help you avoid
<a href="https://gotofail.com/">subtle errors</a>.  You should check that your
code matches the <code class="highlighter-rouge">pep8</code> style wherever possible.</p>

<p><a href="https://www.pylint.org/">pylint</a> is another code quality tool.  It checks
that your code is well documented, well formatted, and avoids practices
that can make your code confusing and fragile.  You should also consider
using <code class="highlighter-rouge">pylint</code> to check all the python code you submit in this course.</p>

<p>For this assignment, using <code class="highlighter-rouge">pep8</code> and <code class="highlighter-rouge">pylint</code> is not required, just highly
recommended.  However, it may be required on future assignments.  Please
familarize yourself with these tools as soon as possible.</p>

<h2 id="assignment"><a name="assignment-section"></a>Assignment</h2>
<p>The goal of this assignment is to test your use of basic git features,
that you have Python 3.6 installed on your system, and that you’re familiar with
the basics of the language.</p>

<h3 id="programming"><a name="programming-assignment-description"></a>Programming</h3>
<p>Once you have python installed, write a python program that prints out the
following things, one on each line:</p>

<ol>
  <li>Your email address.</li>
  <li>Your name, as a list, with each part of your name as a different string
in a list.  So, for the TA, it would be the result of printing a list
with three strings in it, “peter”, “edwin” and “snyder”.  Please use
all lower case characters.</li>
  <li>The current date and time, matching the following format:
<code class="highlighter-rouge">2017-01-10 00:43:13.073277</code>. (in otherwise, with the year, then the month,
then the date, followed by the current hour, minute, second and
millisecond).</li>
  <li>
    <p>Define a function called <code class="highlighter-rouge">four</code> that takes three arguments, <code class="highlighter-rouge">start</code>, <code class="highlighter-rouge">stop</code>,
and <code class="highlighter-rouge">step</code>.  The function should assume that each argument will be an
integer.  This function should return a list of integers, starting at
the <code class="highlighter-rouge">start</code> integer, and increasing by the <code class="highlighter-rouge">step</code> integer, up to but
<strong>not including</strong> the <code class="highlighter-rouge">stop</code> integer.</p>

    <p>For example, if I called <code class="highlighter-rouge">four(10, 50, 10)</code>, the function should return
the list <code class="highlighter-rouge">[10, 20, 30, 40]</code> (note that 50 is not included).</p>

    <p>Similarly, if I called <code class="highlighter-rouge">four(2, 9, 3)</code>, the function should return
<code class="highlighter-rouge">[2, 5, 8]</code>.</p>

    <p>Print the result of calling your <code class="highlighter-rouge">four</code> function with the arguments 17, 40,
and 6 (ie <code class="highlighter-rouge">print(four(17, 40, 6))</code>).</p>
  </li>
  <li>The current version of python.</li>
</ol>

<h3 id="hints-and-notes">Hints and Notes</h3>
<p>For <strong>number 2</strong>, your program should give results of printing the list with
the parts of your name in it.  No need to do any fancy string formatting
or anything like that.  Just use the <code class="highlighter-rouge">print</code> function on the list of strings.</p>

<p>Similarly, for <strong>number 3</strong>, you must determine the current date and time using python.
<em>Do not</em> hard code something into your code.  The
<a href="https://docs.python.org/3.6/library/datetime.html#datetime.datetime.now">datetime</a>
module will be helpful.</p>

<p>For <strong>number 4</strong>, you can use any function or functionality in the python
standard library to help you in this task, even ones that have
<a href="https://docs.python.org/3.6/library/functions.html#func-range">very similar functionality</a>.
Just make sure that you are returning a list. <strong>Bonus hint</strong>, you can convert
from a <a href="https://docs.python.org/3.6/library/functions.html#func-range">range</a>
to a <code class="highlighter-rouge">list</code> (which the homework requires) using
<a href="https://docs.python.org/2/library/functions.html#list">list</a>. Make
sure your function is returning a <code class="highlighter-rouge">list</code> to receive credit.</p>

<p>For <strong>number 5</strong>, <em>do not</em> hard code the version of python into your code (i.e. do
not write <code class="highlighter-rouge">print("3.6")</code>).  You must use the python system for printing the
current version to receive credit.  The <a href="https://docs.python.org/3.6/library/sys.html#sys.version">sys</a>
module will be helpful.</p>

<p>Also for <strong>number 5</strong>, depending on your environment, python might print your
python version on more than one line.  That is not a problem.</p>

<h3 id="testing-your-program">Testing Your Program</h3>
<p>You should test your program before submitting it.  In python, this is as
simple is running <code class="highlighter-rouge">python hw0.py</code> (or, depending on your platform
and environment, possibly <code class="highlighter-rouge">python3 hw0.py</code>).</p>

<h3 id="submission-and-grading">Submission and Grading</h3>
<p>You must submit your solution to this assignment through git.  When you submit
your assignment, your project should have (at least) the following three files
in it:</p>

<ul>
  <li><code class="highlighter-rouge">README.md</code>: this file</li>
  <li><code class="highlighter-rouge">hw0.py</code>: your solution to this homework assignment</li>
  <li><code class="highlighter-rouge">netid.txt</code>: a text file that contains only your UIC NetID.  It should not
contain anything else.</li>
</ul>

<p>There are a total of <strong>10 possible points</strong> for this assignment.</p>

<ul>
  <li><strong>5 points</strong> for having your UIC Net ID in the <code class="highlighter-rouge">netid.txt</code> file.</li>
  <li><strong>1 point</strong> for each of the 5 problems in the
<a href="#programming-assignment-description">Programming Assignment Description</a>
section, when executing <code class="highlighter-rouge">hw0.py</code>.</li>
</ul>

<p>There is no partial credit for any problem.  Other files in your repository
will be ignored.</p>

<p><strong>This assignment is due at the start of class (3pm) on Wednesday, January 18.</strong></p>

        </div>
      </div>
    </div>
    <!-- Footer
    ================================================== -->
    <div class="clearfix"></div>
    <footer class="bs-footer" role="contentinfo">
    <div class="container">    
         <ul class="footer-links">
          <li><a href="https://www.cs.uic.edu/~ckanich/">Chris Kanich</a></li>
          <li class="muted">&middot;</li>
          <li><a href="https://www.cs.uic.edu/">UIC Computer Science</a></li>
        </ul>
    </div>
    </footer>
    <!-- JS and analytics only. -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="//code.jquery.com/jquery.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="/~ckanich/cs450/s17/js/bootstrap.min.js"></script>



  </body>
</html>


