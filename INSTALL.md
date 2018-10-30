# Installing the environment

The instructions were adapted from the [Computational Methods in Physics](http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2018/01/09/00_Setting_up_the_environment/) course, which were themselves adapted from [Software Carpentry](http://software-carpentry.org).

## Overview

You will need to install

1. [The Bash Shell](#shell)
2. [Git](#git)
3. a [text editor](#editor) (by default, `atom`)
4. [Python](#python) (including a number of additional packages required for scientific computing)

In each section, find the instructions for your operating system (Windows, macOS, or Linux).

Once you have installed everything, [test your installation](#testing).


## Setup

<p>
  To participate in the workshop, you will need access to the software described below. In addition, you will need an up-to-date web browser.
</p>
<p>
  If you encounter <strong>problems during the installation</strong> ask an instructor for help.  We also maintain resources for <a href="https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-resources/wiki/installation-troubleshooting">trouble shooting problems during the installation</a>.
</p>

<div id="shell"> <!-- Start of 'shell' section. -->
  <h3>The Bash Shell</h3>
  <p>
    Bash is a commonly-used shell that gives you the power to do simple tasks more quickly.
  </p>
  <div class="row">
    <div class="col-md-4">
      <h4 id="shell-windows">Windows</h4>
      <ol>
        <li>Download the Git for Windows <a href="https://git-for-windows.github.io/">installer</a>.</li>
        <li>Run the installer and follow the steps bellow:
          <ol>
            <!-- Git 2.6.1 Setup -->
            <!-- Welcome to the Git Setup Wizard -->
            <li>Click on "Next".</li>
            <!-- Information -->
            <li>Click on "Next".</li>
            <!-- Select Destination Location -->
            <li>Click on "Next".</li>
            <!-- Select Components -->
            <li>Click on "Next".</li>
            <!-- Select Start Menu Folder -->
            <li>Click on "Next".</li>
            <!-- Adjusting your PATH environment -->
            <li>
              <strong>
                Select "Use Git from the Windows Command Prompt" and click on "Next".
              </strong>
                If you forgot to do this programs that you need for the class will not work properly.
                If this happens rerun the installer and select the appropriate option.
            </li>
            <!-- Configuring the line ending conversions -->
            <li>
              Click on "Next".
              <strong>
                Keep "Checkout Windows-style, commit Unix-style line endings" selected.
              </strong>
            </li>
            <!-- Configuring the terminal emulator to use with Git Bash -->
            <li>
              <strong>
                Select "Use Windows' default console window" and click on "Next".
              </strong>
            </li>
            <!-- Configuring experimental performance tweaks -->
            <li>Click on "Next".</li>
            <!-- Installing -->
            <!-- Completing the Git Setup Wizard -->
            <li>Click on "Finish".</li>
          </ol>
        </li>
      </ol>
      <p>This will provide you with both Git and Bash in the Git Bash program.</p>
    </div>
    <div class="col-md-4">
      <h4 id="shell-macosx">macOS / Mac OS X</h4>
      <p>
        The default shell in all versions of macOS (formerly Mac OS X) is Bash, so no
        need to install anything.  You access Bash from the Terminal
        (found in
        <code>/Applications/Utilities</code>). You may want to keep
        Terminal in your dock for this class.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="shell-linux">Linux</h4>
      <p>
        The default shell is usually Bash, but if your
        machine is set up differently you can run it by opening a
        terminal and typing <code>bash</code>.  There is no need to
        install anything.
      </p>
    </div>
  </div>
</div> <!-- End of 'shell' section. -->

<div id='git'> <!-- Start of 'Git' section. GitHub browser compatability
           is given at https://help.github.com/articles/supported-browsers/-->
  <h3>Git</h3>
  <p>
    Git is a version control system that lets you track who made changes
    to what when and has options for easily updating a shared or public
    version of your code
    on <a href="https://github.com/">github.com</a>. You will need a
    <a href="https://help.github.com/articles/supported-browsers/">supported</a>
    web browser (current versions of Chrome, Firefox, Safari,
    Microsoft Edge, or Internet Explorer version 11 or above).
  </p>
  <div class="row">
    <div class="col-md-4">
      <h4 id="git-windows">Windows</h4>
      <p>
        Git should be installed on your computer as part of your Bash
        install (described above).
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="git-macosx">macOS / Mac OS X</h4>
      <p>
        <strong>For OS X 10.9 and higher</strong>, install Git for Mac
        by downloading and running the most recent "mavericks" installer from
        <a href="http://sourceforge.net/projects/git-osx-installer/files/">this list</a>.
        After installing Git, there will not be anything in your <code>/Applications</code> folder,
        as Git is a command line program.
        <strong>For older versions of OS X (10.5-10.8)</strong> use the
        most recent available installer labelled "snow-leopard"
        <a href="http://sourceforge.net/projects/git-osx-installer/files/">available here</a>.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="git-linux">Linux</h4>
      <p>
        If Git is not already available on your machine you can try to
        install it via your distro's package manager. For Debian/Ubuntu run
        <code>sudo apt-get install git</code> and for Fedora run
        <code>sudo yum install git</code>.
      </p>
    </div>
  </div>
</div> <!-- End of 'Git' section. -->

<div id="editor"> <!-- Start of 'editor' section. -->
  <h3>Text Editor</h3>

  <p>
    When you're writing code, it's nice to have a text editor that is
    optimized for writing code, with features like automatic
    color-coding of key words.  The default text editor on macOS and
    Linux is usually set to <a href="http://www.vim.org/">Vim</a>, which is not famous for being
    intuitive.  if you accidentally find yourself stuck in it, try
    typing the escape key, followed by <code>:q!</code> (colon, lower-case 'q',
    exclamation mark), then hitting Return to return to the shell.
  </p>

  <p>For this class we will use <a href="https://atom.io/">atom</a> as
  the default editor. It is free, open source, available on Windows,
  macOS, and Linux, powerful but also accessible for entry-level
  programmers.</p>
  
  <!-- 
    Other editors that you can consider for serious work are
	[Emacs](http://www.gnu.org/software/emacs/),
	[Vim](http://www.vim.org/) (both of which come with a steep
	learning curve), or a graphical editor such as
	[Gedit](http://projects.gnome.org/gedit/), [Sublime
	Text](https://www.sublimetext.com/). On Windows, a free editor is
	[Notepad++](http://notepad-plus-plus.org/).
	-->
  
  <div class="row">
    <div class="col-md-4">
      <h4 id="editor-windows">Windows</h4>
      <p>
	    <a href="https://atom.io/">atom</a> is a good editor that is
        suitable for professional coding but also accessible to
		newcomers with its graphical user interface.
        To install it,
        download a suitable installer from <a href="https://atom.io/">atom.io</a>
        and double click on the file to run it. (If you cannot find an
		appropriate installer, look for a file "AtomSetup-x64.exe" or
		"AtomSetup.exe" in the  <a
		href="https://github.com/atom/atom/releases/latest">list of
    latest releases</a>.)
	For more details see <a
		href="https://flight-manual.atom.io/getting-started/sections/installing-atom/#platform-windows">Installing atom on Windows</a>.
      </p>
      <p>
        Others editors that you can use are
        <a href="http://notepad-plus-plus.org/">Notepad++</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
        <strong>Be aware that you must
          add its installation directory to your system path.</strong>
        Please ask your instructor to help you do this.
      </p>
      </div>
    <div class="col-md-4">
      <h4 id="editor-macosx">macOS / Mac OS X</h4>
      <p>
		We recommend <a href="https://atom.io/">atom</a> as a good editor that is
        suitable for professional coding but also accessible to
		newcomers with its graphical user interface.
        To install it,
        download a suitable installation zip file from <a href="https://atom.io/">atom.io</a>
        and double click on the file to unpack it. Open your
		Applications directory from the Finder in the Go menu. Drag the unpacked
		Atom application to your Applications directory. (If you cannot find an
		appropriate installer, look for a file "atom-mac.zip" or
		in the  <a
		href="https://github.com/atom/atom/releases/latest">list of
		latest releases</a>.) For more details see <a
		href="https://flight-manual.atom.io/getting-started/sections/installing-atom/#platform-mac">Installing atom on Mac</a>.
        </p>
		<p>
        Alternatively, <a href="https://www.nano-editor.org/">nano</a> is a basic editor.
        It should be pre-installed.
      </p>
      <p>
        Others editors that you can use are
        <a href="http://www.barebones.com/products/textwrangler/">Text Wrangler</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="editor-linux">Linux</h4>
      <p>
		We recommend <a href="https://atom.io/">atom</a> as a good editor that is
        suitable for professional coding but also accessible to
		newcomers with is graphical user interface.
        Please follow the instructions on <a
		href="https://flight-manual.atom.io/getting-started/sections/installing-atom/#platform-linux">Installing
		atom on Linux</a> and ask an instructor for help if anything
		is unclear.
	</p>
	  <p>
	  Alternatively, <a href="https://www.nano-editor.org/">nano</a> is a basic editor.
      It should be pre-installed.
      </p>
      <p>
        Others editors that you can use are
        <a href="https://wiki.gnome.org/Apps/Gedit">Gedit</a>,
        <a href="http://kate-editor.org/">Kate</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
      </p>
    </div>
  </div>
</div> <!-- End of 'editor' section. -->

<div id="python"> 
  <h3>Python</h3>
  <p>
    <a href="http://python.org">Python</a> is a popular language for
    scientific computing, and great for general-purpose programming as
    well.  Installing all of its scientific packages individually can be
    a bit difficult, so we recommend
    <a href="https://www.anaconda.com/download/">Anaconda</a>,
    an all-in-one installer.
  </p>
    <p>
      Regardless of how you choose to install it,
      <strong>please make sure you install Python version 3.x</strong>
      (e.g., 3.4 or 3.5 is fine).
    </p>
    <p>
      We will teach Python using the Jupyter notebook, a programming environment
      that runs in a web browser. For this to work you will need a reasonably
      up-to-date browser. The current versions of the Chrome, Safari and
      Firefox browsers are all supported (some older browsers, including
      Internet Explorer version 9 and below, are not).
    </p>
<div class="row">
    <div class="col-md-4">
      <h4 id="python-windows">Windows</h4>
      <ol>
        <li>Open <a href="https://www.anaconda.com/download/">https://www.anaconda.com/download/</a> with your web browser.</li>
        <li>Download the Python 3 installer for Windows.</li>
        <li>Install Python 3 using all of the defaults for installation <em>except</em> make sure to check <strong>Make Anaconda the default Python</strong>.</li>
      </ol>
    </div>
    <div class="col-md-4">
      <h4 id="python-linux">Linux</h4>
      <ol>
        <li>Open <a href="https://www.anaconda.com/download/">https://www.anaconda.com/download/</a> with your web browser.</li>
        <li>Download the Python 3 installer for Linux.</li>
        <li>Install Python 3 using all of the defaults for installation.
        (Installation requires using the shell. If you aren't
        comfortable doing the installation yourself
        stop here and request help.)</li>
        <li>
          Open a terminal window.
        </li>
        <li>
          Type `bash Anaconda-` and then press
          tab. The name of the file you just downloaded should
          appear.
        </li>
        <li>
          Press enter. You will follow the text-only prompts.  When
          there is a colon at the bottom of the screen press the down
          arrow to move down through the text. Type <code>yes</code> and
          press enter to approve the license. Press enter to approve the
          default location for the files. Type <code>yes</code> and
          press enter to prepend Anaconda to your <code>PATH</code>
          (this makes the Anaconda distribution the default Python).
        </li>
      </ol>
    </div>
</div> <!-- End of 'Python' section. -->


## Installing Python packages

You will need to install the following packages. Install MDAnalysis with
`conda`:

```bash
conda install --channel conda-forge mdanalysis mdanalysisdata pmda
```

## Testing

### Bash shell

Open a *terminal* (macOS, Linux) or open *Git Bash* (under
*All Programs/Git/Git Bash*) in Windows.

Type

{% highlight bash %}
echo $SHELL
{% endhighlight %}

Should show `/bin/bash` or `/usr/bin/bash` (or similar).

We use "shell" and "terminal" (and "console") pretty
interchangeably.

### Git

In the shell, type

{% highlight bash %}
git --version
{% endhighlight %}

which should show something like `git version 2.7.0`.

### editor (atom)

#### First time

Open `atom` using your GUI
* Windows: from the start menu
* macOS: from the Application folder
* Linux: varies (but you might be able to skip to "From the shell"

A window should open showing the atom logo and welcome screen, similar
to 

![atom welcome screenshot]({{site.baseurl}}/{{site.figs}}/atom_welcome.jpg)

If it tries to install additional commands (`atom` and `apm`) then let
it do it and provide your system administrator password if required.

Then exit the editor again (Quit from the menu or close the
window).

#### From the shell

In the shell, type

```
atom
```

It should open the editor. Exit the editor.

If this does not work then you need to let atom install additional commands.
Open the  ([Command
Palette](http://flight-manual.atom.io/getting-started/sections/atom-basics/#command-palette)),
choosing the instructions appropriate for your platform. In the
Command Palette type `Window: Install Shell Commands` (and provide
your system administrator password if requested).


### Python

In the shell, type

```python
python -c 'import sys; print(sys.version)'
```

which should give something similar to `3.5.3 |Anaconda custom (x86_64)| (default, Mar  6 2017, 12:15:08)` (and more
stuff). Important: you should have *Python 3*, i.e., a version like
3.5.x or 3.6.x



### Jupyter notebook

<ol>
<li>
In the shell, type

```
jupyter notebook
```

This should open a browser window at <a href="http://localhost:8888">http://localhost:8888</a>. 
</li>
<li>Open the <tt>New</tt> menu on the right hand side.</li>
<li>Under <tt>Notebooks</tt> select <tt>Python</tt> or <tt>Python
[conda root]</tt> (if it is shown)</li>
<li>In the new window ("Untitled"), type
`print("Hello World!")`
and press <tt>shift</tt> and <tt>return</tt> keys simultaneously to evaluate the
cell. It should print "Hello World!".</li>
<li>Close the browser tab with menu <tt>File: Close and Halt</tt>.</li>
<li>In the files listing, select from <tt>New</tt> under <tt>Notebooks</tt> select
<tt>Python [conda root]</tt></li>
<li>Close the browser tab with menu <tt>File: Close and Halt</tt>.</li>
</ol>

<p>
If you have problems, ask an instructor.
</p>


#### Common problems

* On Windows, the `pip` or `python` commands are not found. Follow the
  steps under [solution: pip or python are not found in
  git-bash](https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-resources/wiki/installation-troubleshooting#pip-or-python-are-not-found-in-git-bash)
* On macOS, if you get the error *OSError: [Errno 49] Can't assign
  requested address* you might need to use `jupyter notebook
  --ip=127.0.0.1`
* Wrong `conda` is used. Check `which conda` in the terminal: it
  should show a path in your home directory (e.g., for user "physics":
  Windows: `/c/Users/Physics/Anaconda3/conda`, macOS:
  `/Users/physics/Anaconda3/conda`, Linux:
  `/home/physics/Anaconda3/conda`). Try exiting the terminal and open
  a new terminal (or git bash) and try again. Changes to PATH only
  take effect when a new shell is opened.

See also [troubleshooting problems during the installation](https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-resources/wiki/installation-troubleshooting)


