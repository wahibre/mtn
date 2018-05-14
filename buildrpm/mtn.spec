Name:		mtn	
Version: 	3.3
Release:	1%{?dist}
Summary:	Movie thumbnailer

Group:		Amusements/Graphics
License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/master/mtn-master.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/%{version}/archive.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/archive.tar.gz?ref=%{version}

BuildRequires:	gd-devel >= 2.1.1
BuildRequires:	ffmpeg-devel >= 3.3.1

Requires:	gd
Requires:	ffmpeg-libs

%description
Movie thumbnail generator

%prep
rm -rf ./*
tar -xf %SOURCE0
mv mtn*/* ./

%build
cd src
%make_build

%install
cd src
%make_install

%files
%{_bindir}/mtn
%{_defaultdocdir}/mtn/*
%{_mandir}/man1/mtn.1*

%clean
rm -rf %{buildroot}
rm -rf *

%changelog
* Wed May 16 2018 wahibre  <wahibre@gmx.com> - 3.3
- Added PNG image format
- Added --shadow switch to draw shadows beneath thumbnails
- Added --transparent switch to set background color as transparent
- Added -q switch to enable quiet mode (overrides -v)
- verbose mode prints MTN, GD and FFmpeg's version to output

* Tue Jan 02 2018 wahibre  <wahibre@gmx.com> - 3.2.1
- fixed final cleaning memory crashing on windows

* Tue Dec 05 2017 wahibre  <wahibre@gmx.com> - 3.2
- add -H option to disable filesize in bytes in media info

* Thu Nov 23 2017 wahibre  <wahibre@gmx.com> - 3.1
- propose new image size in case of too small thumbnails
- file size only in human readable format
- fixed blank lines between media info and additional title
- fixed freezing after reading file error

* Mon Aug 7 2017 wahibre  <wahibre@gmx.com> - 3.0
- removed old and deprecated piece of code and replaced with new FFmpeg's (3.1.8) API
- add -X option to include video extension in output filename
- add -S option to select video stream
- add -d option to set recursion depth
- return code -1 on failure
