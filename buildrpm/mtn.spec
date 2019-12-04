Name:		mtn	
Version: 	3.3.3
Release:	1%{?dist}
Summary:	Movie thumbnailer

Group:		Amusements/Graphics
License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/master/mtn.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/%{version}/archive.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/archive.tar.gz?ref=%{version}

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gd-devel >= 2.0.35
BuildRequires:	ffmpeg-devel >= 3.3.1

Requires:	gd
Requires:	ffmpeg-libs

%description
Movie thumbnail generator

%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: bash-completion
Requires: fontconfig
Enhances: mtn

%description bash-completion
Bash completion support for the %{name}'s utilities.

%package zsh-completion
Summary: Zsh completion support for %{name}
BuildArch: noarch
Requires: zsh
Requires: fontconfig
Enhances: mtn

%description zsh-completion
Zsh completion support for the %{name}'s utilities.

%prep
rm -rf ./*
tar -xf %SOURCE0
mv mtn*/* ./

%build
cd src
%make_build

%install
cd src
%make_install PREFIX=%{_prefix}

## Make bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 ../completions/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -pm644 ../completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%{_bindir}/mtn
%{_defaultdocdir}/mtn/*
%{_mandir}/man1/mtn.1*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%clean
rm -rf %{buildroot}
rm -rf *

%changelog
* Fri Nov 29 2019 wahibre  <wahibre@gmx.com> - 3.3.3
- bash completion
- zsh completion

* Thu May 30 2019 wahibre  <wahibre@gmx.com> - 3.3.2
- add install prefix

* Mon Aug 7 2017 wahibre  <wahibre@gmx.com> - 3.0
- initial
