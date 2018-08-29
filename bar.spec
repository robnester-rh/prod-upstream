%global package_name hello
%global spec_release 4
%global commit 8a891d803ca877be90c62b64345709c6af89eb4b

Name:     hello
Version:  2.10
Release:  1
Summary:  The "Hello World" program from GNU
License:  GPLv3+
URL:      https://www.gnu.org/software/hello/
Source0:  https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%changelog
* Mon Aug 27 2018 Steven Engineer <whatDoesThisButtonDo@example.com>
- Fixed this
- Fixed that
- Broke something else, probably

* Thu Jul 07 2018 The Coon of Ty <Ty@coon.org> - 2.10-1
- Initial version of the package
